# Pitch — Variedades

> Versión: 0.01 (prototipo)
> Fecha: 2026-07-16
> Estado: Pendiente de confirmación

## Problema

El remate carece de un registro unificado que consolide los ingresos por venta, los egresos por compras y los gastos operativos del día, lo que impide conocer el flujo de caja real. No es posible generar reportes diarios que reflejen la utilidad, las pérdidas o el desempeño financiero del negocio.

## Solución propuesta

Sistema web para registrar las diferentes categorías de productos, las ventas del día, las compras y los gastos operativos. En una primera fase (prototipo v0.01) se enfoca en el registro básico de ventas y gastos. En fases posteriores se agregará inventario completo con stock y código de barras para tener un flujo de caja actualizado y completo.

## Modelo Entidad-Relación

Ver `docs/modelo_entidad_relacion.md`

## Backlog inicial

| Prioridad | Tipo | Descripción |
|-----------|------|-------------|
| Alta | FEATURE | CRUD de Categorías |
| Alta | FEATURE | CRUD de Artículos |
| Alta | FEATURE | Registro de Ventas (caja diaria) |
| Alta | FEATURE | Registro de Gastos del día |
| Media | FEATURE | Registro de Compras + DetalleCompra |
| Media | FEATURE | CRUD de Proveedores |
| Media | FEATURE | CRUD de Usuarios + Roles |
| Media | FEATURE | Dashboard de flujo de caja del día |
| Baja | FEATURE | Facturación (descargar/imprimir) |
| Baja | FEATURE | Reportes (utilidad, pérdidas, período) |
| Baja | TECH_DEBT | Stock automático al vender/comprar |
| Baja | FEATURE | Lector de códigos de barras |

## Roadmap por ciclos

| Ciclo | Qué entra | Depende de |
|-------|-----------|------------|
| Ciclo 1 | CRUD Categorías + CRUD Artículos | — |
| Ciclo 2 | Registro de Ventas + DetalleVenta | Ciclo 1 |
| Ciclo 3 | Registro de Gastos + Dashboard flujo de caja | Ciclo 2 |
| Ciclo 4 | CRUD Proveedores + Registro Compras | Ciclo 1 |
| Ciclo 5 | CRUD Usuarios + Roles + Login | — |
| Ciclo 6+ | Facturación, Reportes, Stock automático, Código barras | Ciclos anteriores |

## Riesgos conocidos

- Dependencia de confirmación externa para definir alcance final
- Posible necesidad de código de barras antes de lo planeado

## Criterio de Aceptación

Prototipo v0.01 completo cuando: CRUD Categorías + Artículos funcionando + Registro de Ventas con detalle + Registro de Gastos + Dashboard de flujo de caja del día.
