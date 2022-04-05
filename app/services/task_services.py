from app.models.eisenhower_model import EisenhowerModel


def eisenhower_search(importance: int, urgency: int):
    if (importance + urgency) % 2 == 0:
        if importance == 1:
            eisen_category = EisenhowerModel.query.filter_by(type="Do It First").one()
            return eisen_category.id

        eisen_category = EisenhowerModel.query.filter_by(type="Delete It").one()
        return eisen_category.id

    if importance == 1:
        eisen_category = EisenhowerModel.query.filter_by(type="Delegate It").one()
        return eisen_category.id

    eisen_category = EisenhowerModel.query.filter_by(type="Schedule It").one()
    return eisen_category.id
