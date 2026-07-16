# Architecture Decision Records — Variedades

> Proyecto: Variedades La Divina Providencia
> Inicio: 2026-07-16

---

## ADR-001: Convención de commits

- **Fecha:** 2026-07-16
- **Tipo:** Convención
- **Ciclo:** Cycle 0
- **Contexto:** Necesitamos un formato consistente para los mensajes de commit
- **Decisión:** Formato `SP0X-T.N: verbo + descripción` (ej: `SP01-T1: crear modelo Categoria con nombre`)
- **Consecuencias:** Trazabilidad entre commits y tareas del backlog
- **Estado:** Vigente

## ADR-002: Service Layer

- **Fecha:** 2026-07-16
- **Tipo:** Arquitectura
- **Ciclo:** Cycle 0
- **Contexto:** Separar lógica de negocio de las vistas
- **Decisión:** Patrón View → Service → Model. Las vistas llaman a servicios, los servicios orquestan modelos
- **Consecuencias:** +mantenibilidad, +testeabilidad, -simplicidad inicial
- **Estado:** Vigente

## ADR-003: Estructura de apps

- **Fecha:** 2026-07-16
- **Tipo:** Convención
- **Ciclo:** Cycle 0
- **Contexto:** Definir cómo organizar las apps de Django
- **Decisión:** Una app por módulo de negocio (accounts, core, sales, purchases), naming snake_case singular
- **Consecuencias:** Claro mapeo entre MER y apps, fácil de extender
- **Estado:** Vigente

## ADR-004: Autenticación con Custom User model

- **Fecha:** 2026-07-16
- **Tipo:** Técnica
- **Ciclo:** Cycle 0
- **Contexto:** El sistema necesita usuarios con roles (admin, vendedor)
- **Decisión:** Custom User model heredando de AbstractUser, email como identificador secundario
- **Consecuencias:** +flexibilidad para agregar campos, migración inicial requerida
- **Estado:** Vigente
