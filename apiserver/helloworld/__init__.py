from flask import Blueprint


bp = Blueprint("helloworld", __name__)


@bp.route("/")
def home():
    return "<h1>Hello World</h1>"
