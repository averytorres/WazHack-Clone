from random_utils import from_dungeon_level


def get_axe_chances(game_map):
    wp_en = '-weapon'

    chances = {
        'Pickaxe'+wp_en             : from_dungeon_level([[1, 1]], game_map.dungeon_level),
        'Axe'+wp_en                 : from_dungeon_level([[2, 2]], game_map.dungeon_level),
        'Battle axe' + wp_en        : from_dungeon_level([[3, 3]], game_map.dungeon_level),
        'Massive Axe' + wp_en       : from_dungeon_level([[4, 4]], game_map.dungeon_level),
        'Cleaver' + wp_en           : from_dungeon_level([[5, 5]], game_map.dungeon_level),
        }

    return chances
