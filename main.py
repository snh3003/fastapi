from fastapi import FastAPI

# instance or object
app = FastAPI()

# decorator or route or path
@app.get("/")

def index():
    return {"blog": "blog list"}

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