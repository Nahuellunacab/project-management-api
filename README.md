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
 │       └ users.py
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
 │   ├ user.py
 │   └ token.py
 │
 └ services
     ├ user_service.py
     └ auth_service.py
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

* CRUD de proyectos
* CRUD de tareas
* Relación usuario → proyectos
* Relación proyectos → tareas
* Autorización por usuario
* Dockerización del backend
* Tests automáticos