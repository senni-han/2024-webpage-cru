from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, <a href="/page2">CRU</a>'

@app.route('/page2')
def hello_page2():
    return '<h1 style="text-align:center">Welcome to CRU.<h1/><br/><a href="/"><p style="text-align:center">Go back.<a/>'

app.run()
