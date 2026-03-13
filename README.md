# Project Management API

API REST para la gestión de proyectos y tareas.

Este proyecto fue desarrollado como parte de mi portfolio de backend para demostrar conocimientos de arquitectura backend moderna utilizando Python y FastAPI.

---

# Stack Tecnológico

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy (ORM)
* Alembic (migraciones de base de datos)
* Pydantic (validación de datos)
* Passlib + bcrypt (hash seguro de contraseñas)
* JWT (autenticación)

---

# Funcionalidades Implementadas

## Autenticación de Usuarios

### Registro de usuario

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

---

### Login de usuario

Endpoint:

POST /auth/login

Flujo del login:

email + password  
↓  
buscar usuario en la base de datos  
↓  
verificar contraseña con bcrypt  
↓  
generar JWT  
↓  
devolver access_token  

Respuesta esperada:

```json
{
  "access_token": "eyJhbGc...",
  "token_type": "bearer"
}
```

---

### Obtener usuario autenticado

Endpoint:

GET /users/me

Este endpoint requiere un **JWT válido**.

El token se envía en el header:

Authorization: Bearer \<token>

Permite identificar al usuario autenticado.

Ejemplo de respuesta:

```json
{
  "id": 1,
  "email": "usuario@example.com",
  "created_at": "..."
}
```

---

# Gestión de Proyectos

Cada usuario puede crear y gestionar sus propios proyectos.

Endpoints disponibles:

POST /projects  
GET /projects  
GET /projects/{id}  
PUT /projects/{id}  
DELETE /projects/{id}

Características:

* Los proyectos están asociados al usuario autenticado
* Un usuario solo puede acceder a sus propios proyectos
* Protección mediante JWT

Ejemplo de creación de proyecto:

```json
{
  "name": "API Portfolio",
  "description": "Proyecto de práctica con FastAPI"
}
```

---

# Gestión de Tareas

Cada proyecto puede contener múltiples tareas.

Endpoints disponibles:

POST /tasks  
PUT /tasks/{id}  
DELETE /tasks/{id}

Cada tarea contiene:

* title
* description
* status
* project_id

Estados posibles de una tarea:

```
pending
in_progress
done
```

Ejemplo de creación de tarea:

```json
{
  "title": "Implementar autenticación",
  "description": "Agregar login con JWT",
  "status": "pending",
  "project_id": 1
}
```

---

# Arquitectura del Proyecto

El proyecto sigue una arquitectura modular separando responsabilidades.

```
app
 ├ api
 │   ├ dependencies
 │   │   └ auth.py
 │   │
 │   └ v1
 │       ├ auth.py
 │       ├ users.py
 │       ├ projects.py
 │       └ tasks.py
 │
 ├ core
 │   └ security.py
 │
 ├ db
 │   ├ database.py
 │   └ session.py
 │
 ├ models
 │   ├ user.py
 │   ├ project.py
 │   └ task.py
 │
 ├ schemas
 │   ├ user.py
 │   ├ project.py
 │   ├ task.py
 │   └ token.py
 │
 └ services
     ├ user_service.py
     ├ auth_service.py
     ├ project_service.py
     └ task_service.py
```

Descripción de cada capa:

**api**  
Define los endpoints HTTP.

**dependencies**  
Contiene dependencias reutilizables como autenticación JWT.

**schemas**  
Validación y serialización de datos con Pydantic.

**services**  
Contiene la lógica de negocio del sistema.

**models**  
Define los modelos de base de datos usando SQLAlchemy.

**db**  
Configura la conexión a PostgreSQL.

**core**  
Contiene utilidades del sistema como seguridad y manejo de tokens.

---

# Cómo ejecutar el proyecto

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

---

# Base de Datos

El proyecto utiliza **PostgreSQL** como base de datos.

Las migraciones se gestionan con **Alembic**, lo que permite versionar cambios en el esquema de la base de datos.

---

# Roadmap del Proyecto

Próximas funcionalidades planificadas:

* Relación bidireccional entre entidades en SQLAlchemy
* Endpoint `GET /projects/{id}/tasks`
* Filtros y paginación
* Dockerización del backend
* Tests automáticos con pytest
* CI/CD
