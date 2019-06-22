from item_probability.potion_chances import get_potion_chances
from item_probability.scroll_chances import get_scroll_chances
from item_probability.weapon_chances import get_sword_chances
from item_probability.shield_chances import get_shield_chances


def get_item_chances(game_map):
    chances = {}

    potion_chances = get_potion_chances(game_map)
    scroll_chances = get_scroll_chances(game_map)

    sword_chances = get_sword_chances(game_map)
    shield_chances = get_shield_chances(game_map)

    chances.update(potion_chances)
    chances.update(scroll_chances)

    chances.update(sword_chances)
    chances.update(shield_chances)

    return chances
