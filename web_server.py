import bottle
import os
from graph_maker import *
#from graph_maker_class import *
from login_manager import *

app = bottle.default_app()
bottle.BaseTemplate.defaults['get_url'] = app.get_url

@bottle.route('/database/<filename:path>', name='database')
def serve_static(filename):
    return bottle.static_file(filename, root= os.path.join(os.getcwd(),'..', "database"))

@bottle.route('/graphs_made/ALES/<filename:path>', name='graphs_made/ALES') #daj vse v isto mapo, ni treba name=...
def serve_static(filename):
    username = bottle.request.get_cookie('Logged')
    return bottle.static_file(filename, root= os.path.join(os.getcwd(),'..', "graphs_made", 'ALES'))

# @bottle.route('/graphs_made/<filepath:path>', name='graphs_made')
# def server_static(filepath):
#     username = bottle.request.get_cookie('Logged')
#     return bottle.static_file(filepath, root=os.path.join(os.getcwd(),'..', "graphs_made"))


@bottle.get('/en/login/')
def login_get():
    if bottle.request.get_cookie('Logged'):
        return "You are logged in" #naredi spletno stran ali message
    return bottle.template('login.tpl', alert = '')

@bottle.post('/en/login/')
def login_post():
    username = bottle.request.forms['username']
    password = bottle.request.forms['password']
    first_time_user = bottle.request.forms.first_login
    if first_time_user == 'on':
        if User(username, password).valid_characters():
            if User(username, password).username_exists():
                return bottle.template('login.tpl', alert = 'This username is already taken. Please choose another one')#mogoče bi mogel redirectat na .get/en/login/
            else:
                User(username, password).add_account()
        else:
            return bottle.template('login.tpl', alert = 'Only permitted characters are A-Z, a-z, 0-9.')
    else:
        if User(username, password).correct_password():
            bottle.response.set_cookie('Logged', username, path='/en/')
            bottle.redirect('/en/')
        else:
            return bottle.template('login.tpl', alert = 'wrong password or not registered')
    return bottle.template('login.tpl', alert ='')

@bottle.get('/')
def redirect():
    bottle.redirect('/en/')

@bottle.get('/sl/') #tukaj bi lahko naredil še slovensko različico
def zacetek_sl():
    return bottle.template('naslov.tpl', base='Pozdravljen na strani, kjer se ustvarjanje grafov začne.')

@bottle.get('/en/')
def zacetek_en():
    if bottle.request.get_cookie('Logged'):
        if User(bottle.request.get_cookie('Logged')).username_exists():
            return bottle.template('naslov.tpl', base='Welcome %s to the page where the making of graphs begins.' % bottle.request.get_cookie('Logged'), alert = '')
        else:
            return bottle.template('login.tpl', alert = 'Nice try. Police is heading your way!')
    else:
        bottle.redirect('/en/login/')

@bottle.post('/en/')
def log_out():
    bottle.response.set_cookie('Logged', '', path='/en/', expires=0)
    bottle.redirect('/en/')


@bottle.post('/en/upload/')#ni mi treba novega linka
def upload_file():
    data = bottle.request.files.data 
    tittle = bottle.request.forms['tittle']
    x_label = bottle.request.forms['x_label']
    y_label = bottle.request.forms['y_label'] #šumniki delajo
    fit = bottle.request.forms.fit

    username = bottle.request.get_cookie('Logged')

    global filename
    filename = data.filename
    add_graph_to_account(username = username, filename = filename, title = tittle, x_label = x_label, y_label = y_label, fit = fit)
    if data and data.file and filename.endswith((".txt", ".csv", ".xlsx", ".XLSX")):
        with open(os.path.join(os.getcwd(),'..', "uploaded_files", filename), "wb") as file:
            global Data
            Data = data.file.read()
            file.write(Data)

        bottle.redirect('/en/graph/')
    return bottle.template('naslov.tpl', base='Welcome %s to the page where the making of graphs begins.' % bottle.request.get_cookie('Logged'), alert = 'You missed a field or uploaded an unsupported file type')


@bottle.get('/en/graph/') #problem če imajo datoteke isto ime, treba preusmerit če ni prijavljen-poglej piškotke
def show_graphs():
    username = bottle.request.get_cookie('Logged')
    graphs = read_graphs_from_account(username = bottle.request.get_cookie('Logged'))
    for graph in graphs:
        # graph_class = uploaded_data(username = username, filepath = os.path.join(os.getcwd(),'..', "uploaded_files", graph['filename']), title = graph['title'], x_label = graph['x_label'], y_label = graph['y_label'], fit = graph['fit'])
        # graph_class.read_file()
        # graph_class.make_fit() #napaka: prevečkrat fitta
        # graph_class.make_and_save_graph()
        
        make_graph(username = username,filename = os.path.join(os.getcwd(),'..', "uploaded_files", graph['filename']), tittle = graph['title'], x_label = graph['x_label'], y_label = graph['y_label'], fit = graph['fit'])

    return bottle.template('stran_z_grafom.tpl', 
                            base = "Congratulations, your file has been uploaded and a graph was made from it." ,
                            graphs = graphs,
                            username = username)

bottle.run(debug=True, reloader=True)
#poženi iz roota
#pep 8 formatter
