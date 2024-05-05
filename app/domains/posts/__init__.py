from flask import abort, Blueprint, jsonify, request

POSTS = [
    {
        "id": 1,
        "title": "The first post",
        "author_id": 1,
        "content": "Content of the first post",
    },
    {
        "id": 2,
        "title": "The second post",
        "author_id": 2,
        "content": "Content of the second post",
    },
]

bp = Blueprint("posts", __name__)


@bp.route("/posts", methods=("GET", "POST"))
def posts():
    global POSTS
    if request.method == "GET":
        return jsonify(POSTS)

    if request.method == "POST":
        new_post = request.json
        POSTS.append(new_post)
        return "", 201


@bp.route("/posts/<id>", methods=("GET", "PUT", "DELETE"))
def posts_id(id: str):
    global POSTS
    if request.method == "GET":
        try:
            post = next(filter(lambda p: str(p["id"]) == id, POSTS))
        except StopIteration:
            abort(404)
        return jsonify(post)

    if request.method == "PUT":
        try:
            post = next(filter(lambda p: str(p["id"]) == id, POSTS))
        except StopIteration:
            abort(404)

        for key, value in request.json.items():
            post[key] = value

        return "", 204

    if request.method == "DELETE":
        POSTS = list(filter(lambda p: str(p["id"]) != id, POSTS))
        return "", 204
