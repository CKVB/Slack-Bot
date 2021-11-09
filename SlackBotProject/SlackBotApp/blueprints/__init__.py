from flask import Blueprint, request
from ..services import get_service

slack_blueprint = Blueprint("slack_blueprint", __name__)


@slack_blueprint.get("/")
def index():
    return get_service("INDEX")


@slack_blueprint.post("/prime")
def prime():
    resp = request.form
    number = int(resp.get("text"))
    is_prime = True
    
    for i in range(2, number//2):
        if not number % i:
            is_prime = False
            break

    return f"{number} is " + ["Prime" if is_prime else "Not Prime"][0]
