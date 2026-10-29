
from bottle import run, route, view, static_file

# ROUTE FOR PAGES

@route('/')
@view('home')
def home():
    return {}

@route('/pillartwo')
@view('pillartwo')
def pillartwo():
    return {}

@route('/pillarone')
@view('pillarone')
def pillarone():
    return {}

# ROUTE FOR STATIC FILES

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

# START
run(host='localhost', port=8080, debug=True, reloader=True)