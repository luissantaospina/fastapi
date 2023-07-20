from fastapi import FastAPI, APIRouter
from .models import database, User, Movie, UserReview
from .routers import user_router, movie_router, user_review_router, auth_router
from .middlewares import ErrorHandler
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

app = FastAPI()
app.title = "My first API"
app.version = "0.0.2"

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.add_middleware(ErrorHandler)

api_v1 = APIRouter(prefix='/api/v1')
api_v1.include_router(user_router)
api_v1.include_router(user_review_router)
api_v1.include_router(movie_router)
api_v1.include_router(auth_router)
app.include_router(api_v1)

handler = Mangum(app)


@app.on_event('startup')
def startup():
    if database.is_closed():
        database.connect()
    database.create_tables([User, Movie, UserReview])


@app.on_event('shutdown')
def shutdown():
    if not database.is_closed():
        database.close()
