from flask import abort, jsonify, Request

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


def posts_get(request: Request):
    global POSTS
    return jsonify(POSTS)


def posts_post(request: Request):
    global POSTS
    new_post = request.json
    POSTS.append(new_post)
    return "", 201


def posts_id_get(id: str, request: Request):
    global POSTS
    try:
        post = next(filter(lambda p: str(p["id"]) == id, POSTS))
    except StopIteration:
        abort(404)
    return jsonify(post)


def posts_id_put(id: str, request: Request):
    global POSTS
    try:
        post = next(filter(lambda p: str(p["id"]) == id, POSTS))
    except StopIteration:
        abort(404)

    for key, value in request.json.items():
        post[key] = value

    return "", 204


def posts_id_delete(id: str, request: Request):
    global POSTS
    POSTS = list(filter(lambda p: str(p["id"]) != id, POSTS))
    return "", 204
