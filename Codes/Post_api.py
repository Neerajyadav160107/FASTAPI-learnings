# POST endpoint for user creation using Pydantic


from fastapi import FastAPI
from pydantic import BaseModel 

app = FastAPI()

class User(BaseModel):
    name : str
    age  : int 

@app.post("/create-user")
def create_user(user : User):
    return {
        "message" : "User created" ,
        "data"    : user
    }

# the main differnce in dict and pydantic is the validation and error handling 
# dict is flexible an pydantic is structured .
# error handling is auto is pydantic whereas manual in dict.