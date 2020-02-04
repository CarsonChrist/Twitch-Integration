from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def hello_world():
    return render_template("home.html")


@app.route("/left")
def left():
    print("left")
    socketio.emit("left")


@app.route("/right")
def right():
    print("right")
    socketio.emit("right")


if __name__ == '__main__':
    socketio.run(app, debug=True)
