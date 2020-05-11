from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
import json

@socketio.on('message')
def handle_message(message):
    print("MMMEE================")
    print("-±§"*21)
    print('received message: ' + message)

@socketio.on('joined', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    print("jpined rooom ====", room )
    join_room(room)
    emit('status', {'msg': session.get('name') + ' has entered the room.'}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    print("|TEXTTTTTTTTT|", message)
    room = session.get('room')
    ticker = pdr.get_data_yahoo(message["msg"])

    print('ticker', type(ticker))
    print("06848055885", room)
    emit('message', {'msg': session.get('name') + ':' + ticker}, room=room)


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