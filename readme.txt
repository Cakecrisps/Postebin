posts ->
cd backend/post_worker
uvicorn post_listener:app --host 127.0.0.1 --port 4000
db ->
cd backend/bd
uvicorn post_listener:app --host 127.0.0.1 --port 5050
API ->
cd backend
uvicorn post_listener:app --host 127.0.0.1 --port 80
