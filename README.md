# Employee Knowledge Control App

# Built With

> ### `Fast API` - The framework used
> ### `PostgreSQL` - The database used

---
# Getting started
---
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
# Prerequisites
This is a project written using Python and Fast API

1. Clone the repository
```
https://github.com/luianqi/employee-knowledge-control.git
```
2. Create the virtual enviroment
 ```
python3 -m venv venv
source venv/bin/activate
```
3. Install poetry.lock
```
Poetry install 
```

4. Create a new PostgreSQL database

 In your terminal:
```
psql postgres
CREATE DATABASE databasename
\c databasename
```
5. Run migration 
```
alembic revision --autogenerate -m "New Migration"
alembic upgrade head
```
6. Build the Docker Image
```
docker build -t appimage .
```
7. Run the project
```
$ docker сompose-up
```
