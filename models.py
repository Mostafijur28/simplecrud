from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserFilmRole(Base):
    __tablename__ = 'user_film_roles'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    film_id = Column(Integer, ForeignKey('films.id'), primary_key=True)
    role = Column(String)


class UserCompanyRole(Base):
    __tablename__ = 'user_company_roles'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    company_id = Column(Integer, ForeignKey('companies.id'), primary_key=True)
    role = Column(String)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    minimum_fee = Column(Integer, default=0)

    # Relationship with films
    films = relationship("Film", secondary=UserFilmRole.__table__, back_populates="users")
    companies = relationship("Company", secondary=UserCompanyRole.__table__, back_populates="users")

class Film(Base):
    __tablename__ = 'films'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, unique=True)
    description = Column(String)
    budget = Column(Integer, default=1000)
    release_year = Column(Integer, default=2024)
    genres = Column(String)
    company_id = Column(Integer, ForeignKey('companies.id'))

    users = relationship("User", secondary=UserFilmRole.__table__, back_populates="films")
    company = relationship("Company", back_populates="films")


class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    contact_email_address = Column(String, unique=True)
    phone_number = Column(String, unique=True)

    users = relationship("User", secondary=UserCompanyRole.__table__, back_populates="companies")
    films = relationship("Film", back_populates="company")
