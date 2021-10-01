from flask import Flask, jsonify, request


app = Flask(__name__)
stores = [
    {
        "name": "my_store",
        "items": [
            {
                "name": "my_item",
                "price": 15.99
            }
        ]
    }
]


# POST /store data:{name}


@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items": []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route("/store/<string:name>")
def get_store(name):
    for item in stores:
        if item["name"] == name:
            return jsonify(item)
    return jsonify({"message": "store not found"})


@app.route("/store")
def get_stores():
    return jsonify({"stores": stores})


@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    request_data = request.get_json()
    for item in stores:
        if item["name"] == name:
            new_item = {
                "name": request_data["name"],
                "price": request_data["price"]
            }
            item["items"].append(new_item)
            return jsonify(new_item)
    return jsonify({"message": "store not found"})


@app.route("/store/<string:name>/item")
def get_items_in_store(name):
    for item in stores:
        if item["name"] == name:
            return jsonify({"items": item["items"]})
    return jsonify({"message": "store not found"})


app.run(port=5000)
