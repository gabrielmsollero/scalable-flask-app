from flask import abort, jsonify, Request

from app.extensions import db
from ..models.post import Post


def posts_get(request: Request):
    return jsonify([p.serialized for p in Post.query.all()])


def posts_post(request: Request):
    new_post_data = request.json
    new_post = Post(**new_post_data)

    db.session.add(new_post)
    db.session.commit()

    return "", 201


def posts_id_get(id: str, request: Request):
    post: Post = Post.query.get(int(id))
    if post is None:
        abort(404)

    return jsonify(post.serialized)


def posts_id_put(id: str, request: Request):
    post: Post = Post.query.get(int(id))
    if post is None:
        abort(404)

    for key, value in request.json.items():
        setattr(post, key, value)

    db.session.commit()
    return "", 204


def posts_id_delete(id: str, request: Request):
    post: Post = Post.query.get(int(id))
    if post is None:
        abort(404)

    db.session.delete(post)
    db.session.commit()
    return "", 204
