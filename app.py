from bottle import run, route, template, view, static_file

# ROUTE FOR PAGES

@route('/pillartwo')
@view('pillartwo') 
def pillartwo():
    return template('pillartwo')

@route('/home')
@view('home')
def home():
    pass

@route('/pillarone')
@view('pillarone')
def pillarone():
    pass

# ROUTE FOR STATIC FILES (CSS, images, JS)
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

# START OVER

run(host='localhost', port='8080', debug=True, reloader=True)
