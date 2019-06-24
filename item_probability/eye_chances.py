from random_utils import from_dungeon_level


def get_eye_chances(game_map):
    wp_en = '-eye'

    chances = {}

    chances.update({'Black spectacles' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Eye mask' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Jeweller’s monocle' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Mummy wrapping' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})

    return chances
