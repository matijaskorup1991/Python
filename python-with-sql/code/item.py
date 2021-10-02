from flask_restful import Resource, reqparse
import sqlite3


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price", type=float, required=True,
                        help="This field cannot be left blank")
    # @jwt_required

    def get(self, name):
        try:
            item = self.find_by_name(name)
        except:
            return {"message": "failded to fetch items"}, 500
        if item:
            return item
        return {"message": "Item not found"}, 404

    # class method,
    # mozemo ju pisati i sa @classmethod i onda umijesto parametra self staviti cls
    def insert(self, item):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "insert into items values(?,?)"
        cursor.execute(query, (item["name"], item["price"]))

        connection.commit()
        connection.close()

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "update items set price=? where name=?"

        cursor.execute(query, (item["price"], item["name"]))

        connection.commit()
        connection.close()

    def find_by_name(self, name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT * FROM items where name = ?"
        result = cursor.execute(query, (name,))

        row = result.fetchone()

        connection.close()

        if row:
            return {"item": {"name": row[0], "price": row[1]}}, 200

    def post(self, name):
        if self.find_by_name(name):
            return {'message': "an item with name '{}' already exists".format(name)}, 400

        data = Item.parser.parse_args()
        item = {
            "name": name,
            "price": data["price"]
        }

        try:
            self.insert(item)
        except:
            return {"message": "an error occurred inserting item into intems"}, 500

        return item, 201

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
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "delete from items where name=?"

        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        # global items zato sto nam u metodi ispod python prvo misli da se radi o items varijabli koja se nalazi u klassi
        # global items
        # items = list(filter(lambda x: x["name"] != name, items))
        return {"message": "Item deleted"}

    def put(self, name):

        # data = request.get_json()
        data = Item.parser.parse_args()

        item = self.find_by_name(name)

        updatet_item = {
            "name": name, "price": data["price"]
        }

        # item = next(filter(lambda x: x["name"] == name, items), None)
        if item is None:
            try:
                self.insert(updatet_item)
            except:
                return {"message": "an error occurred while inserting item"}, 500
        else:
            try:
                self.update(updatet_item)
            except:
                return {"message": "an error occurred while updating item"}, 500

        return updatet_item


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
