from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from api.models import Post


def test_createPost(client: Flask, session: SQLAlchemy):
    title = description = "test"
    query = f"mutation {{ createPost(title: \"{title}\" description: \"{description}\") {{ post {{ id title description }} success }} }}"
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


def test_deletePost(client: Flask, expected_post: Post, session: SQLAlchemy):
    # When -> Post not found
    query = "mutation { deletePost(id: -1) { errors success } }"
    response = client.post("/graphql", json={"query": query})
    # Then -> Return not found error
    assert response.status_code == 200
    assert not response.json["data"]["deletePost"]["success"]
    assert response.json["data"]["deletePost"]["errors"] == ["Post with id -1 not found"]

    # When -> Post found
    query = f"mutation {{ deletePost(id: {expected_post.id}) {{ success }} }}"
    response = client.post("/graphql", json={"query": query})
    # Then -> Return 200 and assert Post was deleted
    assert response.status_code == 200
    assert response.json["data"]["deletePost"]["success"]
    expected_post = session.get(Post, expected_post.id)
    assert expected_post is None
