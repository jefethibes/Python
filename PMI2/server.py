import flask

app = flask.Flask(__name__)


@app.route('/')
def login():
    return flask.render_template('login.html')


app.run(debug=True)