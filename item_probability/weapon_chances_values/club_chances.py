from random_utils import from_dungeon_level


def get_club_chances(game_map):
    wp_en = '-weapon'

    chances = {
        'Wooden Club'+wp_en           : from_dungeon_level([[1, 1]], game_map.dungeon_level),
        'Mace'+wp_en                  : from_dungeon_level([[2, 2]], game_map.dungeon_level),
        'Warhammer' + wp_en                   : from_dungeon_level([[3, 3]], game_map.dungeon_level),
        'Morning Star' + wp_en       : from_dungeon_level([[4, 4]], game_map.dungeon_level),
        'Spiked Flail' + wp_en                : from_dungeon_level([[5, 5]], game_map.dungeon_level),
        'Giant Club' + wp_en          : from_dungeon_level([[6, 6]], game_map.dungeon_level),
        'Auger' + wp_en                 : from_dungeon_level([[7, 7]], game_map.dungeon_level),
        'Mjolnir' + wp_en                   : from_dungeon_level([[8, 8]], game_map.dungeon_level),
        }

    return chances
