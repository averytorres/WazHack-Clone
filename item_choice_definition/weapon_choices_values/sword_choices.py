import tcod as libtcod
from components.equipment import EquipmentSlots
from components.equippable import Equippable
from entity import Entity


def get_sword_choices(item_choice,wp_en,x,y,disp_name):
    item = None
    if item_choice == 'Orcish Shortsword'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=3)
        item = Entity(x, y, '/', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Shortsword'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '/', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Gladius'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '/', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Dwarvish Shortsword'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '/', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Broadsword'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '/', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Elven Shortsword'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '/', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Longsword'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '/', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Tsurugi'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '/', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Elven Broadsword'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '/', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Bastard Sword'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '/', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Excalibur'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '/', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Tsurugi of Muramasa'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '/', libtcod.black, disp_name, equippable=equippable_component)

    return item
