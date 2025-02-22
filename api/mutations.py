from ariadne import convert_kwargs_to_snake_case

from datetime import datetime, timezone

from api import db
from api.models import Post
from typing import Any


@convert_kwargs_to_snake_case
def createPost_resolver(obj: Any, info: Any, title: str, description: str) -> dict:
    post = Post(title=title, description=description, created_at=datetime.now(timezone.utc))
    db.session.add(post)
    db.session.commit()
    return {"success": True, "post": post.to_dict()}


@convert_kwargs_to_snake_case
def deletePost_resolver(obj: Any, info: Any, id: int) -> dict:
    post = db.session.get(Post, id)
    if not post:
        return {
            "success": False,
            "errors": [f"Post with id {id} not found"]
        }

    db.session.delete(post)
    db.session.commit()
    return {"success": True}
