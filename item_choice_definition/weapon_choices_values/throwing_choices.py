import tcod as libtcod
from components.equipment import EquipmentSlots
from components.equippable import Equippable
from entity import Entity


def get_throwing_choices(item_choice,wp_en,x,y,disp_name):
    item = None
    if item_choice == 'Shuriken'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=3)
        item = Entity(x, y, '*', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'A boulder'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '*', libtcod.black, disp_name, equippable=equippable_component)

    return item
