from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = "123456"
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = [

]

# sa flask restful ne moramo koristiti jsonify


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price", type="float", required=True,
                        help="This field cannot be left blank")
    # @jwt_required

    def get(self, name):
        item = next(filter(lambda x: x["name"] == name, items), None)
        return {"item": item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x["name"] == name, items), None):
            return {'message': "an item with name '{}' already exists".format(name)}, 400
        # force = True nam govori da ne trebamo content header, ne preporuca se
        # silent=True ne vraca nam error ako data ne postoji

        data = Item.parser.parse_args()

        # data = request.get_json()

        item = {
            "name": name,
            "price": data["price"]
        }
        items.append(item)
        return item, 201

    def delete(self, name):
        # global items zato sto nam u metodi ispod python prvo misli da se radi o items varijabli koja se nalazi u klassi
        global items
        items = list(filter(lambda x: x["name"] != name, items))
        return {"message": "Item deleted"}

    def put(self, name):

        # data = request.get_json()
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x["name"] == name, items), None)
        if item is None:
            item = {
                "name": name, "price": data["price"]
            }
            items.append(item)
        else:
            item.update(data)
        return item


class ItemList(Resource):
    def get(self):
        return {"items": items}


api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")

app.run(port=5000, debug=True)
