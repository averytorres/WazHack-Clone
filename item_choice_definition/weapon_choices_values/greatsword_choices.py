import tcod as libtcod
from components.equipment import EquipmentSlots
from components.equippable import Equippable
from entity import Entity


def get_greatsword_choices(item_choice,wp_en,x,y,disp_name):
    item = None
    if item_choice == 'Greatsword'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=3)
        item = Entity(x, y, '|', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Fiery Greatsword'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '|', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Vorpal Blade '+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '|', libtcod.black, disp_name, equippable=equippable_component)

    return item
