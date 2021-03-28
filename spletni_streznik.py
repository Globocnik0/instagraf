import bottle
import os
from ustvarjalec_grafov import *
from login_manager import *

app = bottle.default_app()
bottle.BaseTemplate.defaults['get_url'] = app.get_url

@bottle.route('/database/<filename:path>', name='database')
def serve_static(filename):
    return bottle.static_file(filename, root= os.path.join(os.getcwd(),'..', "database"))

@bottle.route('/graphs_made/<filename:path>', name='graphs_made')
def serve_static(filename):
    return bottle.static_file(filename, root= os.path.join(os.getcwd(),'..', "graphs_made"))


@bottle.get('/en/login/')
def login_get():
    return bottle.template('login.tpl')

@bottle.post('/en/login/')
def login_post():
    username = bottle.request.forms['username']
    password = bottle.request.forms['password']
    # cookies = bottle.request.GET.get("first_login")
    # print(cookies)
    return bottle.template('login.tpl')

@bottle.get('/')
def redirect():
    bottle.redirect('/en/')

@bottle.get('/sl/')
def zacetek_sl():
    return bottle.template('naslov.tpl', base='Pozdravljen na strani, kjer se ustvarjanje grafov začne.')

@bottle.get('/en/')
def zacetek_en():
    return bottle.template('naslov.tpl', base='Welcome to the page where the making of graphs begins.')


@bottle.post('/en/upload/')
def upload_file():
    data = bottle.request.files.data #tukaj je ena napaka ki je še ne razumem .data bi se dal zapisat drugače
    tittle = bottle.request.forms.tittle #.forms['tittle']
    x_label = bottle.request.forms.x_label
    y_label = bottle.request.forms.y_label
    fit = bottle.request.forms.fit

    global filename
    filename = data.filename
    if data and data.file and filename.endswith((".txt", ".csv", ".xlsx", ".XLSX")):
        with open(os.path.join(os.getcwd(),'..', "uploaded_files", filename), "wb") as file:
            global Data
            Data = data.file.read()
            file.write(Data)

        make_graph(filename = os.path.join(os.getcwd(),'..', "uploaded_files", filename), tittle = tittle, x_label = x_label, y_label = y_label, fit = fit)
        bottle.redirect('/en/graph/')
    return "You missed a field or uploaded an unsupported file type"


@bottle.get('/en/graph/')
def upload_result():
    x = os.path.splitext(os.path.basename(filename))[0] + '.png'
    print(x)
    return bottle.template('stran_z_grafom.tpl', 
                            base = "Congratulations, your file %s (%d bytes) has been uploaded and a graph was made from it." % (filename, len(Data)),
                            graph_filename = x)

bottle.run(debug=True, reloader=True)
