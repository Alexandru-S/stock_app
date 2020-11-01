from flask import session
from flask_socketio import emit, join_room
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
    ticker = pdr.get_data_yahoo(message["value"],start=message['start'], end=message['end'])
    data = yf.download(tickers="SPY AAPL MSFT",period="1d",interval="1m",group_by='ticker',auto_adjust=True,prepost=True,threads=True,proxy=None)
    print('-----------------------------------', data)
    emit('message', {'msg': data.to_json(orient='table')}, room=room)
