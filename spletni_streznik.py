import bottle

@bottle.get('/')
def zacetek():
    return bottle.template('naslov.tpl')

bottle.run(debug=True, reloader=True)