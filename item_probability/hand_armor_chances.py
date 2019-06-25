from random_utils import from_dungeon_level


def get_hand_armor_chances(game_map):
    wp_en = '-hand_armor'

    chances = {}

    chances.update({'Hand Warmers' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Gauntlets of Dexterity' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Gauntlets of Fumbling' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Gauntlets of Power' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Black Silk Gloves' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})

    return chances
