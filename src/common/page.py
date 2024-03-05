from dataclasses import dataclass
from typing import Optional

from fastapi import Query

from src.api.schema import Schema


@dataclass(frozen=True)
class PaginationParams:
    page: int = Query(0)
    limit: int = Query(100)


class Details(Schema):
    page: Optional[int] = None
    limit_per_page: Optional[int] = None
    total_pages: Optional[int] = None
    total_items: Optional[int] = None
