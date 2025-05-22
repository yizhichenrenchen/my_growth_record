from flask import Flask
app = Flask(__name__)

@app.route('/')
def me():
    return '<p>Hello, World!</p>'
@app.route('/hello')
def index():
    return '<p>Hello, World</p>'
@app.route('/hi')
def hi():
    return '<p>hi!</p>'

if __name__ == '__main__':
    app.run(debug=True)

