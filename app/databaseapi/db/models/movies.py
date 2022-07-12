from sqlalchemy import Boolean, Column, Integer, String
from app.databaseapi.db.db_handler import Base


class Movies(Base):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    movie_id = Column(String(100), unique=True, index=True, nullable=False)
    movie_name = Column(String(255), index=True, nullable=False)
    director = Column(String(100), index=True, nullable=False)
    geners = Column(String(100), index=True, nullable=False)
    membership_required = Column(Boolean, nullable=False, default=True)
    cast = Column(String(255), index=True, nullable=False)
    streaming_platform = Column(String(100), index=True)
