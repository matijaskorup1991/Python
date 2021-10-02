
from user import User

# users = [

#     User(1, "bob", "1234")
#     # {
#     #     "id": 1,
#     #     "username": "bob",
#     #     "password": "asdf"
#     # }
# ]

# username_mapping = {
#     # govori nam da ce usermaping objekt biti kolekcija od usernames in users a u users nam se trenuto nalazi samo jedan objekt
#     u.username: u for u in users
# }

# userid_mapping = {
#     u.id: u for u in users
#     # 1: {
#     #     "id": 1,
#     #     "username": "bob",
#     #     "password": "asdf"
#     # }
# }


def authenticate(username, password):
    # user = username_mapping.get(username, None)
    user = User.find_by_username(username)

    if user and user.password == password:
        return user


def identity(payload):
    user_id = payload["identity"]
    return User.find_by_id(user_id)
