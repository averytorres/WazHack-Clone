import tcod as libtcod
from components.equipment import EquipmentSlots
from components.equippable import Equippable
from entity import Entity


def get_eye_choice(item_choice, x, y):
    suffix = '-eye'
    display_icon = 'B'
    display_color = libtcod.black
    equipment_slot = EquipmentSlots.EYES

    disp_name = item_choice.replace(suffix,"")
    item = None

    if item_choice == 'Black spectacles' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=3)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Eye mask' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Mummy wrapping' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Jeweller’s monocle' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)

    return item
