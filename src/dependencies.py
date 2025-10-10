import os

from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

from .users.schemas import UserInDB

load_dotenv()


SECRET_KEY = os.getenv('SECRET_KEY') or "your-secret-key" # It's good practice to provide a default for SECRET_KEY too
ALGORITHM = os.getenv('ALGORITHM') or 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES') or 30)


type FakeDB = dict[str, UserInDB] 


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str 


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


def get_user(db: FakeDB, username: str) -> UserInDB | None:
    return db.get(username)

fake_users_db: dict[str, UserInDB] = {
    "johndoe": UserInDB(
        username="johndoe",
        full_name="John Doe",
        email="johndoe@example.com",
        hashed_password="$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        disabled=False,
    ),
    "alice": UserInDB(
        username="alice",
        full_name="Alice Wonderson",
        email="alice@example.com",
        hashed_password="fakehashedsecret2",
        disabled=True,
    ),
}
