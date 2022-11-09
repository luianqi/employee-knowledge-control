from typing import List

from fastapi import Depends, HTTPException

from src.users.dependencies import CurrentUsers
from src.users.schemas import UserBase


class RoleChecker:
    def __init__(self, allowed_roles: List):
        self.allowed_roles = allowed_roles

    def __call__(self, user: UserBase = Depends(CurrentUsers.get_current_user)):
        if user.role not in self.allowed_roles:
            raise HTTPException(status_code=403, detail="Operation not permitted")


allowed_users = RoleChecker(["user", "admin", "owner"])
