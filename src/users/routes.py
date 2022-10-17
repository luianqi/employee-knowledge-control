from typing import List

from fastapi import APIRouter, HTTPException

from src.users import schemas, crud
from src.users.models import users
from src.users.services import Hash

router = APIRouter(
    prefix="/user",
    tags=["users"]
)


@router.post("/signup/", response_model=schemas.UserResponse)
async def signUp(request: schemas.UserSignUp):
    db_user = await crud.get_user_by_email(email=request.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email in use")
    return await crud.signUp(request=request)


@router.get("/all-users/", response_model=List[schemas.UserBase])
async def usersList(skip: int = 0, take: int = 100):
    return await crud.usersList(skip=skip, take=take)


@router.patch("/{user_id}/", response_model=schemas.UserResponse)
async def updateUser(id: int, request: schemas.UserUpdate):
    db_user = await crud.get_user_by_id(id=id)
    if not db_user:
        raise HTTPException(status_code=404,
                            detail=f"User with the id {id} is not available")
    return await crud.updateUser(id=id, request=request)


@router.delete("{user_id}/")
async def deleteUser(id: int):
    db_user = await crud.get_user_by_id(id=id)
    if not db_user:
        raise HTTPException(status_code=404,
                            detail=f"User with the id {id} is not available")
    return await crud.deleteUser(id=id)







# @router.post("/signin/")
# async def signIn(request: schemas.UserSignIn):
#     if not Hash.verify():
#         raise HTTPException(status_code=404, detail=f"Incorrect password")
#
#     return {"status": "Successfully signed in!"}



