from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio
print('event imported')
@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)