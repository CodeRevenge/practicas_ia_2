from flask import Flask
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
app.config['SECRET KEY'] = 'secret!'
socket = SocketIO(app)

@app.route('/')
def index():
    emit("hola")
    return "Hola"


if __name__ == "__main__":
    port = int(os.environ.get('PORT',5000))
    host = '0.0.0.0'
    socket.run(app, host, port, debug=True, use_reloader=True)