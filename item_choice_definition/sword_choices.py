import tcod as libtcod
from components.equipment import EquipmentSlots
from components.equippable import Equippable
from entity import Entity


def get_sword_choice(item_choice, x, y):

    if item_choice == 'sword':
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=3)
        item = Entity(x, y, '/', libtcod.sky, 'Sword', equippable=equippable_component)
    else:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=0)
        item = Entity(x, y, '?', libtcod.sky, 'ERROR SWORD', equippable=equippable_component)

    return item
