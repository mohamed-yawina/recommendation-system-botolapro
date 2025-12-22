from neomodel import (
    StructuredNode, StringProperty, IntegerProperty, DateProperty, 
    DateTimeProperty, RelationshipTo, UniqueIdProperty
)
from datetime import datetime

class Club(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)
    email = StringProperty(unique_index=True) # Linked to Django User
    city = StringProperty()
    league = StringProperty(default="Botola Pro")
    founded = IntegerProperty()

class Quality(StructuredNode):
    uid = UniqueIdProperty()
    label = StringProperty(unique_index=True, required=True)
    category = StringProperty()

class Weakness(StructuredNode):
    uid = UniqueIdProperty()
    label = StringProperty(unique_index=True, required=True)

class Style(StructuredNode):
    uid = UniqueIdProperty()
    type = StringProperty(unique_index=True, required=True)

class Player(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(required=True, index=True)
    age = IntegerProperty()
    position = StringProperty(index=True)
    nationality = StringProperty()
    contract_end = StringProperty() # Changed from DateProperty to handle potential string data
    created_at = DateTimeProperty(default=datetime.now)

    # Relationships
    plays_for = RelationshipTo(Club, 'PLAYS_FOR')
    qualities = RelationshipTo(Quality, 'HAS_QUALITY')
    weaknesses = RelationshipTo(Weakness, 'HAS_WEAKNESS')
    style = RelationshipTo(Style, 'HAS_STYLE')
    similar_to = RelationshipTo('Player', 'SIMILAR_TO')
