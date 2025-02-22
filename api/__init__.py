from flask import Flask

from api.extensions import cors, db


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize CORS and DB
    import api.models  # noqa
    with app.app_context():
        cors.init_app(app)
        db.init_app(app)
        db.create_all()

    # Initialize Routes
    from api.routes import blueprint
    app.register_blueprint(blueprint)

    return app
