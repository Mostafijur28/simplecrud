from fastapi import FastAPI
from db_config import create_all_tables
from user_role_film import router as film_router
from user_role_company import router as company_router

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    create_all_tables()

app.include_router(film_router, prefix="/films", tags=["films"])
app.include_router(company_router, prefix="/companies", tags=["companies"])
