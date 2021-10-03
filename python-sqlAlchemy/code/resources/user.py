import sqlite3
from flask_restful import Resource, reqparse


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