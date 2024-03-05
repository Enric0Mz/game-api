from typing import Generic, Optional, TypeVar

from pydantic import Field
from pydantic import BaseModel
from src.api.schema import Schema

from .page import Details

T_co = TypeVar("T_co", bound=Schema, covariant=True)


class ListResult(Schema, BaseModel, Generic[T_co]):
    data: list[T_co] = Field(default_factory=list)
    details: Optional[Details] = Field(default_factory=Details)
