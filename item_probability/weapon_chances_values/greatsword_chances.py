from random_utils import from_dungeon_level


def get_greatsword_chances(game_map):
    wp_en = '-weapon'

    chances = {
        'Greatsword'+wp_en           : from_dungeon_level([[1, 1]], game_map.dungeon_level),
        'Fiery Greatsword'+wp_en     : from_dungeon_level([[2, 2]], game_map.dungeon_level),
        'Vorpal Blade' + wp_en       : from_dungeon_level([[3, 3]], game_map.dungeon_level),
        }

    return chances
