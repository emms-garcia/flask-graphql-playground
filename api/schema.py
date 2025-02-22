from ariadne import gql, make_executable_schema, ObjectType, snake_case_fallback_resolvers

from api.mutations import create_post_resolver
from api.resolvers import getPost_resolver, listPosts_resolver


type_defs = gql("""
    schema {
        query: Query
        mutation: Mutation
    }

    type Post {
        id: Int!
        title: String!
        description: String!
        createdAt: String!
    }

    type PostResult {
        success: Boolean!
        errors: [String]
        post: Post
    }

    type PostsResult {
        success: Boolean!
        errors: [String]
        posts: [Post]
    }

    type Query {
        listPosts: PostsResult!
        getPost(id: Int!): PostResult!
    }
                
    type Mutation {
        createPost(title: String!, description: String!, createdAt: String): PostResult!
    }
""")
query = ObjectType("Query")
query.set_field("getPost", getPost_resolver)
query.set_field("listPosts", listPosts_resolver)

mutation = ObjectType("Mutation")
mutation.set_field("createPost", create_post_resolver)

schema = make_executable_schema(type_defs, query, mutation, snake_case_fallback_resolvers)
