from fastapi import FastAPI
from post import Post
from post_config import posts_dir
from meet_with_others.to_db import add_post_to_db
from check_post_local import check_file_exists
app = FastAPI()


@app.post("/post/add")
async def add_post(text : str,author_id : str,lifetime : int,author_name : str):
    new_post = Post(text = text,author_id = author_id,lifetime=lifetime,author_name=author_name)
    r = await new_post.create_post()
    post_id = r[0]
    lifetime = r[1]
    r = await add_post_to_db(post_id,author_id,lifetime)
    if r == 'ok':
        return 'ok'
    else:
        return 'e'

@app.get("/post/get/{post_id}") #TODO
async def get_post(post_id):
    print(1)
    f = await check_file_exists(posts_dir + '/',f"{post_id}.txt")
    if f:
        with open(f"{posts_dir}/{post_id}.txt",'r') as f:
            return f.read()
    else:
        return "ooops..."
