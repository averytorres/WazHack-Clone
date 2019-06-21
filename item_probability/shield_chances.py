from random_utils import from_dungeon_level


def get_shield_chances(game_map):
    chances = {
            'shield': from_dungeon_level([[15, 8]], game_map.dungeon_level),
        }

    return chances
