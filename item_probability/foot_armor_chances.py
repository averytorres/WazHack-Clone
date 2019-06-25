from random_utils import from_dungeon_level


def get_foot_armor_chances(game_map):
    wp_en = '-foot_armor'

    chances = {}

    chances.update({'Black Boots' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Elven Boots' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Dwarvish Iron Shoes' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Boots of Jumping' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Boots of Levitation' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Speed Boots' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Silk Shoes' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Low Boots' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})

    return chances
