from db import db


class ItemModal(db.Model):

    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {"name": self.name, "price": self.price}

     # class method,
    # mozemo ju pisati i sa @classmethod i onda umijesto parametra self staviti cls
    def save_to_db(self):
        # sqlalchemy automatski radi ili insert ili update
        db.session.add(self)
        db.session.commit()

    # # @classmethod
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        # Select * from items where name=name limit=1
        return ItemModal.query.filter_by(name=name).first()
        # connection = sqlite3.connect("data.db")
        # cursor = connection.cursor()

        # query = "SELECT * FROM items where name = ?"
        # result = cursor.execute(query, (name,))
        # row = result.fetchone()

        # connection.close()

        # if row:
        #     return ItemModal(*row), 200

        # return {"item": {"name": row[0], "price": row[1]}}, 200
