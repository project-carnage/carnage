"""Module that represents the Dungeon Schema seeding."""

from typing import Any

from carnage.database.repository.dungeon import (
    DungeonDifficultyRepository,
    DungeonSchemaRepository,
)
from carnage.database.seeds.base import BaseSeed


class DungeonSchemaSeed(BaseSeed):
    """Class that overrides the base seed methods."""

    name: str = "dungeon_schema"
    data: list[dict[str, Any]] = [
        {
            "_dungeon_difficulty": "Easy",
            "name": "Easy dungeon schema",
            "description": "Max dungeon levels 25. Rooms can vary between 5-10.",
            "schema": """\
{
    "levels": {
        {% set number_of_levels = 25 %}
        {% for level in range(number_of_levels) %}
        "{{ level }}": {
            "next": {{ None | tojson if level >= (number_of_levels - 1) else (level + 1) }},
            "previous": {{ None | tojson if level <= 0 else (level - 1) }},
            "rooms":{
                {% set number_of_rooms = 10 %}
                {% set rooms = randint(5, number_of_rooms) %}
                {% for room in range(rooms) %}
                "{{ room }}": {
                    {% set monster = pick_random_monster(monsters) %}
                    "monster": "{{ monster.id }}",
                    "is_boss": {{ monster.is_boss | tojson }},
                    "last_room": {{ true | tojson if room >= (rooms - 1) else false | tojson }}
                },
                {% endfor %}
            }
        },
        {% endfor %}
    }
}
""",
            "version": 1,
        },
        {
            "_dungeon_difficulty": "Medium",
            "name": "Medium dungeon schema",
            "description": "Max dungeon levels 50. Rooms can vary between 5-10.",
            "schema": """\
{
    "levels": {
        {% set number_of_levels = 50 %}
        {% for level in range(number_of_levels) %}
        "{{ level }}": {
            "next": {{ None | tojson if level >= (number_of_levels - 1) else (level + 1) }},
            "previous": {{ None | tojson if level <= 0 else (level - 1) }},
            "rooms":{
                {% set number_of_rooms = 10 %}
                {% set rooms = randint(5, number_of_rooms) %}
                {% for room in range(rooms) %}
                "{{ room }}": {
                    {% set monster = pick_random_monster(monsters) %}
                    "monster": "{{ monster.id }}",
                    "is_boss": {{ monster.is_boss | tojson }},
                    "last_room": {{ true | tojson if room >= (rooms - 1) else false | tojson }}
                },
                {% endfor %}
            }
        },
        {% endfor %}
    }
}
""",
            "version": 1,
        },
        {
            "_dungeon_difficulty": "Hard",
            "name": "Hard dungeon schema",
            "description": "Max dungeon levels 100. Rooms can vary between 5-10.",
            "schema": """\
{
    "levels": {
        {% set number_of_levels = 100 %}
        {% for level in range(number_of_levels) %}
        "{{ level }}": {
            "next": {{ None | tojson if level >= (number_of_levels - 1) else (level + 1) }},
            "previous": {{ None | tojson if level <= 0 else (level - 1) }},
            "rooms":{
                {% set number_of_rooms = 10 %}
                {% set rooms = randint(5, number_of_rooms) %}
                {% for room in range(rooms) %}
                "{{ room }}": {
                    {% set monster = pick_random_monster(monsters) %}
                    "monster": "{{ monster.id }}",
                    "is_boss": {{ monster.is_boss | tojson }},
                    "last_room": {{ true | tojson if room >= (rooms - 1) else false | tojson }}
                },
                {% endfor %}
            }
        },
        {% endfor %}
    }
}
""",
            "version": 1,
        },
        {
            "_dungeon_difficulty": "Nightmare",
            "name": "Nightmare dungeon schema",
            "description": "Max dungeon levels 150. Rooms can vary between 10-20.",
            "schema": """\
{
    "levels": {
        {% set number_of_levels = 150 %}
        {% for level in range(number_of_levels) %}
        "{{ level }}": {
            "next": {{ None | tojson if level >= (number_of_levels - 1) else (level + 1) }},
            "previous": {{ None | tojson if level <= 0 else (level - 1) }},
            "rooms":{
                {% set number_of_rooms = 20 %}
                {% set rooms = randint(10, number_of_rooms) %}
                {% for room in range(rooms) %}
                "{{ room }}": {
                    {% set monster = pick_random_monster(monsters) %}
                    "monster": "{{ monster.id }}",
                    "is_boss": {{ monster.is_boss | tojson }},
                    "last_room": {{ true | tojson if room >= (rooms - 1) else false | tojson }}
                },
                {% endfor %}
            }
        },
        {% endfor %}
    }
}
""",
            "version": 1,
        },
    ]

    def __init__(
        self,
        repository: type[DungeonSchemaRepository] = DungeonSchemaRepository,
    ) -> None:
        """Default class constructor.

        :param repository: The repository used to issue queries.
        """
        super().__init__(repository=repository)
        self.dungeon_difficulty_repository = DungeonDifficultyRepository()

    def seed(self) -> None:
        """Method to seed data into the database."""
        for item in self.data:
            dungeon_difficulty = (
                self.dungeon_difficulty_repository.select_by_level(
                    level=item.get("_dungeon_difficulty", "Easy"),
                )
            )
            # Remove the searchable key
            item.pop("_dungeon_difficulty")
            item.update(
                {
                    "dungeon_difficulty_id": dungeon_difficulty[0].id,
                },
            )

        super().seed()
