from app import app, db
from app import socketio
from flask_socketio import emit
from app.models import Booking
import json

@app.route('/')
def index():
    print("Hello!")

@socketio.on('my_event', namespace='/test')
def test_message(message):
    print(message)
    emit('my_response',
         {'data': message['data']})

@socketio.on('my_event', namespace='/test')
def test_json(data):
    data = json.loads(data)

    b = Booking(id=data['id'], user_id = data['user_id'], vehicle_model_id=data['vehicle_model_id'], package_id=data['package_id'], travel_type_id=data['travel_type_id'],
    from_area_id=data['from_area_id'], to_area_id=data['to_area_id'], from_city_id=data['from_city_id'], to_city_id=data['to_city_id'], from_date=data['from_date'],
    to_date=data['to_date'], online_booking=data['online_booking'], mobile_site_booking=data['mobile_site_booking'], booking_created=data['booking_created'],
    from_lat=data['from_lat'], from_long=data['from_long'], to_lat=data['to_lat'], to_long=data['to_long'], Car_Cancellation=data['Car_Cancellation'])
    db.session.add(b)
    db.session.commit()
    emit('my_response',
         {'data': data['id']})

@socketio.on('connect', namespace='/test')
def test_connect():
    print("Helloooooo")
    emit('my_response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')