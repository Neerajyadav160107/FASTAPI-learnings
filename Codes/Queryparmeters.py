from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_users(name: str = None ):
    return {"Name":name}


@app.get("/items")
def get_users(name: str = None , price : int=0 ):
    return {
        "name" :  name,
        "price" : price
    }

##real word usecase: search , filter , pagination : ex-filter in e-commerce 