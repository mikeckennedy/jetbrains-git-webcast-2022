import flask

__VERSION__ = '0.0.1'

app = flask.Flask(__name__)

print(f'App starting up, version {__VERSION__}')


@app.get('/')
def index():
    # This is the index
    print("Indexing!")
    return flask.render_template('index.html')


@app.get('/about')
def about():
    return "This is a demo app, it's simple"
