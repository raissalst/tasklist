from flask import Blueprint

from app.controllers import category_controller

bp = Blueprint("categories", __name__)

bp.post("/categories")(category_controller.create_category)
bp.get("/")(category_controller.read_category)
bp.patch("/categories/<int:id>")(category_controller.update_category)
bp.delete("/categories/<int:id>")(category_controller.delete_category)
