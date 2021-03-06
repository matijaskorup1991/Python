import sqlite3
from db import db

# from resources.user import User


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self,  username, password):
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(self, username):
        user = UserModel.query.filter_by(username=username).first()
        return user

    @classmethod
    def find_by_id(self, _id):
        return UserModel.query.filter_by(id=_id).first()

        # connection = sqlite3.connect("data.db")
        # cursor = connection.cursor()

        # query = "select * from users where id = ?"
        # result = cursor.execute(query, (_id,))
        # row = result.fetchone()
        # if row:
        #     user = User(*row)
        # else:
        #     user = None

        # connection.close()
        # return user

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
