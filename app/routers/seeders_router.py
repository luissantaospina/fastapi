from fastapi import APIRouter
from app.database.seeders.movie_seeder import seed_movies

router = APIRouter(
    prefix='/seeders',
    tags=["seeders"]
)


@router.post("")
async def create_seeders() -> dict:
    seed_movies()
    return {"message": "Seeders created"}
