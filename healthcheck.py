from flask import Blueprint

healthcheck = Blueprint("healthcheck", __name__)

@healthcheck.route("/healthz")
def healthz():
    return "OK", 200
