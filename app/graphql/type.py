from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from covid.database.models import CovidKorea, CovidInter

class Korea(SQLAlchemyObjectType):
    class Meta:
        model = CovidKorea
        interfaces = (relay.Node, )

class Inter(SQLAlchemyObjectType):
    class Meta:
        model = CovidInter
        interfaces = (relay.Node, )