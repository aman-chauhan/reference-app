from flask import Flask


config = {"development": {"DEBUG": True}, "production": {"DEBUG": False}}


def create_apiserver(config_name: str = "production") -> Flask:
    app = Flask(__name__)
    app.config.from_mapping(config[config_name])

    from .helloworld import bp as helloworld_bp

    app.register_blueprint(helloworld_bp)

    return app
