from flask import Blueprint,render_template,request,redirect
from models.products import Producto
from config.db import db

productos = Blueprint('products', __name__)


@productos.route('/')

def listarProductos():

    p = Producto.query.all()

    return render_template('products/index.html', lista = p)

@productos.route('/new',methods=['POST'])
def crearProducto():

    Nombre = request.form['Nombre']
    Precio = request.form['Precio']
    Cantidad = request.form['Cantidad']
    print(Nombre,Precio,Cantidad)
    new_Producto = Producto(Nombre, Precio, Cantidad)
    db.session.add(new_Producto)
    db.session.commit()
    return redirect('/')


@productos.route('/edit/<id>',methods=['POST','GET'])
def editarProducto(id):
    if request.method == 'POST':
        productos = Producto.query.get(id)
        
        productos.Nombre = request.form['Nombre']
        productos.Precio = request.form['Precio']
        productos.Cantidad = request.form['Cantidad']
        db.session.commit()
        return redirect('/')
    else:
        productos = Producto.query.get(id)
        return render_template('products/update.html',producto = productos)

@productos.route('/delete/<id>')
def eliminarProducto(id):
    producto = Producto.query.get(id)
    db.session.delete(producto)
    db.session.commit()
    return redirect('/')