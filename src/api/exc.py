from fastapi import status, HTTPException


def already_exists_exception(field: str, value: str):
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT, 
        detail=f"value {value} already exists for field {field}"
    )


def not_found_exception(field: str, value: str):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"field {field} not found on {value}"
    )


def incorrect_password_exception():
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect password!"
    )