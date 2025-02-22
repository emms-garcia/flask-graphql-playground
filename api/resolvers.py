from api import db
from api.models import Post


def listPosts_resolver(obj: object, info: object) -> dict:
    posts = [post.to_dict() for post in db.session.query(Post).all()]
    return {"success": True, "posts": posts}


def getPost_resolver(obj: object, info: object, id: int) -> dict:
    post = db.session.get(Post, id)
    if not post:
        return {
            "success": False,
            "errors": [f"Post with id {id} not found"]
        }

    return {"success": True, "post": post.to_dict()}
