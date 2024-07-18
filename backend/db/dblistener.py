from fastapi import FastAPI

app = FastAPI()

@app.post("/db/adduser") #TODO
async def adduser(user_name : str):
    ...

@app.post("/db/checkuser") #TODO
async def adduser(user_name : str):
    ...

@app.post("/db/addviews") #TODO
async def adduser(user_name : str):
    ...

