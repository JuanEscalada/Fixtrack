from datetime import datetime

from app import db


class Repair(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    customer = db.Column(db.String(100), nullable=False)
    item = db.Column(db.String(100), nullable=False)
    problem = db.Column(db.Text, nullable=False)

    status = db.Column(
        db.String(30),
        nullable=False,
        default="Received",
    )

    estimated_price = db.Column(db.Float)
    final_price = db.Column(db.Float)

    notes = db.Column(db.Text)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False,
    )