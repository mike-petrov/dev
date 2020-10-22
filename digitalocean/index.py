from flask import Flask, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["400 per day", "70 per hour"]
)

@socketio.on('call', namespace='/space')
def rtc_call(mes):
        socketio.emit('call', {
                'description': mes['description'],
                'room': mes['room'],
        }, namespace='/space')

@app.route('/geo', methods=['POST'])
@limiter.limit("10 per minute")
def geo():
    return jsonify({ 'server': 'true' })

if __name__ == '__main__':
	app.run(
		host='127.0.0.1',
		port='5051',
		debug=True,
		threaded=True,
	)
