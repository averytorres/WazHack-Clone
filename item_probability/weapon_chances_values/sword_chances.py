from random_utils import from_dungeon_level


def get_sword_chances(game_map):
    wp_en = '-weapon'

    chances = {
        'Orcish Shortsword'+wp_en           : from_dungeon_level([[1, 1]], game_map.dungeon_level),
        'Shortsword'+wp_en                  : from_dungeon_level([[2, 2]], game_map.dungeon_level),
        'Gladius' + wp_en                   : from_dungeon_level([[3, 3]], game_map.dungeon_level),
        'Dwarvish Shortsword' + wp_en       : from_dungeon_level([[4, 4]], game_map.dungeon_level),
        'Broadsword' + wp_en                : from_dungeon_level([[5, 5]], game_map.dungeon_level),
        'Elven Shortsword' + wp_en          : from_dungeon_level([[6, 6]], game_map.dungeon_level),
        'Longsword' + wp_en                 : from_dungeon_level([[7, 7]], game_map.dungeon_level),
        'Tsurugi' + wp_en                   : from_dungeon_level([[8, 9]], game_map.dungeon_level),
        'Elven Broadsword' + wp_en          : from_dungeon_level([[9, 9]], game_map.dungeon_level),
        'Bastard Sword' + wp_en             : from_dungeon_level([[10, 10]], game_map.dungeon_level),
        'Excalibur' + wp_en                 : from_dungeon_level([[11, 11]], game_map.dungeon_level),
        'Tsurugi of Muramasa' + wp_en       : from_dungeon_level([[12, 12]], game_map.dungeon_level),
        }

    return chances
