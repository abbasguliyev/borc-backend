import datetime

from sqlalchemy import Column, Date
from sqlalchemy.sql import func

class TimestampMixin:
    created_at = Column(Date, server_default=func.now())
    updated_at = Column(Date, server_default=func.now(), onupdate=datetime.datetime.utcnow())