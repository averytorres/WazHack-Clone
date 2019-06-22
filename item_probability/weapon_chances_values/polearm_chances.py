from random_utils import from_dungeon_level


def get_polearm_chances(game_map):
    wp_en = '-weapon'

    chances = {
        'Staff'+wp_en                   : from_dungeon_level([[1, 1]], game_map.dungeon_level),
        'Staff of Light'+wp_en          : from_dungeon_level([[2, 2]], game_map.dungeon_level),
        'Staff of Darkness' + wp_en     : from_dungeon_level([[3, 3]], game_map.dungeon_level),
        'Spear' + wp_en                 : from_dungeon_level([[4, 4]], game_map.dungeon_level),
        'Staff of Life' + wp_en         : from_dungeon_level([[5, 5]], game_map.dungeon_level),
        'Staff of Death' + wp_en        : from_dungeon_level([[6, 6]], game_map.dungeon_level),
        'Red Hot Poker' + wp_en         : from_dungeon_level([[7, 7]], game_map.dungeon_level),
        'Thyrsus' + wp_en               : from_dungeon_level([[8, 9]], game_map.dungeon_level),
        }

    return chances
