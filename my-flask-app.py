from flask import Flask
from mongoengine import connect

app = Flask(__name__)

@app.route('/')
def hello():
    return {'hello': 'world'}


def main():
    connect('project1')
    app.run(host='0.0.0.0', port='5000')



