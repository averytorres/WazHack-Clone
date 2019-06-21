from random_utils import from_dungeon_level


def get_scroll_chances(game_map):
    chances = {
            'lightning_scroll': from_dungeon_level([[25, 4]], game_map.dungeon_level),
            'fireball_scroll': from_dungeon_level([[25, 6]], game_map.dungeon_level),
            'confusion_scroll': from_dungeon_level([[10, 2]], game_map.dungeon_level)
        }

    return chances
