import graphene
#from graphene_django.debug import DjangoDebuig
import apps.league.schema


class Query(
        apps.league.schema.Query,
        graphene.ObjectType):
        pass
    #debug = graphene.Field(DjangoDebug, name='__debug')


schema = graphene.Schema(query=Query)
