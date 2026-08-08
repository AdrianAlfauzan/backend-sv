from fastapi import FastAPI, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import schemas, crud

app = FastAPI(title="Article API", version="1.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/article", status_code=status.HTTP_201_CREATED)
def create_article(article: schemas.PostCreate, db: Session = Depends(get_db)):
    crud.create_post(db, article)
    return {}


@app.get("/article/{limit}/{offset}")
def get_articles(limit: int, offset: int, db: Session = Depends(get_db)):
    posts = crud.get_posts(db, limit=limit, offset=offset)
    return [
        {
            "id": p.id,  
            "title": p.Title,
            "content": p.Content,
            "category": p.Category,
            "status": p.Status,
            "created_date": p.Created_date.isoformat() if p.Created_date else None,
            "updated_date": p.Updated_date.isoformat() if p.Updated_date else None,
        }
        for p in posts
    ]


@app.get("/article/{post_id}")
def get_article(post_id: int, db: Session = Depends(get_db)):
    post = crud.get_post(db, post_id)
    return {
        "id": post.id,  
        "title": post.Title,
        "content": post.Content,
        "category": post.Category,
        "status": post.Status,
        "created_date": post.Created_date.isoformat() if post.Created_date else None,
        "updated_date": post.Updated_date.isoformat() if post.Updated_date else None,
    }


@app.patch("/article/{post_id}")
def update_article(
    post_id: int, 
    article_update: schemas.PostUpdate, 
    db: Session = Depends(get_db)
):
    crud.update_post(db, post_id, article_update)
    return {}


@app.delete("/article/{post_id}")
def delete_article(post_id: int, db: Session = Depends(get_db)):
    crud.delete_post(db, post_id)
    return {}