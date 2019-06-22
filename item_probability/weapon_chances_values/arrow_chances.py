from random_utils import from_dungeon_level


def get_arrow_chances(game_map):
    wp_en = '-weapon'

    chances = {
        'Wooden Arrows'+wp_en   : from_dungeon_level([[1, 1]], game_map.dungeon_level),
        'Copper Arrows'+wp_en   : from_dungeon_level([[2, 2]], game_map.dungeon_level),
        'Iron Arrows' + wp_en   : from_dungeon_level([[2, 2]], game_map.dungeon_level),
        'Steel Arrows' + wp_en  : from_dungeon_level([[2, 2]], game_map.dungeon_level),
        }

    return chances
