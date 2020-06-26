from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Schema


class DateTimeModelMixin(BaseModel):
    created_at: Optional[datetime] = Schema(..., alias="createdAt")


class DBModelMixin(DateTimeModelMixin):
    id: Optional[int] = None
