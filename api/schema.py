from ariadne import gql, make_executable_schema, ObjectType, snake_case_fallback_resolvers

from api.mutations import createPost_resolver, deletePost_resolver
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

    type DeletePostResult {
        success: Boolean!
        errors: [String]
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
        deletePost(id: Int!): DeletePostResult!
    }
""")
query = ObjectType("Query")
query.set_field("getPost", getPost_resolver)
query.set_field("listPosts", listPosts_resolver)

mutation = ObjectType("Mutation")
mutation.set_field("createPost", createPost_resolver)
mutation.set_field("deletePost", deletePost_resolver)

schema = make_executable_schema(type_defs, query, mutation, snake_case_fallback_resolvers)
