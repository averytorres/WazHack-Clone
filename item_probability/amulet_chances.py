from random_utils import from_dungeon_level


def get_amulet_chances(game_map):
    wp_en = '-amulet'

    chances = {}

    chances.update({'Amulet of Dweomery' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Amulet of ESP' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Amulet of Life Saving' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Amulet of magical breathing' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Amulet of Reflection' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Amulet of Restful Sleep' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Amulet of Slow Digestion' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Amulet of Strangulation' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Amulet of Unchanging' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Amulet of Dweomery' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})
    chances.update({'Amulet of Versus Poison' + wp_en: from_dungeon_level([[1, 1]], game_map.dungeon_level)})

    return chances
