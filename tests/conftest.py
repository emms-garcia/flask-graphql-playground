from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker
import pytest

from datetime import datetime, timezone

from api import create_app, db
from api.models import Post


@pytest.fixture(scope="session")
def app():
    app = create_app()
    ctx = app.test_request_context()
    ctx.push()
    yield app
    ctx.pop()


@pytest.fixture(scope="session", autouse=True)
def client(app: Flask):
    with app.test_client() as client:
        yield client


@pytest.fixture(scope="function", autouse=True)
def session_transaction():
    connection = db.engine.connect()
    connection.begin()
    # Use a scoped session that binds to our connection
    db.session = scoped_session(sessionmaker(bind=connection))
    yield  # This is where the test runs
    # Rollback and remove session after test
    connection.close()
    db.session.remove()


@pytest.fixture(scope="function")
def session():
    session = db.session
    session.begin()
    yield session
    session.rollback()
    session.remove()


@pytest.fixture(scope="function")
def expected_post(session: SQLAlchemy):
    title = description = "test"
    post = Post(
        created_at=datetime.now(timezone.utc),
        title=title,
        description=description,
    )
    session.add(post)
    session.flush()
    yield post
