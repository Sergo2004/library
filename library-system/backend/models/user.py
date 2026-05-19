from app import db

class Reader(db.Model):
    __tablename__ = 'readers'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(50))
    email = db.Column(db.String(255))
