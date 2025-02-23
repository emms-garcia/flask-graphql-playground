from api.models import Post


def test_Post_to_dict(expected_post: Post):
    assert expected_post.to_dict() == {
        "id": expected_post.id,
        "title": expected_post.title,
        "description": expected_post.description,
        "created_at": expected_post.created_at.isoformat(),
    }
