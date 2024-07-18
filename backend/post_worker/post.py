import os
from post_config import *
from generate_sha import *
from check_post_local import *
from create_post import *
from datetime import datetime


class Post:
    def __init__(self,text : str,lifetime : int,author_name: str,author_id: str):
        self.text = text
        self.lifetime = f"{lifetime}${datetime.now().strftime('%Y-%m-%d %H:%M')}"
        print(self.lifetime)
        self.author_name  = author_name
        self.author_id = author_id
    async def create_post(self) -> [str]:
        r_sha = await generate_random_hash(max_id_lenght)
        post_id = f"{self.author_id}${r_sha}"
        while await check_file_exists(posts_dir,f"{post_id}.txt"):
            post_id = f"{self.author_id}${r_sha}"
        await create_file_in_directory(posts_dir,f"/{post_id}.txt",self.text)
        return [post_id,self.lifetime]

