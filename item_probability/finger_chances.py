from random_utils import from_dungeon_level


def get_finger_chances(game_map):
    wp_en = '-finger'

    chances = {}

    chances.update({'Ring of Hunger' + wp_en: from_dungeon_level([[99, 0]], game_map.dungeon_level)})
    chances.update({'Ring of Adornment' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Ring of Levitation' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Ring of Invisibility' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Ring of See Invisible' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Ring of Gain Strength' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Ring of Gain Constitution' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Ring of Fire Resistance' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Ring of Magic Regeneration' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Ring of Polymorph' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Ring of Polymorph Control' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Ring of Teleport' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Ring of Teleport Control' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Ring of Regeneration' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})

    return chances
