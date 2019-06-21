from random_utils import from_dungeon_level


def get_sword_chances(game_map):
    chances = {
            'sword': from_dungeon_level([[5, 4]], game_map.dungeon_level),
        }

    return chances
