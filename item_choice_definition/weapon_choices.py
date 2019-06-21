import tcod as libtcod
from components.equipment import EquipmentSlots
from components.equippable import Equippable
from entity import Entity


def get_weapon_choice(item_choice, x, y):
    wp_en = '-weapon'
    disp_name = item_choice.replace(wp_en,"")
    if item_choice == 'Sickle'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=3)
        item = Entity(x, y, ',', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Orcish Dagger'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, ',', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Dagger'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, ',', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Athame'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, ',', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Kris Knife'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, ',', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Grimtooth'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, ',', libtcod.black, disp_name, equippable=equippable_component)
    else:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=0)
        item = Entity(x, y, '?', libtcod.black, 'ERROR WEAPON', equippable=equippable_component)

    return item
