from item_probability.weapon_chances_values.knive_chances import get_knive_chances
from item_probability.weapon_chances_values.sword_chances import get_sword_chances


def get_weapon_chances(game_map):
    chances = {}

    chances.update(get_knive_chances(game_map))
    chances.update(get_sword_chances(game_map))

    return chances
