from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate

app = FastAPI()

text_posts = {1: {"title": "ruthvik", "posts": "hello, world!"}}


@app.get("/posts")
async def list_posts():
    return text_posts


@app.get("/posts/{id}")
async def retrieve_post(id: int):
    if id != 1:
        return HTTPException(status_code=404, detail="invalid path parameter")
    return {"id": id}


@app.post("/posts")
async def create_post(post: PostCreate):
    text_posts[max(text_posts.keys()) + 1] = post
    return post
