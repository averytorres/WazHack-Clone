from random_utils import from_dungeon_level


def get_bow_chances(game_map):
    wp_en = '-weapon'

    chances = {
        'Bow'+wp_en                 : from_dungeon_level([[1, 1]], game_map.dungeon_level),
        'Recurve Bow'+wp_en         : from_dungeon_level([[2, 2]], game_map.dungeon_level),
        'Longbow' + wp_en           : from_dungeon_level([[3, 3]], game_map.dungeon_level),
        'Composite Bow' + wp_en     : from_dungeon_level([[4, 4]], game_map.dungeon_level),
        'Battle Bow' + wp_en        : from_dungeon_level([[5, 5]], game_map.dungeon_level),
        'Certus' + wp_en            : from_dungeon_level([[6, 6]], game_map.dungeon_level),
        }

    return chances
