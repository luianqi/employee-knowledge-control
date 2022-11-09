from typing import List

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.database import database
from src.users import schemas, crud
from src.users.dependencies import CurrentUsers
from src.users.models import users
from src.users.schemas import UserBase, UpdatePassword
from src.users.services import RoleChecker, allowed_users
from src.users.utils import Hash, Token

router = APIRouter(
    prefix="/user",
    tags=["users"]
)


@router.post("/signup/", response_model=schemas.UserResponse)
async def sign_up(request: schemas.UserSignUp):
    db_user = await crud.get_user_by_email(email=request.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email in use")
    return await crud.signUp(request=request)


@router.post("/signin/")
async def sign_in(request: OAuth2PasswordRequestForm = Depends()):
    db_user = await crud.get_user_by_email(email=request.username)
    if not db_user:
        raise HTTPException(status_code=404,
                            detail=f"Invalid Credentials")
    if not Hash.verify(db_user.password, request.password):
        raise HTTPException(status_code=404,
                            detail=f"Incorrect password")

    access_token = Token.create_access_token(data={"sub": db_user.email})

    return {"access_token": access_token,
            "token_type": "bearer"}


@router.get("/all-users/", response_model=List[schemas.UserInDBBase])
async def users_list(skip: int = 0, take: int = 100):
    return await crud.usersList(skip=skip, take=take)


@router.patch("/{user_id}/", response_model=schemas.UserResponse)
async def update_user(id: int, request: schemas.UserUpdate):
    db_user = await crud.get_user_by_id(id=id)
    if not db_user:
        raise HTTPException(status_code=404,
                            detail=f"User with the id {id} is not available")
    return await crud.updateUser(id=id, request=request)


@router.delete("{user_id}/")
async def delete_user(id: int):
    db_user = await crud.get_user_by_id(id=id)
    if not db_user:
        raise HTTPException(status_code=404,
                            detail=f"User with the id {id} is not available")
    return await crud.deleteUser(id=id)


@router.post("/some-resource/", dependencies=[Depends(allowed_users)],
)
async def add_resource(resource: schemas.UserSignUp):
    # Some validation like resource does not already exist
    # Create the resource
    pass



# @router.patch("{change_password}/", dependencies=[Depends(allowed_users)])
# async def change_password(id: int,
#                           data: UpdatePassword,
#                           current_user: UserBase = Depends(CurrentUsers.get_current_user)):
#
#     if not current_user:
#         raise HTTPException(status_code=404, detail=f"User not found.")
#     if current_user.id != id:
#         raise HTTPException(
#             status_code=403, detail=f"only user can change their own password."
#         )
#     password_changed = crud.UpdatePassword(data)
#     if password_changed:
#         return {"message": "password updated"}
#     raise HTTPException(status_code=400, detail="invalid current password")










