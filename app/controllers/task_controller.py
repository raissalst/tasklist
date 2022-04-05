from http import HTTPStatus

from flask import current_app, jsonify, request
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound

from app.exc.invalid_number_error import InvalidNumberError
from app.models.category_model import CategoryModel
from app.models.eisenhower_model import EisenhowerModel
from app.models.task_model import TaskModel
from app.services.task_services import eisenhower_search


def create_task():
    data = request.get_json()

    new_categories_list = []

    try:
        categories_requested = data.pop("categories")

        for category in categories_requested:
            category = category.lower()

            # lista com categorias normalizadas:
            new_categories_list.append(category)

            # crio as categorias caso não existam:
            if CategoryModel.query.filter_by(name=category).one_or_none() == None:
                new_category = CategoryModel(name=category, description="")
                current_app.db.session.add(new_category)
                current_app.db.session.commit()

        new_task = TaskModel(**data)

        for category in new_categories_list:
            find_category = CategoryModel.query.filter_by(name=category).one()
            new_task.categories.append(find_category)

        eisenhower_category_id = eisenhower_search(data["importance"], data["urgency"])
        new_task.eisenhower_id = eisenhower_category_id

        current_app.db.session.add(new_task)
        current_app.db.session.commit()

        classification = EisenhowerModel.query.filter_by(
            id=new_task.eisenhower_id
        ).one()

        return (
            jsonify(
                {
                    "id": new_task.id,
                    "name": new_task.name,
                    "description": new_task.description,
                    "duration": new_task.duration,
                    "classification": classification.type,
                    "categories": new_categories_list,
                }
            ),
            HTTPStatus.CREATED,
        )

    except InvalidNumberError:
        return {
            "msg": {
                "valid_options": {"importance": [1, 2], "urgency": [1, 2]},
                "received_options": {
                    "importance": data["importance"],
                    "urgency": data["urgency"],
                },
            }
        }, HTTPStatus.BAD_REQUEST

    except IntegrityError:
        return {"msg": "task already exists!"}, HTTPStatus.CONFLICT

    except KeyError:
        return {"msg": "missing key 'categories'"}, HTTPStatus.BAD_REQUEST


def update_task(id):
    data = request.get_json()

    categories_requested = data.pop("categories", None)
    new_categories_list = []

    # tenho meu array normalizado aqui e categorias criadas, caso não existam
    if categories_requested:
        for category in categories_requested:
            category = category.lower()

            # lista com categorias normalizadas:
            new_categories_list.append(category)

            # crio as categorias caso não existam:
            if CategoryModel.query.filter_by(name=category).one_or_none() == None:
                new_category = CategoryModel(name=category, description="")
                current_app.db.session.add(new_category)
                current_app.db.session.commit()

    try:
        updated_task = TaskModel.query.get_or_404(id)

        for key, value in data.items():
            if key == "name":
                setattr(updated_task, key, value.lower())
            if key == "importance" or key == "urgency":
                if value < 1 or value > 2:
                    raise InvalidNumberError
            setattr(updated_task, key, value)

        eisenhower_category_id = eisenhower_search(
            updated_task.importance, updated_task.urgency
        )
        updated_task.eisenhower_id = eisenhower_category_id

        if categories_requested:
            updated_task.categories.clear()
            for category in new_categories_list:
                find_category = CategoryModel.query.filter_by(name=category).one()
                updated_task.categories.append(find_category)

        current_app.db.session.add(updated_task)
        current_app.db.session.commit()

        classification = EisenhowerModel.query.filter_by(
            id=updated_task.eisenhower_id
        ).one()

        return (
            jsonify(
                {
                    "id": updated_task.id,
                    "name": updated_task.name,
                    "description": updated_task.description,
                    "duration": updated_task.duration,
                    "classification": classification.type,
                    "categories": [
                        x.name
                        for x in updated_task.categories
                        if updated_task.categories
                    ],
                }
            ),
            HTTPStatus.OK,
        )

    except NotFound:
        return {"msg": "task not found!"}, HTTPStatus.NOT_FOUND

    except InvalidNumberError:
        return {
            "msg": {"valid_options": {"importance": [1, 2], "urgency": [1, 2]}}
        }, HTTPStatus.BAD_REQUEST


def delete_task(id):
    try:
        filtered_task = TaskModel.query.get_or_404(id)

        current_app.db.session.delete(filtered_task)
        current_app.db.session.commit()

        return {}, HTTPStatus.NO_CONTENT

    except NotFound:
        return {"msg": "task not found!"}, HTTPStatus.NOT_FOUND
