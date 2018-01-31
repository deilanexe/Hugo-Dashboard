from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hugo Dashboard API diff'


if __name__ == '__main__':
    app.run()
