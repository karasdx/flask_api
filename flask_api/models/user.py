from db import db
from datetime import datetime

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    created_at = db.Column(db.DateTime(), default=datetime.now)
    updated_at = db.Column(db.DateTime(), default=datetime.now, onupdate=datetime.now)

    def __init__(self, name, email, password, created_at, updated_at):
        self.name = name
        self.email = email
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at

    def json(self):
        return {'name': self.name, 'email': self.email, 'password': self.password}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()