from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import validates

from app.configs.database import db
from app.exc.invalid_number_error import InvalidNumberError


class TaskModel(db.Model):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    duration = Column(Integer)
    importance = Column(Integer)
    urgency = Column(Integer)

    eisenhower_id = Column(
        Integer, ForeignKey("eisenhowers.id"), nullable=False, default=1
    )

    @validates("name")
    def normalize_name(self, key, value):
        return value.lower()

    @validates("importance", "urgency")
    def trunc_values(self, key, value):
        if value > 2 or value < 1:
            raise InvalidNumberError
        return value
