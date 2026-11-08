#Path parameters allow you to pass values directly through a URL path.
#For example, instead of creating a separate route for every user, you can use a dynamic parameter.


#In FastAPI, a dynamic route (dynamic router) is a route that accepts variable values through the URL instead of using fixed URLs.
from fastapi import FastAPI

app = FastAPI()

#Users Route
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
