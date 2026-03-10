from pydantic import BaseModel

# Define lo que devuelve el endpoint al login.
class Token(BaseModel):
    access_token: str
    token_type: str


#  Define lo que se recibe del token, en este caso el email del usuario.
class TokenData(BaseModel):
    email: str | None = None
