import enum

from sqlalchemy import Column, String, Integer, Date, Boolean, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.db.database import Base
from src.models.base import TimestampMixin

class GenderEnum(enum.Enum):
    male = "male"
    female = "female"


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    username = Column(String(255), unique=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255), nullable=True, unique=True)
    is_active = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
    is_staff = Column(Boolean, default=False)
    gender = Column(Enum(GenderEnum), default=GenderEnum.male, nullable=False)

    borrower_debts = relationship("Debt", foreign_keys="[Debt.borrower_id]", back_populates="borrower")
    creditor_debts = relationship("Debt", foreign_keys="[Debt.creditor_id]", back_populates="borrower")

