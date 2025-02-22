from api import db
from api.models import Post


def listPosts_resolver(obj: object, info: object) -> dict:
    try:
        posts = [post.to_dict() for post in db.session.query(Post).all()]
        return {"success": True, "posts": posts}
    except Exception as error:
        return {"success": False, "errors": [str(error)]}


def getPost_resolver(obj: object, info: object, id: int) -> dict:
    try:
        post = db.session.get(Post, id)
        return {"success": True, "post": post.to_dict()}
    except AttributeError:
        return {
            "success": False,
            "errors": [f"Post item matching {id} not found"]
        }
