from random_utils import from_dungeon_level


def get_head_armor_chances(game_map):
    wp_en = '-head_armor'

    chances = {}

    chances.update({'Cornuthaum' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Crested helm' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Crown' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Dwarvish helm' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Engineer’s cap' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Green Headband' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Helm of brilliance' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Orcish helm' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})

    return chances
