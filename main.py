import json
import logging
import sys
import time
import traceback
from asyncio.log import logger
from datetime import datetime
from pathlib import Path
from uuid import uuid4

from asgi_correlation_id import CorrelationIdMiddleware
from fastapi import FastAPI, Request, Response
from fastapi.exceptions import RequestValidationError
from fastapi.logger import logger as fastapi_logger
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse

from api.v1.routers.routers import v1_router

from custom_logging import CustomizeLogger

logger_name = logging.getLogger(__name__)
config_path = Path(__file__).with_name("logging_config.json")

app = FastAPI(
    servers=[
        {"url": "http://plinor.ru/",
            "description": "Production Plinor Co."},
    ],
    logger=CustomizeLogger.make_logger(config_path),
    docs_url="/v1/docs",
    redoc_url="/v1/redoc",
    root_path="/v1/",
    debug=False,
)

app.logger = logger_name

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1_router)

app.add_middleware(GZipMiddleware, minimum_size=1000)
app.add_middleware(
    CorrelationIdMiddleware,
    header_name="X-Request-ID",
    generator=lambda: uuid4().hex,
    transformer=lambda a: a,
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    print(f"OMG! (0_0) The client sent invalid data!: {exc}")
    exc_json: dict = json.loads(exc.json())
    request_params: dict = request.path_params
    fastapi_logger.error("request_params: %s", request_params)
    request_method: str = request.method
    fastapi_logger.error("method: %s", request_method)
    request_url = request.url
    fastapi_logger.error("request_url: %s", request_url)
    request_headers_raw = request.headers.raw
    fastapi_logger.error("request_headers_raw: %s", request_headers_raw)
    # response = {"message": [], "data": None}
    response = {"detail": []}
    for error in exc_json:
        loc = error["loc"][-1]
        error_msg = error["msg"]
        error_txt = str(loc) + " " + f": {error_msg}"
        response["detail"].append(error_txt)
    response_to_logger = response
    response_to_logger["ip"] = str(request.client.host)
    fastapi_logger.error(msg=dict(detail=response_to_logger))
    return JSONResponse(response, status_code=422)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """Добавляет x-process-time в заголовок. Время затраченное на обработку запроса."""
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    response.headers["X-Real-IP"] = request.client.host
    return response


@app.get("/v1/openapi.json")
async def get_openapi_json(request: Request):
    return JSONResponse(get_openapi(
        title="Plinor Co. API",
        version="1.0.0",
        description="**Dev Production Plinor Co.**",
        routes=app.routes,
    ))


@app.on_event("startup")
async def startup_event():
    log_folder_if_exist = Path.cwd() / "logs"
    log_folder_if_exist.mkdir(parents=True, exist_ok=True)
    logger.info("Starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down...")
