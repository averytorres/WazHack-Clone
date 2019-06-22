from random_utils import from_dungeon_level


def get_backsword_chances(game_map):
    wp_en = '-weapon'

    chances = {
        'Scimitar'+wp_en                : from_dungeon_level([[1, 1]], game_map.dungeon_level),
        'Sabre'+wp_en                   : from_dungeon_level([[2, 2]], game_map.dungeon_level),
        'Katana' + wp_en                : from_dungeon_level([[3, 3]], game_map.dungeon_level),
        'Werewindle' + wp_en            : from_dungeon_level([[4, 4]], game_map.dungeon_level),
        'Grayswandir' + wp_en           : from_dungeon_level([[5, 5]], game_map.dungeon_level),
        'Katana of Muramasa' + wp_en    : from_dungeon_level([[6, 6]], game_map.dungeon_level),
        }

    return chances
