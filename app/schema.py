from typing import Dict, List, Optional, Union

from fastapi.openapi.models import Example
from pydantic import BaseModel, Field
from requests import models
from starlette.responses import FileResponse
import uuid

# 定義規格
class RequestBody(BaseModel):
    Number_1: int = Field(default=1, description="first number to be added")
    Number_2: int = Field(default=2, description="second number to be added")
    
class ResponseSchema(BaseModel):
    status: str = Field(example="success or failure")
    result: int = Field(example=3)
