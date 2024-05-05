from flask import abort, jsonify, Request

from app.extensions import db
from app.models.user import User


def users_get(request: Request):
    return jsonify([u.serialized for u in User.query.all()])


def users_post(request: Request):
    new_user_data = request.json
    new_user = User(**new_user_data)

    db.session.add(new_user)
    db.session.commit()

    return "", 201


def users_id_get(id: str, request: Request):
    user: User = User.query.get(int(id))
    if user is None:
        abort(404)

    return jsonify(user.serialized)


def users_id_put(id: str, request: Request):
    user: User = User.query.get(int(id))
    if user is None:
        abort(404)

    for key, value in request.json.items():
        setattr(user, key, value)

    db.session.commit()
    return "", 204


def users_id_delete(id: str, request: Request):
    user: User = User.query.get(int(id))
    if user is None:
        abort(404)

    db.session.delete(user)
    db.session.commit()
    return "", 204
