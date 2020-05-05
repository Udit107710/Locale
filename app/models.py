from app import db
from datetime import datetime

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80))
    vehicle_model_id = db.Column(db.String(80))
    package_id = db.Column(db.String(80))
    travel_type_id = db.Column(db.String(80))
    from_area_id = db.Column(db.String(80))
    to_area_id = db.Column(db.String(80))
    from_city_id = db.Column(db.String(80))
    to_city_id = db.Column(db.String(80))
    from_date = db.Column(db.String(80))
    to_date = db.Column(db.String(80))
    online_booking = db.Column(db.String(80))
    mobile_site_booking =db.Column(db.String(80))
    booking_created = db.Column(db.String(80))
    from_lat = db.Column(db.String(80))
    from_long = db.Column(db.String(80))
    to_lat = db.Column(db.String(80))
    to_long = db.Column(db.String(80))
    Car_Cancellation = db.Column(db.String(80))

    def __repr__(self):
        return '<Booking {}>'.format(self.id)