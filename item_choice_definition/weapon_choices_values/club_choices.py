import tcod as libtcod
from components.equipment import EquipmentSlots
from components.equippable import Equippable
from entity import Entity


def get_club_choices(item_choice,wp_en,x,y,disp_name):
    item = None
    if item_choice == 'Wooden Club'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=3)
        item = Entity(x, y, '!', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Mace'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '!', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Warhammer'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '!', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Morning Star'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '!', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Spiked Flail'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '!', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Giant Club'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '!', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Auger'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '!', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Mjolnir'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '!', libtcod.black, disp_name, equippable=equippable_component)


    return item
