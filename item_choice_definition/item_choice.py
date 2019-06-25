from item_choice_definition.potion_choices import get_potion_choice
from item_choice_definition.weapon_choices import get_weapon_choice
from item_choice_definition.shield_choices import get_shield_choice
from item_choice_definition.scroll_choices import get_scroll_choice
from item_choice_definition.amulet_choices import get_amulet_choice
from item_choice_definition.chest_armor_choices import get_chest_armor_choice
from item_choice_definition.head_armor_choices import get_head_armor_choice
from item_choice_definition.eye_choices import get_eye_choice
from item_choice_definition.finger_choices import get_finger_choice


def get_item_choice(item_choice, x, y):

    if 'POTION'.upper() in item_choice.upper():
        item = get_potion_choice(item_choice, x, y)

    elif 'SCROLL'.upper() in item_choice.upper():
        item = get_scroll_choice(item_choice, x, y)

    elif 'WEAPON'.upper() in item_choice.upper():
        item = get_weapon_choice(item_choice, x, y)

    elif 'SHIELD'.upper() in item_choice.upper():
        item = get_shield_choice(item_choice, x, y)

    elif 'AMULET'.upper() in item_choice.upper():
        item = get_amulet_choice(item_choice, x, y)

    elif 'EYE'.upper() in item_choice.upper():
        item = get_eye_choice(item_choice, x, y)

    elif 'HEAD_ARMOR'.upper() in item_choice.upper():
        item = get_head_armor_choice(item_choice, x, y)

    elif 'CHEST_ARMOR'.upper() in item_choice.upper():
        item = get_chest_armor_choice(item_choice, x, y)

    elif 'FINGER'.upper() in item_choice.upper():
        item = get_finger_choice(item_choice, x, y)

    else:
        print("ERROR: " + str(item_choice))

    return item
