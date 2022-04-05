from http import HTTPStatus

from flask import current_app, jsonify, request
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Query
from werkzeug.exceptions import NotFound

from app.models.category_model import CategoryModel
from app.models.eisenhower_model import EisenhowerModel
from app.models.task_model import TaskModel
from app.models.tasks_categories_table import tasks_categories


def create_category():
    data = request.get_json()

    try:
        new_category = CategoryModel(**data)

        current_app.db.session.add(new_category)
        current_app.db.session.commit()

        return jsonify(new_category), HTTPStatus.CREATED

    except IntegrityError:
        return {"msg": "category already exists!"}, HTTPStatus.CONFLICT


def update_category(id):
    data = request.get_json()

    try:
        filtered_category = CategoryModel.query.get_or_404(id)

        for key, value in data.items():
            if key == "name":
                setattr(filtered_category, key, value.lower())
            else:
                setattr(filtered_category, key, value)

        current_app.db.session.add(filtered_category)
        current_app.db.session.commit()

        return jsonify(filtered_category), HTTPStatus.OK

    except NotFound:
        return {"msg": "category not found!"}, HTTPStatus.NOT_FOUND
    except IntegrityError:
        return {"msg": "category already exists!"}, HTTPStatus.CONFLICT


def delete_category(id):
    try:
        filtered_category = CategoryModel.query.get_or_404(id)

        current_app.db.session.delete(filtered_category)
        current_app.db.session.commit()

        return {}, HTTPStatus.NO_CONTENT

    except NotFound:
        return {"msg": "category not found!"}, HTTPStatus.NOT_FOUND


def read_category():
    list_categories_with_tasks = CategoryModel.query.order_by(CategoryModel.id).all()

    categories_with_tasks_list = []
    list_of_categories_ids = []

    for cat in list_categories_with_tasks:
        cats_dict = {}

        cats_dict["id"] = cat.id
        cats_dict["name"] = cat.name
        cats_dict["description"] = cat.description
        cats_dict["tasks"] = []

        categories_with_tasks_list.append(cats_dict)

    for item in categories_with_tasks_list:
        list_of_categories_ids.append(item["id"])

    base_query: Query = (
        current_app.db.session.query(
            CategoryModel,
            TaskModel.id,
            TaskModel.name,
            TaskModel.description,
            TaskModel.duration,
            EisenhowerModel.type.label("classification"),
        )
        .select_from(TaskModel)
        .join(tasks_categories)
        .join(CategoryModel)
        .join(EisenhowerModel)
        .order_by(CategoryModel.id)
    )

    column_names = [q["name"] for q in base_query.column_descriptions]

    serialized_data = [dict(zip(column_names, row)) for row in base_query.all()]

    for item in serialized_data:
        new_dict = {}
        for cat in categories_with_tasks_list:
            if item["CategoryModel"].id == cat["id"]:
                new_dict = dict(
                    id=item["id"],
                    name=item["name"],
                    description=item["description"],
                    duration=item["duration"],
                    classification=item["classification"],
                )
                cat["tasks"].append(new_dict)
                break

    return jsonify(categories_with_tasks_list), HTTPStatus.OK
