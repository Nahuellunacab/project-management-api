from sqlalchemy.orm import Session

from app.models.user import User
from app.core.security import verify_password, create_access_token


# Funcion para buscar un usuario por email y verificar su contraseña
def authenticate_user(db: Session, email: str, password: str):

    user = db.query(User).filter(User.email == email).first()

    if not user:
        return None

    if not verify_password(password, user.password_hash):
        return None

    return user


# Funcion para iniciar sesión y generar un token de acceso
def login_user(db: Session, email: str, password: str):

    user = authenticate_user(db, email, password)

    if not user:
        return None

    access_token = create_access_token(
        data={"sub": user.email}
    )

    return access_token