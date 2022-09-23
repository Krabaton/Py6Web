import datetime

from gino import Gino

db = Gino()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, **kw):
        super().__init__(**kw)
        self._messages = set()

    @property
    def messages(self):
        return self._messages

    @messages.setter
    def add_message(self, message):
        self._messages.add(message)


class Messages(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(255), nullable=False)
    created = db.Column(db.DateTime, default=datetime.datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='cascade'))

    def __repr__(self):
        return self.message