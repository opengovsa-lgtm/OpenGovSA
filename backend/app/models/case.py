from sqlalchemy import Column, String, Numeric
from app.database import Base

class Case(Base):
    __tablename__ = "cases"

    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    amount_confirmed = Column(Numeric(18,2), default=0)
