from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Witaj w tym smutnym jak pizda świecie.'

if __name__ == '__main__':
    app.run()
