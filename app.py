import flask

app = flask.Flask(__name__)


@app.get('/')
def index():
    return "Hello world"


@app.get('/about')
def about():
    return "This is a demo app, it's simple"
