from flask_restful import Resource, reqparse
import sqlite3
from models.item import ItemModal


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price", type=float, required=True,
                        help="This field cannot be left blank")

    # @jwt_required

    def get(self, name):
        # testItem = ItemModal.find_by_name(name)
        # print(testItem)

        # pokusavas pozvati metodu direktno na klasu
        item = ItemModal.find_by_name(name)

        if item:
            return item.json()
        return {"message": "Item not found"}, 404

    def post(self, name):
        # if ItemModal.find_by_name(name):
        #     return {'message': "an item with name '{}' already exists".format(name)}, 400

        data = Item.parser.parse_args()
        item = ItemModal(name, data["price"])

        try:
            item.save_to_db()
        except:
            return {"message": "an error occurred inserting item into intems"}, 500

        return item.json(), 201

        # if next(filter(lambda x: x["name"] == name, items), None):
        #     return {'message': "an item with name '{}' already exists".format(name)}, 400
        # # force = True nam govori da ne trebamo content header, ne preporuca se
        # # silent=True ne vraca nam error ako data ne postoji

        # data = Item.parser.parse_args()

        # # data = request.get_json()

        # item = {
        #     "name": name,
        #     "price": data["price"]
        # }
        # items.append(item)
        # return item, 201

    def delete(self, name):
        item = ItemModal.find_by_name(name)
        if item:
            item.delete_from_db()
        # global items zato sto nam u metodi ispod python prvo misli da se radi o items varijabli koja se nalazi u klassi
        # global items
        # items = list(filter(lambda x: x["name"] != name, items))
        return {"message": "Item deleted"}

    def put(self, name):

        # data = request.get_json()
        data = Item.parser.parse_args()

        item = ItemModal.find_by_name(name)

        # item = next(filter(lambda x: x["name"] == name, items), None)
        if item is None:
            item = ItemModal(name, data["price"])
        else:
            item.price = data["price"]

        item.save_to_db()

        return item.json()


class ItemList(Resource):

    def get(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "select * from items"

        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({"name": row[0], "price": row[1]})

        # commit nam treba samo ako nesto spremamo
        # connection.commit()
        connection.close()

        return {"items": items}
