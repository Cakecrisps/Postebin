import aiohttp

async def add_post_to_db(post_id : str,author_id : str,lifetime : str):
    async with aiohttp.ClientSession() as session:
        async with session.post(url = 'https://127.0.0.1:5050/db/addpost',data={"post_id":post_id,"author_id":author_id,"lifetime":lifetime}) as response:
            data = await response.json()
            if response.status == 200:
                return 'ok'
            else:
                return 'e'
async def get_veiws_from_db(post_id : str):
    async with aiohttp.ClientSession() as session:
        async with session.post(url = 'https://127.0.0.1:5050/db/getveiws',data={"post_id":post_id}) as response:
            ...
