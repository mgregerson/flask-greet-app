from flask import Flask

app = Flask(__name__)

@app.get('/welcome')
def welcome_statement():
    """Return a welcome statement"""

    html = "<html><body><h1>welcome</h1></body></html>"
    return html

@app.get('/welcome/home')
def welcome_home():
    """Returns Welcome Home"""

    html = "<html><body><h1>welcome home</h1></body></html>"
    return html

@app.get('/welcome/back')
def welcome_back():
    """Returns Welcome back"""

    html = "<html><body><h1>welcome back</h1></body></html>"
    return html