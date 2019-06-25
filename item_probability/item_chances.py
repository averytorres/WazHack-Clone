from item_probability.potion_chances import get_potion_chances
from item_probability.scroll_chances import get_scroll_chances
from item_probability.weapon_chances import get_weapon_chances
from item_probability.eye_chances import get_eye_chances
from item_probability.head_armor_chances import get_head_armor_chances
from item_probability.chest_armor_chances import get_chest_armor_chances
from item_probability.shield_chances import get_shield_chances
from item_probability.amulet_chances import get_amulet_chances
from item_probability.finger_chances import get_finger_chances


def get_item_chances(game_map):
    chances = {}

    chances.update(get_potion_chances(game_map))
    chances.update(get_scroll_chances(game_map))

    chances.update(get_weapon_chances(game_map))

    chances.update(get_eye_chances(game_map))
    chances.update(get_head_armor_chances(game_map))
    chances.update(get_chest_armor_chances(game_map))
    chances.update(get_shield_chances(game_map))

    chances.update(get_amulet_chances(game_map))
    chances.update(get_finger_chances(game_map))

    return chances
