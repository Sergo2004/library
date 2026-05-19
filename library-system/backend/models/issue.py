from app import db

class Issue(db.Model):
    __tablename__ = 'issues'

    id = db.Column(db.Integer, primary_key=True)

    reader_id = db.Column(
        db.Integer,
        db.ForeignKey('readers.id')
    )

    book_id = db.Column(
        db.Integer,
        db.ForeignKey('books.id')
    )

    issue_date = db.Column(db.Date)
    return_date = db.Column(db.Date)
    actual_return_date = db.Column(db.Date)
    fine = db.Column(db.Numeric(10, 2), default=0)
