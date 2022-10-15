from src.database import database
from src.users import schemas
from src.users.models import users
from src.users.services import Hash


async def signUp(request: schemas.UserSignUp):
    """
    Method for user to sign up

    :param request: UserSignUp schema, post body
    :return: created user

    """
    query = users.insert().values(
        first_name=request.first_name,
        last_name=request.last_name,
        email=request.email,
        password=Hash.bcrypt(request.password),
    )

    user_id = await database.execute(query)
    return {**request.dict(), "id": user_id}


async def updateUser(id: int, request: schemas.UserUpdate):
    """
    Method for updating the existing user

    :param id: id of user
    :param request: UserUpdate schema, update body
    :return: updated user

    """
    query = users.update().where(users.c.id == id).values(
        first_name=request.first_name,
        last_name=request.last_name,
        email=request.email,)

    await database.execute(query)
    return {**request.dict(), "id": id}


async def deleteUser(id: int):
    """
    Method for deleting the existing user
    :param id: user id
    :return: success status

    """
    query = users.delete().where(users.c.id == id)
    await database.execute(query)
    return {"status": "User with id: {} deleted successfully!".format(id)}


async def usersList(skip: int = 0, take: int = 100):
    """
    Method for listing all users

    :param skip: how many users to be skipped
    :param take: how many users to be returned
    :return: list of users

    """
    return await database.fetch_all(
        users.select().offset(skip).limit(take))


async def get_user_by_email(email: str):
    """
    Method for getting user by his email

    :param email: email of user
    :return: user with requested email

    """
    return await database.fetch_one(
        users.select().where(users.c.email == email)
    )


async def get_user_by_id(id: str):
    """
    Method for getting user by his id

    :param id: user id
    :return: user with requested id

    """
    return await database.fetch_one(
        users.select().where(users.c.id == id)
    )
