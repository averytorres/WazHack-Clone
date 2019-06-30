

from enum import Enum


class Action(Enum):

    # Keyboard Actions
    NEW_GAME = -1
    LOAD_GAME = 0
    MOVE = 1
    WAIT = 2
    PICKUP = 3
    SHOW_INVENTORY = 4
    SHOW_WEAPON_INVENTORY = 5
    SHOW_ARMOR_INVENTORY = 6
    SHOW_SCROLL_INVENTORY = 7
    SHOW_QUAFF_INVENTORY = 8
    DROP_INVENTORY = 9
    INVENTORY_INDEX = 10
    WEAPON_INVENTORY_INDEX = 11
    ARMOR_INVENTORY_INDEX = 12
    SCROLL_INVENTORY_INDEX = 13
    QUAFF_INVENTORY_INDEX = 14
    TAKE_STAIRS_DOWN = 15
    TAKE_STAIRS_UP = 16
    LEVEL_UP = 17
    SHOW_CHARACTER_SCREEN = 18
    EXIT = 19
    FULLSCREEN = 20

    # Mouse Actions
    LEFT_CLICK = 21
    RIGHT_CLICK = 22
    INVENTORY_INDEX_MOUSE = 23
    WEAPON_INVENTORY_INDEX_MOUSE = 24
    ARMOR_INVENTORY_INDEX_MOUSE = 25
    SCROLL_INVENTORY_INDEX_MOUSE = 26
    QUAFF_INVENTORY_INDEX_MOUSE = 27
    LEVEL_UP_MOUSE = 28
