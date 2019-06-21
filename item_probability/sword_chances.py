from random_utils import from_dungeon_level
from item_choice_definition.weapon_chances.knive_chances import get_knive_chances

def get_sword_chances(game_map):
    chances = {}

    chances.update(get_knive_chances(game_map))

    return chances
