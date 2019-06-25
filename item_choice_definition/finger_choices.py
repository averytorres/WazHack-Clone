import tcod as libtcod
from components.equipment import EquipmentSlots
from components.equippable import Equippable
from entity import Entity


def get_finger_choice(item_choice, x, y):
    suffix = '-finger'
    display_icon = 'o'
    display_color = libtcod.darker_amber
    equipment_slot = EquipmentSlots.FINGERS

    disp_name = item_choice.replace(suffix,"")
    item = None

    if item_choice == 'Ring of Hunger' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=3)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Ring of Adornment' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Ring of Levitation' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Ring of Invisibility' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Ring of See Invisible' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Ring of Gain Strength' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Ring of Gain Constitution' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Ring of Fire Resistance' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Ring of Magic Regeneration' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Ring of Polymorph' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Ring of Polymorph Control' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Ring of Teleport' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Ring of Teleport Control' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Ring of Regeneration' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)

    return item
