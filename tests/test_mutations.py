from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from api.models import Post


def test_createPost(client: Flask, session: SQLAlchemy):
    title = description = "test"
    query = f"mutation {{ createPost(title: \"{title}\" description: \"{description}\") {{ post {{ id, title, description }} success }} }}"
    response = client.post("/graphql", json={"query": query})
    assert response.status_code == 200
    expected_post = session.query(Post).filter(Post.title == title).first()
    assert expected_post
    assert response.json["data"]["createPost"]["success"]
    assert response.json["data"]["createPost"]["post"] == {
        "id": expected_post.id,
        "title": expected_post.title,
        "description": expected_post.description,
    }
