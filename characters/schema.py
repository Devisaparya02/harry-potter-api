import strawberry
from characters.models import Character, House
from typing import List, Optional

@strawberry.type
class HouseType:
    name: str

@strawberry.type
class CharacterType:
    id: int
    name: str
    house: HouseType

@strawberry.type
class Query:
    @strawberry.field
    def all_characters(self) -> List[CharacterType]:
        return Character.objects.all()

    @strawberry.field
    def all_houses(self) -> List[HouseType]:
        return House.objects.all()

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_character(self, name: str, house_name: str) -> CharacterType:
        house, _ = House.objects.get_or_create(name=house_name)
        character, _ = Character.objects.get_or_create(name=name, house=house)
        return character

    @strawberry.mutation
    def update_character(self, id: int, name: Optional[str] = None, house_name: Optional[str] = None) -> CharacterType:
        try:
            character = Character.objects.get(id=id)
            if name:
                character.name = name
            if house_name:
                house, _ = House.objects.get_or_create(name=house_name)
                character.house = house
            character.save()
            return character
        except Character.DoesNotExist:
            raise Exception("Character not found")

# Register Query and Mutation in Schema
schema = strawberry.Schema(query=Query, mutation=Mutation)
