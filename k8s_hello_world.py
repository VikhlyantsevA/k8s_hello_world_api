from flask import Flask
import socket

app = Flask(__name__)

@app.route("/hello_world")
def hello_world():
    return f"<p>Version1: Hello, World from {socket.gethostname()}! </p>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)