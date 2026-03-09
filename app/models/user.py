from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.db.database import Base


# Modelo de usuario
# id: Identificador único del usuario
# email: Correo electrónico del usuario (único)
# password_hash: Hash de la contraseña del usuario
# created_at: Fecha de creación del usuario
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)