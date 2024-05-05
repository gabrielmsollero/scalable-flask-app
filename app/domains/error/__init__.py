from flask import Blueprint, jsonify
from werkzeug.exceptions import (
    HTTPException,
    NotFound,
)

bp = Blueprint("error", __name__)


@bp.app_errorhandler(HTTPException)
def handle_http_exception(e):
    return jsonify({"error": str(e)}), e.code


@bp.app_errorhandler(NotFound)
def handle_not_found(e):
    return jsonify({"error": f"NotFound - {str(e)}"}), 404
