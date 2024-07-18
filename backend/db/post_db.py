import psycopg2
from config import user,db_name,host,password


async def query(query : str,is_get : bool) -> list:
    try:
        connect = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
        )
        connect.autocommit = True
        cursor = connect.cursor()
        cursor.execute(query)
        if is_get:
            return cursor.fetchall()
        else:
            return ["ok"]
    except Exception as e:
        print('ERROR ',e)
        return ['ERROR']
    finally:
        connect.close()
        print('conn closed')




