from os import getenv
import logging

from api import create_app


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    DEBUG = getenv("FLASK_DEBUG_MODE") or None
    PORT = getenv("FLASK_RUN_PORT") or "8080"
    app = create_app()
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
