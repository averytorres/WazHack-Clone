import tcod as libtcod
from components.equipment import EquipmentSlots
from components.equippable import Equippable
from entity import Entity


def get_bow_choices(item_choice,wp_en,x,y,disp_name):
    item = None
    if item_choice == 'Bow'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=3)
        item = Entity(x, y, 'D', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Recurve Bow'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, 'D', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Longbow'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, 'D', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Composite Bow'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, 'D', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Battle Bow'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, 'D', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Certus'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, 'D', libtcod.black, disp_name, equippable=equippable_component)

    return item
