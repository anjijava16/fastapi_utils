from sqlalchemy.orm import Session
from app.databaseapi.db.models import movies
from app.databaseapi.schema import MovieBase


def get_movie_by_movie_id(db: Session, movie_id: int):
    res = db.query(movies.Movies).filter(movies.Movies.movie_id == movie_id).first()
    return res


def get_movie_id(db: Session, sl_id: int):
    res = db.query(movies.Movies).filter(movies.Movies.id == sl_id).first()
    return res;


def get_movies(db: Session, skip: int = 0, limit: int = 100):
    res = db.query(movies.Movies).offset(skip).limit(limit).all()
    return res


def add_movie_details_to_db(db: Session, movie: MovieBase.MovieAdd):
    mv_details = movies.Movies(
        movie_id=movie.movie_id,
        movie_name=movie.movie_name,
        director=movie.director,
        geners=movie.geners,
        membership_required=movie.membership_required,
        cast=movie.cast,
        streaming_platform=movie.streaming_platform

    )
    db.add(mv_details)
    db.commit()
    db.refresh(mv_details)
    res = movies.Movies(**movie.dict())
    return res


def update_movie_details(db: Session, sl_id: int, details: MovieBase.UpdateMovie):
    """
    This method update the movie details by sl_id
    :param db: database session object
    :param sl_id: serial id of record or primary key
    :param details: Object of class MovieBase.UpdateMovie
    :return: update_movie_details the movie record

    """
    try:
        db.query(movies.Movies).filter(movies.Movies.id == sl_id).update(vars(details))
        db.commit()
        return db.query(movies.Movies).filter(movies.Movies.id == sl_id).first()
    except Exception as e:
        raise Exception(e)
    pass


def delete_movie_details_by_id(db: Session, sl_id: int):
    """
    This will delete the record from database based on Primary key
    :param db: database session object
    :param sl_id: serial id of record or primary key
    :return: None

    """
    try:
        db.query(movies.Movies).filter(movies.Movies.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)
    pass
