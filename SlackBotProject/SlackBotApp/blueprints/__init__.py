from flask import Blueprint
from ..services import get_service

slack_blueprint = Blueprint("slack_blueprint", __name__)


@slack_blueprint.get("/")
def index():
    return get_service("INDEX")
