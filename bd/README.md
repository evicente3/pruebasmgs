# Laboratorio 05: Base de Datos - Modelo de Gestión de Suscripciones V3

## Autores

| Autores                     | Rol                                   | Porcentaje |
|-----------------------------|---------------------------------------|------------|
| Eder Lucio Vicente Medina   | Implementación BD y Supabase          | 100%       |
| Marco Antonio Salas Zegarra | Elaboración de Informe                | 100%       |
| Kevin Peralta Llasa         | Elaboración del modelo lógico DER     | 100%       |
| Percy Molina Soncco         | Documentación y Pruebas               | 100%       |
|                             | **Total** | **100%** |

---

## Entregables

| Entregables | URL |
|-------------|-----|
| Repositorio | [https://github.com/evicente3/MGS.git](https://github.com/evicente3/MGS.git) |
| Informe     | [[https://github.com/evicente3/MGS/blob/main/informes/DAW_lab05_bd.pdf](https://github.com/evicente3/MGS/blob/main/informes/DAW_lab05_bd.pdf](https://github.com/evicente3/MGS/blob/main/informes/lab05_daw.pdf)) |
| Supabase    | [https://supabase.com/dashboard/project/zdjjpofxtnfbjagjhbia] |

---

## Descripción del Laboratorio

El objetivo de esta práctica es el diseño e implementación de una base de datos relacional para gestionar suscripciones digitales. El sistema permite centralizar estados, gestionar catálogos de servicios internacionales y controlar deudas por cuentas compartidas.

- **Modelo Lógico (DER):** Arquitectura normalizada para asegurar integridad.
- **Modelo Físico:** Implementación en PostgreSQL con estándares de auditoría.
- **Cloud Hosting:** Despliegue en Supabase con seguridad a nivel de fila (RLS).

---

## 1. Elaboración del modelo lógico DER

El modelo lógico se ha diseñado para normalizar la información y evitar la redundancia de datos. Se centra en la entidad `SUBSCRIPTIONS` como núcleo transaccional.

* **Relaciones Principales**: Los usuarios poseen suscripciones (`USERS` owns `SUBSCRIPTIONS`) y definen sus propias categorías de organización.
* **Catálogos Maestros**: Se utilizan tablas estáticas para monedas (`CURRENCIES`) y estados (`STATUS_TYPES`) para estandarizar la información a nivel global.
* **Gestión de Deudas**: Se utiliza una relación de compartición (`SUBSCRIPTION_SHARES`) que genera registros automáticos en la tabla de deudas (`DEBTS`).

---

## 2. Implementación del Modelo Físico PostgreSQL

En esta fase se tradujo el modelo conceptual lógico al motor de base de datos relacional PostgreSQL. Se establecieron las restricciones de integridad (Primary Keys, Foreign Keys, Constraints de tipo CHECK y DEFAULT) mediante scripts DDL (Data Definition Language).

---

## 3. Implementación en Supabase

Finalmente, se realizó el despliegue de la base de datos en Supabase, aprovechando sus capacidades de Backend-as-a-Service (BaaS). Se migró el esquema diseñado y se establecieron políticas de seguridad (RLS) para proteger los datos a nivel de usuario.

---
## Rúbrica de calificación
| ítem | Descripción | Puntaje |
| :--- | :--- | :---: |
| **DER** | Elaboración del modelo lógico DER. | 4 |
| **Modelo físico** | Implementación del modelo físico PostgreSQL. | 7 |
| **Supabase** | Implementación en Supabase. | 4 |
| **Informe** | El laboratorio tiene un README.md que detalla toda la práctica. | 3 |
| **Prueba[^2]** | Se tomaron en cuenta todas las consideraciones y recomendaciones, lo que evidencia un trabajo en equipo. | -0 |
|  | **Total** | **18** |
