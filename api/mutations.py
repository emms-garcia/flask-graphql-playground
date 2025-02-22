from ariadne import convert_kwargs_to_snake_case

from datetime import datetime, timezone

from api import db
from api.models import Post
from typing import Any


@convert_kwargs_to_snake_case
def create_post_resolver(obj: Any, info: Any, title: str, description: str) -> dict:
    try:
        post = Post(title=title, description=description, created_at=datetime.now(timezone.utc))
        db.session.add(post)
        db.session.commit()
        return {"success": True, "post": post.to_dict()}
    except ValueError:
        return {
            "success": False,
            "errors": ["Incorrect date format provided. Date should be in the format dd-mm-yyyy"]
        }
