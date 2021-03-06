import sqlite3
from flask_restful import Resource, reqparse


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    def find_by_username(self, username):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "select * from users where username = ?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = User(*row)
        else:
            user = None

        connection.close()
        return user

    def find_by_id(self, _id):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "select * from users where id = ?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = User(*row)
        else:
            user = None

        connection.close()
        return user


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str,
                        required=True, help="Username is required")
    parser.add_argument("password", type=str,
                        required=True, help="Password is required")

    def post(self):

        data = UserRegister.parser.parse_args()
        # print(data["username"])

        # if User.find_by_username(data["username"]):
        #     return {"message": "user already registered"}, 400

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "insert into users values(null,?,?)"
        cursor.execute(query, (data["username"], data["password"],))
        connection.commit()
        connection.close()

        return {"message": "user created successfully"}, 201
