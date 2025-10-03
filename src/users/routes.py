from typing import Annotated, Any

import jwt
from fastapi import APIRouter, Depends, HTTPException, status
from jwt.exceptions import InvalidTokenError

from ..dependencies import (
    ALGORITHM,
    SECRET_KEY,
    TokenData,
    User,
    fake_users_db,
    get_user,
    oauth2_scheme,
)

router = APIRouter(
    prefix="/user",   
    tags=["User"]    
)

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload: dict[str, Any] = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@router.get("/", response_model=list[User])
async def read_users_all(current_user: Annotated[User, Depends(get_current_user)]):
    users = list(fake_users_db.values())

    return users


@router.post("/")
async def new_user(user: User):
    return user


@router.get("/me", response_model=User)
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user
    

@router.get("/{user_id}")
async def read_user(user_id: int, current_user: Annotated[User, Depends(get_current_user)]):
    return {"message": "Some user" }

