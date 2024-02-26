from pydantic import BaseModel
from typing import List, Literal

class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    minimum_fee: int

class Film(BaseModel):
    title: str
    description: str
    budget: int
    release_year: int
    genres: List[str]


class Company(BaseModel):
    name: str
    contact_email_address: str
    phone_number: str


class UserRoleFilm(BaseModel):
    user_id: int
    film_id: int
    role: Literal['writer', 'director', 'producer']

class UserRoleCompany(BaseModel):
    user_id: int
    company_id: int
    role: Literal['writer', 'director', 'producer']

