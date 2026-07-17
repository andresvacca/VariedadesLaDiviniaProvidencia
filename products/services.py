from .models import Categoria, Articulo


def listar_categorias():
    return Categoria.objects.all()


def crear_categoria(nombre):
    return Categoria.objects.create(nombre=nombre)


def actualizar_categoria(categoria_id, nombre):
    categoria = Categoria.objects.get(id=categoria_id)
    categoria.nombre = nombre
    categoria.save()
    return categoria


def eliminar_categoria(categoria_id):
    Categoria.objects.filter(id=categoria_id).delete()


def listar_articulos():
    return Articulo.objects.select_related('categoria').all()


def crear_articulo(nombre, precio_venta, precio_compra, stock, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    return Articulo.objects.create(
        nombre=nombre,
        precio_venta=precio_venta,
        precio_compra=precio_compra,
        stock=stock,
        categoria=categoria,
    )


def actualizar_articulo(articulo_id, **datos):
    Articulo.objects.filter(id=articulo_id).update(**datos)
    return Articulo.objects.get(id=articulo_id)


def eliminar_articulo(articulo_id):
    Articulo.objects.filter(id=articulo_id).delete()
