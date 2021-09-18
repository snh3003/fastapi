from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

# instance or object
app = FastAPI()

# decorator or route or path
@app.get("/")
def index(limit, published: bool, sort: Optional[str] = None):
    if(published):
        return {
            "blogs": " all blogs "
        }
    return {"blog": f"{limit} list of blogs "}

@app.get('/blog/unpublished')
def blog_unpublished():
    return {
        "data": "list of unpublished blogs"
    }

# dynamic routing 
@app.get("/blog/{id}")
def blog(id: int):
    return {
        "blog": "blog detail",
        "blog_id": id
    }

@app.get("/blog/{id}/comments")
def blog_comments(id: int):
    return{
        "blog": "blog name",
        "blog_id": id,
        "comments": ['hell', "0"]
    }

class Blog(BaseModel):
    id: int
    title: str
    published: bool

@app.post("/blog")
def create(blog: Blog):
    return {
        "status": "created",
        "blog": blog.title,
    }
