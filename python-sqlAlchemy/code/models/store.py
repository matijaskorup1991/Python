from db import db


class StoreModel(db.Model):

    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    # ako koristimo lazy="dynamic" onda items nije automatski lista (jer to bi mogla biti teska operacija za bazu podataka ovisno o tome koliko elemenata ima u bazi )
    # ali zato u metodi json moramo staviti umijesto self.items, self.items.all()
    items = db.relationship("ItemModal", lazy="dynamic")

    def __init__(self, name):
        self.name = name

    def json(self):
        return {"name": self.name, "items": [item.json() for item in self.items.all()]}

     # class method,
    # mozemo ju pisati i sa @classmethod i onda umijesto parametra self staviti cls
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # # @classmethod
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return StoreModel.query.filter_by(name=name).first()
