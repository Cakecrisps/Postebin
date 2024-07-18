from fastapi import FastAPI

app = FastAPI()

@app.post('/addpost')
async def addpost(author_id : str,text : str,author_name : str,lifetime : int):
    ...

@app.get('/getpost/{post_id}')
async def addpost(post_id : str):
    ...

