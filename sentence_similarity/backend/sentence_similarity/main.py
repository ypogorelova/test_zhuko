from fastapi import FastAPI
from starlette.exceptions import HTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from sentence_similarity.backend.sentence_similarity.config import API_STR
from sentence_similarity.backend.sentence_similarity.errors import (
    http_error_handler, http_422_error_handler
)
from sentence_similarity.backend.sentence_similarity.mongo_utils import (
    connect_to_mongo, close_mongo_connection
)
from sentence_similarity.backend.sentence_similarity.api import router as api_router

app = FastAPI()

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(HTTP_422_UNPROCESSABLE_ENTITY, http_422_error_handler)

app.include_router(api_router, prefix=API_STR)