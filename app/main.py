from fastapi import FastAPI
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
    return app

def add(body):
    return body.Number_1+body.Number_2

def division(body):
    return body.Number_1/body.Number_2
app = create_app()

@app.post(f'/add', response_model=ResponseSchema)
async def test_add(body: RequestBody):
    
    result = add(body)
    
    response_list = {
        "status":"success",
        "result":result
    }
    return response_list

@app.post(f'/divide', response_model=ResponseSchema)
async def test_divide(body: RequestBody, request: Request):
    result = division(body)
    
    response_list = {
        "status":"success",
        "result":result
    }
    response = Response( media_type='text/plain')
    return response_list