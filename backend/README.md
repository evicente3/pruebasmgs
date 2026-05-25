# Laboratorio 06: Backend - Gestión de Suscripciones con Django

## Autores

| Autores                     | Rol                                   | Porcentaje |
|-----------------------------|---------------------------------------|------------|
| Marco Antonio Salas Zegarra | Implementación Backend y Django       | 100%       |
| Eder Lucio Vicente Medina   | Elaboración de Informe                | 100%       |
| Kevin Peralta Llasa         | Diseño DER y Modelado                 | 100%       |
| Percy Molina Soncco         | Documentación y Pruebas               | 100%       |
|                             | **Total**                             | **100%**   |

---

## Entregables

| Entregables | URL |
|-------------|-----|
| Repositorio | https://github.com/evicente3/MGS/tree/main/backend |
| Informe     | https://github.com/evicente3/MGS/blob/main/informes/lab06_daw.pdf |
| Supabase    | https://supabase.com/dashboard/project/zdjjpofxtnfbjagjhbia/database/schemas |
| Video       |  |

---

# Descripción del Laboratorio

El objetivo de esta práctica fue desarrollar y configurar el backend del sistema utilizando Django. Se implementaron modelos independientes, restricciones personalizadas y operaciones CRUD automáticas mediante Django Admin.

El proyecto fue estructurado siguiendo la arquitectura estándar de Django y utilizando PostgreSQL en Supabase como sistema gestor de base de datos.

- **Framework Backend:** Django  
- **Base de Datos:** PostgreSQL  
- **Cloud Hosting:** Supabase  
- **Control de Versiones:** Git y GitHub  

---

# 1. Objetivos del Laboratorio

- Crear un proyecto Django y la aplicación `sissub`.
- Implementar modelos desacoplados en archivos independientes.
- Aplicar restricciones y validaciones desde los modelos.
- Redefinir métodos `save()` y `__str__()`.
- Generar operaciones CRUD automáticas con Django Admin.

---

# 2. Desarrollo Técnico

## Estructura del Proyecto y Modelos Independientes

El backend fue organizado utilizando una estructura modular dentro de la aplicación `sissub`.

```bash
backend/
│── mgs/
│── sissub/
│   │── models/
│   │   │── category.py
│   │   │── currency.py
│   │   │── service.py
│   │   │── subscription.py
│   │   │── subscription_user.py
│   │   │── user_profile.py
│── admin.py
│── manage.py
│── requirements.txt
```

---

# 3. Creación de Modelos y Restricciones

## Modelo Service (`service.py`)

Se implementaron validaciones para garantizar que el nombre del servicio tenga al menos 3 caracteres. Además, el método `save()` elimina espacios innecesarios antes de guardar los datos.

Características:

- Validación de nombre.
- Estado activo por defecto.
- Limpieza automática de datos.
- Personalización de visualización mediante `__str__()`.

---

## Modelo Subscription (`subscription.py`)

Este modelo administra las suscripciones y relaciones entre usuarios, servicios, categorías y monedas.

Restricciones implementadas:

- Montos mayores a cero.
- Fechas de facturación válidas.
- Uso de claves foráneas.
- Formateo automático del ciclo de facturación.

---

## Configuración del Django Admin (`admin.py`)

Se registraron todos los modelos en Django Admin para generar interfaces CRUD automáticas.

Funciones implementadas:

- Listado personalizado de columnas.
- Filtros de búsqueda.
- Barras de búsqueda.
- Organización de registros.

---

# 4. Diagrama Entidad-Relación (DER)

El modelo entidad-relación fue generado utilizando `django-extensions` y `Graphviz`.

```bash
python manage.py graph_models sissub -o diagrama_der.png
```

El DER permitió visualizar las relaciones entre servicios, usuarios, categorías y suscripciones.

---

# 5. Operaciones CRUD

Django Admin permitió realizar operaciones CRUD automáticamente sobre los modelos del sistema.

| Operación | Descripción |
|------------|-------------|
| Create | Registro de nuevos servicios y suscripciones |
| Read | Visualización de registros |
| Update | Modificación de información |
| Delete | Eliminación de registros |

---

# 6. Proceso de Implementación

## Preparación del Entorno

```bash
source venv/bin/activate
pip install -r requirements.txt
```

## Migraciones

```bash
python manage.py makemigrations sissub
python manage.py migrate
```

## Creación del Administrador

```bash
python manage.py createsuperuser
python manage.py runserver
```


---


# 7. Conclusiones

- La separación de modelos mejora la organización y escalabilidad del proyecto.
- Las validaciones garantizan integridad de datos antes de almacenarlos.
- Django Admin facilita la generación automática de operaciones CRUD.
- GitHub permitió un trabajo colaborativo ordenado.

---

# Rúbrica de Calificación

| Ítem | Descripción | Puntaje |
| :--- | :--- | :---: |
| **Entorno Virtual** | Uso correcto del entorno virtual. | 2 |
| **Django Admin** | Creación y configuración del administrador. | 3 |
| **Restricciones** | Implementación de validaciones en modelos. | 3 |
| **Modelo DER** | Generación del modelo entidad-relación. | 3 |
| **BD** | Base de datos con registros funcionales. | 3 |
| **Modelos** | Configuración correcta de modelos Django. | 3 |
| **Informe** | README.md detallando la práctica. | 3 |
|  | **Total** | **18** |
