# Modelo Entidad-Relación — Variedades

> Versión: 0.01 (prototipo)

```sql
Project VentasCore {
  database_type: "PostgreSQL"
  note: "MiniMarket"
}

Table ROL {
  id int [pk, increment]
  nombre varchar(50)
}

Table USUARIO {
  id int [pk, increment]
  nombre varchar(100)
  email varchar(100)
  password varchar(255)
  rol_id int [ref: > ROL.id]
}

Table PROVEEDOR {
  id int [pk, increment]
  nombre varchar(150)
  telefono varchar(20)
}

Table CATEGORIA {
  id int [pk, increment]
  nombre varchar(100)
}

Table ARTICULOS {
  id int [pk, increment]
  nombre varchar(150)
  precio_venta decimal(10,2)
  precio_compra decimal(10,2)
  stock int
  categoria_id int [ref: > CATEGORIA.id]
}

Table COMPRAS {
  id int [pk, increment]
  fecha date
  total decimal(10,2)
  proveedor_id int [ref: > PROVEEDOR.id]
}

Table DETALLECOMPRA {
  id int [pk, increment]
  compra_id int [ref: > COMPRAS.id]
  articulo_id int [ref: > ARTICULOS.id]
  cantidad int
  precio_unitario decimal(10,2)
  subtotal decimal(10,2)
}

Table VENTAS {
  id int [pk, increment]
  fecha date
  total decimal(10,2)
  usuario_id int [ref: > USUARIO.id]
}

Table DETALLEVENTA {
  id int [pk, increment]
  venta_id int [ref: > VENTAS.id]
  articulo_id int [ref: > ARTICULOS.id]
  cantidad int
  precio_unitario decimal(10,2)
  subtotal decimal(10,2)
}

Table FACTURA {
  id int [pk, increment]
  numero varchar(50)
  fecha date
  total decimal(10,2)
  tipo char(1)
  venta_id int [ref: - VENTAS.id]
  compra_id int [ref: - COMPRAS.id]
}

Table GASTOS {
  id int [pk, increment]
  descripcion text
  monto decimal(10,2)
  fecha date
  usuario_id int [ref: > USUARIO.id]
}
```
