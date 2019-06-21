import tcod as libtcod
from components.equipment import EquipmentSlots
from components.equippable import Equippable
from entity import Entity


def get_shield_choice(item_choice, x, y):

    if item_choice == 'shield':
        equippable_component = Equippable(EquipmentSlots.OFF_HAND, defense_bonus=1)
        item = Entity(x, y, '[', libtcod.darker_orange, 'Shield', equippable=equippable_component)
    else:
        equippable_component = Equippable(EquipmentSlots.OFF_HAND, defense_bonus=0)
        item = Entity(x, y, '?', libtcod.darker_orange, 'ERROR SHIELD', equippable=equippable_component)

    return item
