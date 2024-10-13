import datetime

from sqlalchemy import Column, Integer, String, Boolean, Date, DECIMAL, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.db.database import Base
from src.models.base import TimestampMixin

class Debt(Base, TimestampMixin):
    __tablename__ = "debts"

    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    amount = Column(DECIMAL(10,2), default=0)
    description = Column(Text, nullable=True)
    is_payed = Column(Boolean, default=False)
    due_date = Column(Date)
    borrower_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    creditor_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    borrower = relationship("User", foreign_keys=[borrower_id], back_populates="borrower_debts")
    creditor = relationship("User", foreign_keys=[creditor_id], back_populates="creditor_debts")
