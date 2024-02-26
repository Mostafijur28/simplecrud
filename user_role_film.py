from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db_config import get_db
from schemas import UserRoleFilm
import models

router = APIRouter()

@router.post("/user-roles/films/create-user-role", response_model=UserRoleFilm)
def create_user_role_film(role: UserRoleFilm, db: Session = Depends(get_db)):
    try:
        user_role_film = models.UserFilmRole(**role.dict())
        db.add(user_role_film)
        db.commit()
        return user_role_film
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/user-roles/films/read-user-role", response_model=UserRoleFilm)
def read_user_role_film(user_id: int, film_id: int, db: Session = Depends(get_db)):
    try:
        user_role_film = db.query(models.UserFilmRole).filter_by(user_id=user_id, film_id=film_id).first()
        if user_role_film is None:
            raise HTTPException(status_code=404, detail="User role for the specified film and user not found")
        return user_role_film
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/user-roles/films/update-user-role", response_model=UserRoleFilm)
def update_user_role_film(role: UserRoleFilm, db: Session = Depends(get_db)):
    try:
        user_role_film = db.query(models.UserFilmRole).filter(
            models.UserFilmRole.user_id == role.user_id,
            models.UserFilmRole.film_id == role.film_id
        ).first()

        if user_role_film is None:
            raise HTTPException(status_code=404, detail="Role not found")

        for attr, value in role.dict().items():
            setattr(user_role_film, attr, value)

        db.commit()
        db.refresh(user_role_film)

        return user_role_film

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to update user role: {str(e)}")
