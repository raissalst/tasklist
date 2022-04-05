from flask import Blueprint

from app.controllers import task_controller

bp = Blueprint("tasks", __name__, url_prefix="/tasks")

bp.post("")(task_controller.create_task)
bp.patch("/<int:id>")(task_controller.update_task)
bp.delete("/<int:id>")(task_controller.delete_task)
