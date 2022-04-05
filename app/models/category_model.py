from dataclasses import dataclass

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import validates

from app.configs.database import db
from app.models.tasks_categories_table import tasks_categories


@dataclass
class CategoryModel(db.Model):
    id: int
    name: str
    description: str

    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)

    # criando um atributo virtual na tabela tasks chamado categories que referencia o category model com intermediário sendo a tabela tasks_categories, que faz a conexão entre tasks e categories
    tasks = db.relationship(
        "TaskModel", secondary=tasks_categories, backref="categories"
    )

    @validates("name")
    def normalize_name(self, key, value):
        return value.lower()
