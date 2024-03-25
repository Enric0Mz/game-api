from fastapi import status, HTTPException


def already_exists_exception(field: str, value: str):
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT, 
        detail=f"value {value} already exists for field {field}"
    )
