import graphene
import noteapp.schema


class Query(noteapp.schema.Query, graphene.ObjectType):
    pass


class Mutation(noteapp.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
