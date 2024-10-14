import datetime

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DECIMAL, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.db.database import Base
from src.models.base import TimestampMixin

class Payment(Base, TimestampMixin):
    __tablename__ = "payments"

    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    debt_id = Column(Integer, ForeignKey('debts.id'), nullable=False)
    amount_paid = Column(DECIMAL(10, 2), nullable=False)
    payment_date = Column(Date)
    