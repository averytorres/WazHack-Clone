from item_choice_definition.potion_choices import get_potion_choice
from item_choice_definition.weapon_choices import get_weapon_choice
from item_choice_definition.shield_choices import get_shield_choice
from item_choice_definition.scroll_choices import get_scroll_choice
from item_choice_definition.amulet_choices import get_amulet_choice


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
    else:
        print("ERROR: " + str(item_choice))
    return item
