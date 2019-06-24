from random_utils import from_dungeon_level


def get_chest_armor_chances(game_map):
    wp_en = '-chest_armor'

    chances = {}

    chances.update({'Crystal plate mail' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Dragon Scale Mail' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Dwarvish mithril coat' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Elven mithril coat' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Light chain mail suit' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Suit of banded mail' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Suit of bronze splintmail' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Black dress' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Blue outfit' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Gnome Outfit' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Leather tunic' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Suit of studded leather' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})

    return chances
