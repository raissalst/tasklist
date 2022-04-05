from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.configs.database import db


class EisenhowerModel(db.Model):

    __tablename__ = "eisenhowers"

    id = Column(Integer, primary_key=True)
    type = Column(String(100))

    # criando um atributo virtual na tabela tasks chamado eisen que referencia o model eisenhower
    tasks = relationship("TaskModel", backref="eisen", uselist=True)
