from flask import Flask
import requests
import socket

app = Flask(__name__)


@app.route("/")
def hello_world():
    return f"<p>Version1.1.0: Api was run on {socket.gethostname()}! </p>"


@app.route("/nginx")
def nginx_start_page():
    url = 'http://nginx:8080'
    return requests.get(url).text


@app.route("/jsonplaceholder/posts")
def jsonplaceholder_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    return requests.get(url).json()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
