from graphene_sqlalchemy.fields import SQLAlchemyConnectionField
from graphene import ObjectType, relay
from .type import Korea, Inter

class Query(ObjectType):
    
    node = relay.Node.Field()

    all_korea = SQLAlchemyConnectionField(Korea.connection)
    all_inter = SQLAlchemyConnectionField(Inter.connection)