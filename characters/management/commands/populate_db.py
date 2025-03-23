from django.core.management.base import BaseCommand
from characters.models import Character, House

class Command(BaseCommand):
    help = "Populate the database with character data"

    def handle(self, *args, **kwargs):
        # Ensure House instances exist
        gryffindor, _ = House.objects.get_or_create(name="Gryffindor")
        slytherin, _ = House.objects.get_or_create(name="Slytherin")

        characters_data = [
            {"name": "Harry Potter", "house": gryffindor, "role": "Student", "wand": "Holly, Phoenix Feather", "patronus": "Stag"},
            {"name": "Hermione Granger", "house": gryffindor, "role": "Student", "wand": "Vine, Dragon Heartstring", "patronus": "Otter"},
            {"name": "Ron Weasley", "house": gryffindor, "role": "Student", "wand": "Willow, Unicorn Hair", "patronus": "Jack Russell Terrier"},
            {"name": "Albus Dumbledore", "house": gryffindor, "role": "Professor", "wand": "Elder, Thestral Tail Hair", "patronus": "Phoenix"},
            {"name": "Severus Snape", "house": slytherin, "role": "Professor", "wand": "Unknown", "patronus": "Doe"},
        ]

        for char_data in characters_data:
            character, created = Character.objects.get_or_create(
                name=char_data["name"],
                role=char_data["role"],
                defaults={
                    "house": char_data["house"],  # Now assigns a House instance
                    "wand": char_data["wand"],
                    "patronus": char_data["patronus"],
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Added: {character.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Skipped (Already exists): {character.name}"))
