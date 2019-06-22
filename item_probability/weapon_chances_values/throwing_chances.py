from random_utils import from_dungeon_level


def get_throwing_chances(game_map):
    wp_en = '-weapon'

    chances = {
        'Shuriken'+wp_en            : from_dungeon_level([[1, 1]], game_map.dungeon_level),
        'A boulder'+wp_en           : from_dungeon_level([[2, 2]], game_map.dungeon_level),
        }

    return chances
