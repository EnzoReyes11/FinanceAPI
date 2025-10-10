from sqlalchemy.orm import Session

from ..auth.routes import get_password_hash
from . import models, schemas


def get_user_by_username(db: Session, username: str) -> models.User | None:
    """
    Retrieves a user from the database by their username.
    """
    return db.query(models.User).filter(models.User.username == username).first()


def get_user_by_email(db: Session, email: str) -> models.User | None:
    """
    Retrieves a user from the database by their email.
    """
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    """
    Creates a new user in the database.
    """
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, email=user.email, full_name=user.full_name, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user