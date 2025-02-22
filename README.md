# flask-graphql-playground

Playing with:
- [Flask](https://flask.palletsprojects.com/en/stable/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Ariadne](https://ariadnegraphql.org/) (GraphQL)

## Set up
- Install [uv](https://github.com/astral-sh/uv)
- Run `uv sync` to install all dependencies
- Run `uv run app.py` to run the API locally
- Check the GraphQL playground at: http://localhost:8080/graphql

## Example queries / mutations

### Create a Post

```graphql
mutation CreatePost {
  createPost(
    title:"My first post"
    description:"This is my first post's description"
  ) {
    post {
      title
      createdAt
      id
    }
    success
    errors
  }
}
```

### Get a Post by ID

Note: Replace `<Post-ID>` below.

```graphql
query {
  getPost(id: <Post-ID>) {
    post {
      createdAt
      title
      description
    }
    success
    errors
  }
}
```

### List all Posts

```graphql
query {
  listPosts {
    success
    errors
    posts {
      id
      createdAt
      title 
      description
    }
  }
}
```

### Delete a Post

Note: Replace `<Post-ID>` below.

```graphql
mutation {
  deletePost(id: <Post-ID>) {
    success
    errors
  }
}
```

## Testing
Run: `uv run pytest -s` to run all tests
