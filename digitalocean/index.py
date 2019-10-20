from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@socketio.on('call', namespace='/space')
def rtc_call(mes):
        socketio.emit('call', {
                'description': mes['description'],
                'room': mes['room'],
        }, namespace='/space')

@socketio.on('answer', namespace='/space')
def rtc_answer(mes):
        socketio.emit('answer', {
                'description': mes['description'],
                'room': mes['room'],
        }, namespace='/space')

@socketio.on('cand1', namespace='/space')
def rtc_cond1(mes):
        socketio.emit('cand1', {
                'description': mes['description'],
                'room': mes['room'],
        }, namespace='/space')

@socketio.on('cand2', namespace='/space')
def rtc_cond2(mes):
        socketio.emit('cand2', {
                'description': mes['description'],
                'room': mes['room'],
        }, namespace='/space')

if __name__ == '__main__':
    socketio.run(app,host='127.0.0.1', port=5050)
