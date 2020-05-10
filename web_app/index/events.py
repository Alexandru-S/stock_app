from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio
import yfinance as yf

@socketio.on('message')
def handle_message(message):
    print("MMMEE================")
    print("-±§"*21)
    print('received message: ' + message)

@socketio.on('joined', namespace='/chat')
def joined(message):
    print("JJJOOOIIINNNNEEDDDDDD")
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    join_room(room)
    emit('status', {'msg': session.get('name') + ' has entered the room.'}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    print("|TEXTTTTTTTTT|", message)
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get('room')
    print("06848055885", room)
    emit('message', {'msg': session.get('name') + ':' + message['msg']})


@socketio.on('something', namespace='nothing')
def something(message):
    print('=========', message)


@socketio.on('left', namespace='/chat')
def left(message):
    print("LEEEEEFFFTTTTTTTTTTTT")
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)