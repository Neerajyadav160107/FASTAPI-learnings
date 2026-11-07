from fastapi import FastAPI 

app = FastAPI ()

#HOME ROUTE 
@app.get("/")
def home ():
    return {"message":"The World is yours"}

#ABOUT ROUTE 
@app.get("/about")
def about ():
    return {"message":"This is an about page"}

#USERS ROUTE 
@app.get("/users")
def users ():
    return {
        "users":["SURAJ","NEERAJ"]
    }