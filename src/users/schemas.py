from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    username: str = Field(title = "Username for the user", min_length=4)
    email: EmailStr = Field(title = "Email for the user", min_length=4)
    full_name: str | None = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    disabled: bool | None = None

    class Config:
        orm_mode = True

class UserInDB(UserBase):
    hashed_password: str
    disabled: bool | None = None


