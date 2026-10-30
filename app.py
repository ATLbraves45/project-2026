from bottle import run, route, view, static_file, TEMPLATE_PATH
import os

# Tell Bottle where the templates are
TEMPLATE_PATH.insert(
    0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'views')
)

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
    return static_file(
        filename,
        root=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    )

# START
run(host='localhost', port=8080, debug=True, reloader=True)
