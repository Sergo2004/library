from app import db

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    isbn = db.Column(db.String(50), unique=True)
    publication_year = db.Column(db.Integer)
    category = db.Column(db.String(100))
    copies_total = db.Column(db.Integer, default=1)
    copies_available = db.Column(db.Integer, default=1)
