#  MGS V3 - Sistema de Gestión de Suscripciones


##  Visión General
**MGS V3** (Management of Subscriptions) es una solución integral diseñada para centralizar, controlar y optimizar el ciclo de vida de suscripciones digitales. El sistema resuelve problemas críticos de gestión financiera, como la fragmentación de pagos en cuentas compartidas, el seguimiento de deudas pendientes y la estandarización de catálogos de servicios internacionales.

Desarrollado bajo estándares académicos de ingeniería, el proyecto implementa una arquitectura de base de datos robusta con auditoría universal y seguridad a nivel de registros (RLS).

---

##  Equipo de Desarrollo 

| Autor | Rol Principal | GitHub |
| :--- | :--- | :--- |
| **Eder Lucio Vicente Medina** | Desarrollador fullstack (devops) | [@evicente3](https://github.com/evicente3) |
| **Marco Antonio Salas Zegarra** | Desarrollador backend (programador) | [@msalasz](https://github.com/gkeras) |
| **Kevin Peralta Llasa** | Desarrollador frontend (programador y diseñador) | [@kperaltal](https://github.com/kevvperalta) |
| **Percy Molina Soncco** |Administrador de SGBD (Base de datos) | [@pmolinas](https://github.com/pmolinas) |

---

##  Stack Tecnológico
* **Motor de BD:** PostgreSQL 15+
* **Plataforma Cloud:** Supabase (Backend as a Service)
* **Modelado:** Mermaid.js & Database Visualizer
* **Control de Versiones:** Git & GitHub (GitFlow Workflow)

---

##  Características Principales
- **Normalización de Nivel Superior:** Diseño relacional optimizado para evitar redundancia en servicios y monedas (ISO 4217).
- **Seguridad Garantizada:** Implementación de **Row Level Security (RLS)** que asegura que la información financiera sea privada y accesible solo por el propietario.
- **Auditoría Universal:** Sistema de rastreo nativo en cada tabla (`created`, `modified`, `status`, etc.) para cumplimiento de estándares corporativos.
- **Gestión de Deudas Inteligente:** Lógica integrada para la partición de costos entre múltiples usuarios y seguimiento de saldos pendientes.

---

##  Estructura del Proyecto
El repositorio está organizado siguiendo una arquitectura modular para facilitar el trabajo colaborativo:

```bash
MGS/
├── backend/            # Lógica de servidor y APIs (Próximamente)
├── bd/                 # Implementación física, scripts SQL y DER
│   └── screenshots/    # Evidencias de implementación en Supabase
├── frontend/           # Interfaz de usuario (Próximamente)
├── informes/           # Entregables académicos en formato PDF
└── README.md           # Presentación general del proyecto
