
import strawberry
from .esquemas import *

@strawberry.type
class Query:
    ordenes: typing.List[Orden] = strawberry.field(resolver=crear_orden)