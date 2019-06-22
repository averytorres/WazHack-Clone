import tcod as libtcod
from components.equipment import EquipmentSlots
from components.equippable import Equippable
from entity import Entity
from item_choice_definition.weapon_choices_values.knive_choices import get_knife_choices
from item_choice_definition.weapon_choices_values.sword_choices import get_sword_choices


def get_weapon_choice(item_choice, x, y):
    wp_en = '-weapon'
    disp_name = item_choice.replace(wp_en,"")
    item = None

    if item is None:
        item = get_knife_choices(item_choice,wp_en,x,y,disp_name)
    if item is None:
        item = get_sword_choices(item_choice, wp_en, x, y, disp_name)
    if item is None:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=0)
        item = Entity(x, y, '?', libtcod.black, 'ERROR WEAPON'+item_choice, equippable=equippable_component)

    return item
