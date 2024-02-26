from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Company, Film

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

user_data = [
    {"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com", "minimum_fee": 100},
    {"first_name": "Jane", "last_name": "Smith", "email": "jane.smith@example.com", "minimum_fee": 150},
]

company_data = [
    {"name": "ABC Inc.", "contact_email_address": "info@abc.com", "phone_number": "123-456-7890"},
    {"name": "XYZ Corp.", "contact_email_address": "info@xyz.com", "phone_number": "987-654-3210"},
]

film_data = [
    {"title": "Movie 1", "description": "Description of Movie 1", "budget": 100000, "release_year": 2021, "genres": "Action"},
    {"title": "Movie 2", "description": "Description of Movie 2", "budget": 150000, "release_year": 2022, "genres": "Drama"},
]

def insert_initial_data():
    insert_data(User, user_data)
    insert_data(Company, company_data)
    insert_data(Film, film_data)

def insert_data(model, data):
    with SessionLocal() as session:
        for item in data:
            session.add(model(**item))
        session.commit()

def create_all_tables():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    insert_initial_data()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()