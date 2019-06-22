import tcod as libtcod
from components.equipment import EquipmentSlots
from components.equippable import Equippable
from entity import Entity


def get_backsword_choices(item_choice,wp_en,x,y,disp_name):
    item = None
    if item_choice == 'Scimitar'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=3)
        item = Entity(x, y, '\\', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Sabre'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '\\', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Katana'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '\\', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Werewindle'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '\\', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Grayswandir'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '\\', libtcod.black, disp_name, equippable=equippable_component)
    elif item_choice == 'Katana of Muramasa'+wp_en:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
        item = Entity(x, y, '\\', libtcod.black, disp_name, equippable=equippable_component)

    return item
