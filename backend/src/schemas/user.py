from pydantic import BaseModel, EmailStr, constr


class UserCreate(BaseModel):
    email: EmailStr
    password: constr(min_length=8)


class UserResponse(BaseModel):
    email: EmailStr

    class Config:
        orm_mode = True
