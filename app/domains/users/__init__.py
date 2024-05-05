from flask import Blueprint, request

from . import services

bp = Blueprint("users", __name__)


@bp.route("/users", methods=("GET", "POST"))
def users():
    if request.method == "GET":
        return services.users_get(request)

    if request.method == "POST":
        return services.users_post(request)


@bp.route("/users/<id>", methods=("GET", "PUT", "DELETE"))
def users_id(id: str):
    if request.method == "GET":
        return services.users_id_get(id, request)

    if request.method == "PUT":
        return services.users_id_put(id, request)

    if request.method == "DELETE":
        return services.users_id_delete(id, request)
