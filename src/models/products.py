from config.db import db


class Producto(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    Nombre = db.Column(db.String(45))
    Precio = db.Column(db.Integer())
    Cantidad = db.Column(db.Integer())

    def __init__(self, Nombre,Precio,Cantidad):
        self.Nombre = Nombre
        self.Precio = Precio
        self.Cantidad = Cantidad