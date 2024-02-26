from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db_config import get_db
from schemas import UserRoleCompany
import models

router = APIRouter()

@router.post("/user-roles/companies/create-user-role", response_model=UserRoleCompany)
def create_user_role(role: UserRoleCompany, db: Session = Depends(get_db)):

    try:
        user_role_company = models.UserCompanyRole(**role.dict())
        db.add(user_role_company)
        db.commit()
        return user_role_company

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/user-roles/companies/read-user-role", response_model=UserRoleCompany)
def read_user_role(company_id: int, user_id: int, db: Session = Depends(get_db)):
    try:
        user_role_company = db.query(models.UserCompanyRole).filter_by(company_id=company_id, user_id=user_id).first()
        if user_role_company is None:
            raise HTTPException(status_code=404, detail="User role for the specified company and user not found")
        return user_role_company
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/user-roles/companies/update-user-role", response_model=UserRoleCompany)
def update_user_role_company(role: UserRoleCompany, db: Session = Depends(get_db)):
    try:
        user_role_company = db.query(models.UserCompanyRole).filter(
            models.UserCompanyRole.user_id == role.user_id,
            models.UserCompanyRole.company_id == role.company_id
        ).first()
        if user_role_company is None:
            raise HTTPException(status_code=404, detail="Role not found")

        for attr, value in role.dict().items():
            setattr(user_role_company, attr, value)

        db.commit()
        db.refresh(user_role_company)

        return user_role_company

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to update user role: {str(e)}")