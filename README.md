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
4. Build the Docker Image
```
docker build -t appimage .
```
5. Run the project
```
$ docker run -p 8000:8000 appimage
```
