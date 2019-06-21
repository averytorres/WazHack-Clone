from random_utils import from_dungeon_level


def get_knive_chances(game_map):
    wp_en = '-weapon'
    chances = {
        'Sickle'+wp_en          : from_dungeon_level([[1, 1]], game_map.dungeon_level),
        'Orcish Dagger'+wp_en    : from_dungeon_level([[2, 2]], game_map.dungeon_level),
        'Dagger' + wp_en        : from_dungeon_level([[3, 3]], game_map.dungeon_level),
        'Elven Dagger' + wp_en   : from_dungeon_level([[4, 4]], game_map.dungeon_level),
        'Athame' + wp_en        : from_dungeon_level([[5, 5]], game_map.dungeon_level),
        'Kris Knife' + wp_en     : from_dungeon_level([[6, 6]], game_map.dungeon_level),
        'Grimtooth' + wp_en     : from_dungeon_level([[7, 7]], game_map.dungeon_level),
        }

    return chances
