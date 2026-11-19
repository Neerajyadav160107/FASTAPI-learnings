from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users =[]
class User(BaseModel):
    name : str
    age  : int

@app.post("/users")
def create_user(user:User):
    users.append(user)
    return {
        "message" : "User created" ,
        "data" : user 
    }

@app.put("/users/{user_id}")
def updated_user(user_id : int , user : User , notify : bool =False) :
    if user_id< len(users) :
        users[user_id] = user 

        return {
            "message" : "User modified",
            "notify"  :  notify,
            "data" : user
        }
    return { 
        "error" : "User not found"
    }

# Logic: Implemented user creation and update endpoints using FastAPI 
# and Pydantic. Added a notify query parameter (defaulting to False) 
# to control an optional notification flag- in the update response.