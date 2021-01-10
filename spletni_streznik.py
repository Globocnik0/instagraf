import bottle

@bottle.get('/')
def zacetek():
    return bottle.template('naslov.tpl')


@bottle.post('/upload')
def do_upload():
    name = bottle.request.forms.name
    data = bottle.request.files.data
    if name and data and data.file:
        filename = data.filename

        with open(filename, "wb") as file:
            Data = data.file.read()
            if type(Data) == bytes: file.write(Data)
            elif type(Data) == str: file.write(Data.encode("utf-8"))

        return "Hello %s! You uploaded %s (%d bytes)." % (name, filename, len(Data))
    return "You missed a field."

bottle.run(debug=True, reloader=True)