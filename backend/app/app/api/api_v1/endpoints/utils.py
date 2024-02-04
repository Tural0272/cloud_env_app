import json
from typing import Any, Dict, List

from fastapi import APIRouter, Depends
from app import crud, models, schemas
from app.api import deps
from sqlalchemy.orm import Session

from datetime import datetime

router = APIRouter()



@router.get("/test-test", status_code=201)
def test_test(
    
) -> Any:
    print('Received')
    return 'Received'



@router.get("/get-time", response_model=str, status_code=200)
def available_trays(
) -> Any:
    """
    Get server time.
    """
    return datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f%zZ')