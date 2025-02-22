def test_ping_get(client):
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.text == "pong"


def test_graphql_get(client):
    response = client.get("/graphql")
    assert response.status_code == 200
    assert response.content_type == "text/html; charset=utf-8"


def test_graphql_post(client):
    query = "query { listPosts { success errors } }"
    response = client.post("/graphql", json={"query": query})
    assert response.status_code == 200
    assert response.json["data"]["listPosts"]["success"]
