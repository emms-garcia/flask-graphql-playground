from flask import Flask

from api.models import Post


def test_getPost(client: Flask, expected_post: Post):
    query = f"query {{ getPost(id: {expected_post.id}) {{ post {{ id, title, description }} success }} }}"
    response = client.post("/graphql", json={"query": query})
    assert response.status_code == 200
    assert response.json["data"]["getPost"]["success"]
    assert response.json["data"]["getPost"]["post"] == {
        "id": expected_post.id,
        "title": expected_post.title,
        "description": expected_post.description,
    }


def test_listPosts(client: Flask, expected_post: Post):
    query = "query { listPosts { posts { id, title, description } success } }"
    response = client.post("/graphql", json={"query": query})
    assert response.status_code == 200
    assert response.json["data"]["listPosts"]["success"]
    assert response.json["data"]["listPosts"]["posts"] == [
        {
            "id": expected_post.id,
            "title": expected_post.title,
            "description": expected_post.description,
        }
    ]
