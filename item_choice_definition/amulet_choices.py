import tcod as libtcod
from components.equipment import EquipmentSlots
from components.equippable import Equippable
from entity import Entity


def get_amulet_choice(item_choice, x, y):
    suffix = '-amulet'
    display_icon = 'o'
    display_color = libtcod.gold
    equipment_slot = EquipmentSlots.NECK_1

    disp_name = item_choice.replace(suffix,"")
    item = None

    if item_choice == 'Amulet of Dweomery' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=3)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Amulet of ESP' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Amulet of Life Saving' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Amulet of magical breathing' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Amulet of Reflection' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Amulet of Restful Sleep' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Amulet of Slow Digestion' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Amulet of Strangulation' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Amulet of Unchanging' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Amulet of Versus Poison' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'The Amulet of Zaw' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)

    return item
