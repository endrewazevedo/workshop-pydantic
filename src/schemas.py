from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Optional
from pydantic.alias_generators import to_camel


class BaseSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        from_attributes=True,
    )


class User(BaseSchema):
    full_name: str
    email: str
    password: str

    @field_validator('full_name')
    def validate_name(cls, full_name):
        if not full_name.replace(" ", "").isalpha():
            raise ValueError('O nome de usuário deve conter apenas letras')
        if len(full_name) < 3:
            raise ValueError('O nome de usuário deve ter no mínimo 3 caracteres')
        if full_name[0].islower():
            raise ValueError('O nome de usuário deve começar com uma letra maiúscula')
        if full_name.strip() != full_name:
            raise ValueError('O nome de usuário não deve conter espaços em branco no início ou no fim')
        if len(full_name.split(" ")) < 2:
            raise ValueError('O nome de usuário deve conter pelo menos um sobrenome')

        return full_name

    @field_validator('email')
    def validate_email(cls, email):
        if email:
            if not email.count('@') == 1:
                raise ValueError('O email deve conter apenas um "@"')
            if not email.count('.') >= 1:
                raise ValueError('O email deve conter pelo menos um "."')
            if not email.endswith('.com'):
                raise ValueError('O email deve terminar com ".com"')
        return email

    @field_validator('password')
    def validate_password(cls, password):
        if len(password) < 8:
            raise ValueError('A senha deve ter no mínimo 8 caracteres')
        if not any(char.isdigit() for char in password):
            raise ValueError('A senha deve conter pelo menos um número')
        if not any(char.isupper() for char in password):
            raise ValueError('A senha deve conter pelo menos uma letra maiúscula')
        if not any(char.islower() for char in password):
            raise ValueError('A senha deve conter pelo menos uma letra minúscula')
                             
        return password


class UserResponse(BaseSchema):
    full_name: str
    email: str
    created_at: datetime = Field(default_factory=datetime.now)


class AllUsersResponse(BaseSchema):
    total: int
    users: list[UserResponse]