from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()


@socketio.on('joined', namespace='/chat')
def joined(message):
    room = session.get('room')
    join_room(room)
    emit('status', {'msg': session.get('name') + ' has entered the room.'}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    room = session.get('room')
    ticker = pdr.get_data_yahoo(message["msg"],start="2017-01-01", end="2017-04-30")
    emit('message', {'msg': ticker.to_json(orient='table')}, room=room)
