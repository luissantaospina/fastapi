from typing import List
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import MovieRequestModel, MovieResponseModel
from fastapi import APIRouter, Depends, Path
from ..helpers import oauth2_scheme
from ..services import MovieService

router = APIRouter(
    prefix='/movies',
    tags=["movies"],
    dependencies=[Depends(oauth2_scheme)]
)


@router.post("", response_model=MovieResponseModel, tags=["movies"])
async def create_movie(movie: MovieRequestModel, db: Session = Depends(get_db)) -> MovieResponseModel:
    movie_created = MovieService.create_movie(movie, db)
    return movie_created


@router.get("", response_model=List[MovieResponseModel])
async def get_movies(page: int = 1, limit: int = 10, db: Session = Depends(get_db)) -> List[MovieResponseModel]:
    movies = MovieService.get_movies(page, limit, db)
    return movies


@router.get("/{movie_id}", response_model=MovieResponseModel)
def get_movie(movie_id: int = Path(ge=1), db: Session = Depends(get_db)) -> MovieResponseModel:
    movie = MovieService.get_movie(movie_id, db)
    return movie


@router.put("/{movie_id}", response_model=MovieResponseModel)
async def update_movie(movie_request: MovieRequestModel, movie_id: int = Path(ge=1), db: Session = Depends(get_db)) \
        -> MovieResponseModel:
    movie_updated = MovieService.update_movie(movie_request, movie_id, db)
    return movie_updated


@router.delete("/{movie_id}", response_model=MovieResponseModel)
def delete_movie(movie_id: int = Path(ge=1), db: Session = Depends(get_db)) -> MovieResponseModel:
    movie_deleted = MovieService.delete_movie(movie_id, db)
    return movie_deleted
