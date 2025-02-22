from os import getenv
import logging

from app import app


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    PORT = getenv("FLASK_RUN_PORT") or "8080"
    DEBUG = getenv("FLASK_DEBUG_MODE") or None
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
