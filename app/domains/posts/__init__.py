from flask import abort, Blueprint, jsonify, request

from . import services

bp = Blueprint("posts", __name__)


@bp.route("/posts", methods=("GET", "POST"))
def posts():
    global POSTS
    if request.method == "GET":
        return services.posts_get(request)

    if request.method == "POST":
        return services.posts_post(request)


@bp.route("/posts/<id>", methods=("GET", "PUT", "DELETE"))
def posts_id(id: str):
    global POSTS
    if request.method == "GET":
        return services.posts_id_get(id, request)

    if request.method == "PUT":
        return services.posts_id_put(id, request)

    if request.method == "DELETE":
        return services.posts_id_delete(id, request)
