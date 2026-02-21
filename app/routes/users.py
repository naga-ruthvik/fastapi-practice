from fastapi import APIRouter, HTTPException, Depends, status
from app.db.base import get_db
from app.schemas.schemas import UserCreate
from sqlalchemy.orm import Session
from app.db.models import User

router = APIRouter()


@router.get("/users")
async def list_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@router.post("/users")
async def create_user(body: UserCreate, db: Session = Depends(get_db)):
    try:
        user_exists = db.query(User).filter(User.name == body.name).count()
        if user_exists:
            return HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="user with name already exists",
            )

        user = User(name=body.name)
        db.add(user)
        db.commit()
        return HTTPException(
            status_code=status.HTTP_200_OK,
            detail=f"user {user.id} created successfully",
        )

    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"error while creating user:{e}",
        )
