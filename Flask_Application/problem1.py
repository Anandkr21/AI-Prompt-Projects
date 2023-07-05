from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome'

@app.route('/hello/<name>')
def hello(name):
    return f'Hello {name}'

@app.route('/Goodbye/<name>')
def good(name):
    return f'Goodbye {name}'

if __name__ == '__main__':
    app.run(port=5000)
