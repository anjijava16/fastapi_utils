from typing import List
from fastapi import Depends, FastAPI, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.databaseapi.db.repositories.movierepo import *
from app.databaseapi.db.models import movies
from app.databaseapi.schema.MovieBase import *
from app.databaseapi.db.db_handler import *

movies.Base.metadata.create_all(bind=engine)

db_router = APIRouter()


@db_router.get("/welcomemovie")
async def hello():
    return {'hello': 'world'}


# Depedency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@db_router.get('/retrieve_all_movie_details', response_model=List[Movie])
async def retrive_all_movies_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movies = get_movies(db=db, skip=skip, limit=limit)
    return movies

@db_router.post('/add_new_movie', response_model=MovieAdd)
async def add_new_movie(movie: MovieAdd, db: Session = Depends(get_db)):
    movie_id = get_movie_by_movie_id(db=db, movie_id=movie.movie_id)
    if movie_id:
        raise HTTPException(status_code=400,
                            detail=f"Movie id {movie.movie_id} already exist in the database:{movie_id}")
    return add_movie_details_to_db(db=db, movie=movie)
