from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# class User(BaseModel):
#     name : str 
#     age  : int 
#     email: str

# @app.post ("/create_user")
# def create_user(user : User) :
#     return {
#         "message" : "User Created",
#         "data"    :  user 
#     }

# Add email field to User model and create-user endpoint

class Address (BaseModel):
    city : str
    pincode : int 

class User(BaseModel):
    name : str
    age  : int 
    address : Address # way to handle nested data

@app.post("/create_user")
def create_user(user : User) :
    return user
