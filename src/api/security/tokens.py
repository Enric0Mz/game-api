import jwt

from datetime import datetime
from datetime import timedelta
from typing import Optional

from src.core.settings import SECRET_KEY
from src.core.settings import ALGORITHM


def create_token(data: dict, expires_delta: timedelta) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
