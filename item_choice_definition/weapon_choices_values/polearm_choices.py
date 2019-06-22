import tcod as libtcod
from components.equipment import EquipmentSlots
from components.equippable import Equippable
from entity import Entity


def get_polearm_choices(item_choice,wp_en,x,y,disp_name):
    item = None
    if item_choice == 'Staff'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=3)
        item = Entity(x, y, '_', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Staff of Light'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '_', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Staff of Darkness'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '_', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Spear'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '_', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Staff of Life'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '_', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Staff of Death'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '_', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Red Hot Poker'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '_', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Thyrsus '+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '_', libtcod.black, disp_name, equippable=equippable_component)

    return item
