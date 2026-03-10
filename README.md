# Project Management API

API REST para la gestión de proyectos y tareas.

Este proyecto fue desarrollado como parte de mi portfolio de backend para demostrar conocimientos de arquitectura backend moderna utilizando Python y FastAPI.

## Stack Tecnológico

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy (ORM)
* Alembic (migraciones de base de datos)
* Pydantic (validación de datos)
* Passlib + bcrypt (hash seguro de contraseñas)

## Funcionalidades Implementadas

### Registro de Usuario

Endpoint:

POST /auth/register

Permite crear un nuevo usuario con:

* validación de email
* hash seguro de contraseña
* protección contra emails duplicados

Ejemplo de request:

```json
{
  "email": "usuario@example.com",
  "password": "123456"
}
```

## Arquitectura del Proyecto

El proyecto sigue una estructura modular separando responsabilidades:

```
app
 ├ api
 │   └ v1
 │       └ auth.py
 │
 ├ core
 │   └ security.py
 │
 ├ db
 │   ├ database.py
 │   └ session.py
 │
 ├ models
 │   └ user.py
 │
 ├ schemas
 │   └ user.py
 │
 └ services
     └ user_service.py
```

Descripción de cada capa:

* **api** → define los endpoints HTTP
* **schemas** → validación de datos con Pydantic
* **services** → lógica de negocio
* **models** → modelos de base de datos (SQLAlchemy)
* **db** → configuración de conexión a base de datos
* **core** → utilidades del sistema (seguridad, configuración, etc.)

## Cómo ejecutar el proyecto

Clonar el repositorio:

```bash
git clone https://github.com/Nahuellunacab/project-management-api
```

Entrar al proyecto:

```bash
cd project-management-api
```

Crear entorno virtual:

```bash
python -m venv venv
```

Activar entorno virtual:

Windows:

```bash
venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar la API:

```bash
uvicorn app.main:app --reload
```

Abrir la documentación automática:

```
http://127.0.0.1:8000/docs
```

## Base de Datos

El proyecto utiliza **PostgreSQL** como base de datos.

Las migraciones se gestionan con **Alembic**, lo que permite versionar cambios en el esquema de la base de datos.

## Roadmap del Proyecto

Próximas funcionalidades planificadas:

* Login de usuarios
* Autenticación con JWT
* Middleware de autenticación
* CRUD de proyectos
* CRUD de tareas
* Autorización por usuario
* Dockerización del backend
