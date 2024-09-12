from flask import Flask # type: ignore

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello, World!</h1>'

if __name__ == '__main__':
    app.run(debug=True, port=8001)