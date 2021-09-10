from fastapi import FastAPI
from awoo_logger.log import CustomizeLogger
from pathlib import Path
from fastapi import Request, Response
from app.schema import (RequestBody,
                        ResponseSchema)
import uvicorn
import logging
import os
import uuid
logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    app = FastAPI(title='CustomLogger', debug=False)
    logger = CustomizeLogger.make_logger()
    app.logger = logger

    return app

def add(body):
    return body.Number_1+body.Number_2

def division(body):
    return body.Number_1/body.Number_2
app = create_app()

@app.post(f'/add', response_model=ResponseSchema)
async def test_add(body: RequestBody):
    
    app.logger.bind(log_type="ACCESS_LOG").info("request:{}".format(body))
    result = add(body)
    
    response_list = {
        "status":"success",
        "result":result
    }
    app.logger.bind(log_type="ACCESS_LOG").info("response:{}".format(response_list))
    return response_list

@app.post(f'/divide', response_model=ResponseSchema)
async def test_divide(body: RequestBody, request: Request):
    app.logger.bind(log_type="ACCESS_LOG").info("request:{}".format(body))
    if body.Number_2==0:
        app.logger.bind(log_type="exception warning").warning("Number_2 is zero, it will cause error")
    result = division(body)
    
    response_list = {
        "status":"success",
        "result":result
    }
    response = Response( media_type='text/plain')
    app.logger.bind(log_type="ACCESS_LOG").info("response:{} ,status_code:{}".format(response_list, response.status_code))
    return response_list