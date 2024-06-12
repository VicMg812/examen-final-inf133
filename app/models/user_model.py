import json
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from app.database import db

class Customer(UserMixin, db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email= db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    phone= db.Column(db.String(50), unique=True, nullable=False)
    roles = db.Column(db.String(50), nullable=False)
    def __init__(self, name,email, password,phone, roles=["customer"]):
        self.name = name
        self.email=email
        self.phone=phone
        self.roles = json.dumps(roles)
        self.password_hash = generate_password_hash(password)
    def save(self):
        db.session.add(self)
        db.session.commit()
    @staticmethod
    def find_by_name(name):
        return Customer.query.filter_by(name=name).first()