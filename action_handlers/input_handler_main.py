import tcod as libtcod

from game_states import GameStates
from menu_info.menu_details import get_menu_title, get_menu_width, get_main_menu_key, get_menu_height
from action_handlers.weapon_inventory_index_ih import get_weapon_inventory_index_options
from action_handlers.armor_inventory_index_ih import get_armor_inventory_index_options
from action_handlers.scroll_inventory_index_ih import get_scroll_inventory_index_options
from action_handlers.quaff_inventory_index_ih import get_quaff_inventory_index_options
from action_handlers.level_up_ih import get_level_up_index_options
from action_handlers.level_up_ih import get_level_up_key
from action_consumer.available_actions_enum import AvailableActionsEnum
import math


def handle_keys(key,mouse,game_state):
    if game_state == GameStates.PLAYERS_TURN:
        return handle_player_turn_keys(key,mouse)
    elif game_state == GameStates.PLAYER_DEAD:
        return handle_player_dead_keys(key,mouse)
    elif game_state == GameStates.TARGETING:
        return handle_targeting_keys(key,mouse)
    elif game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY):
        return handle_inventory_keys(key,mouse)
    elif game_state == GameStates.SHOW_WEAPON_INVENTORY:
        return handle_weapon_inventory_keys(key,mouse)
    elif game_state == GameStates.SHOW_ARMOR_INVENTORY:
        return handle_armor_inventory_keys(key,mouse)
    elif game_state == GameStates.SHOW_SCROLL_INVENTORY:
        return handle_scroll_inventory_keys(key,mouse)
    elif game_state == GameStates.SHOW_QUAFF_INVENTORY:
        return handle_quaff_inventory_keys(key,mouse)
    elif game_state == GameStates.LEVEL_UP:
        return handle_level_up_menu(key,mouse)
    elif game_state == GameStates.CHARACTER_SCREEN:
        return handle_character_screen(key,mouse)

    return {}


def handle_player_turn_keys(key,mouse):
    key_char = chr(key.c)

    # Movement keys
    if key.vk == libtcod.KEY_UP or key_char == 'k':
        return {AvailableActionsEnum.MOVE: (0, -1)}
    elif key.vk == libtcod.KEY_DOWN or key_char == 'j':
        return {AvailableActionsEnum.MOVE: (0, 1)}
    elif key.vk == libtcod.KEY_LEFT or key_char == 'h':
        return {AvailableActionsEnum.MOVE: (-1, 0)}
    elif key.vk == libtcod.KEY_RIGHT or key_char == 'l':
        return {AvailableActionsEnum.MOVE: (1, 0)}
    elif key_char == 'y':
        return {AvailableActionsEnum.MOVE: (-1, -1)}
    elif key_char == 'u':
        return {AvailableActionsEnum.MOVE: (1, -1)}
    elif key_char == 'b':
        return {AvailableActionsEnum.MOVE: (-1, 1)}
    elif key_char == 'n':
        return {AvailableActionsEnum.MOVE: (1, 1)}
    elif key.vk == libtcod.KEY_TAB:
        return {AvailableActionsEnum.WAIT: True}

    if key_char == 'g':
        return {AvailableActionsEnum.PICKUP: True}

    elif key_char == 'i':
        return {AvailableActionsEnum.SHOW_INVENTORY: True}

    elif key_char == 'w':
        return {AvailableActionsEnum.SHOW_WEAPON_INVENTORY: True}

    elif key_char == 'a':
        return {AvailableActionsEnum.SHOW_ARMOR_INVENTORY: True}

    elif key_char == 'r':
        return {AvailableActionsEnum.SHOW_SCROLL_INVENTORY: True}

    elif key_char == 'q':
        return {AvailableActionsEnum.SHOW_QUAFF_INVENTORY: True}

    elif key_char == 'd':
        return {AvailableActionsEnum.DROP_INVENTORY: True}

    elif key_char == '.':
        return {AvailableActionsEnum.TAKE_STAIRS_DOWN: True}

    elif key_char == ',':
        return {AvailableActionsEnum.TAKE_STAIRS_UP: True}

    elif key_char == 'c':
        return {AvailableActionsEnum.SHOW_CHARACTER_SCREEN: True}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {AvailableActionsEnum.FULLSCREEN: True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {AvailableActionsEnum.EXIT: True}

    # No key was pressed
    return {}


def handle_targeting_keys(key,mouse):
    if key.vk == libtcod.KEY_ESCAPE:
        return {AvailableActionsEnum.EXIT: True}

    return {}


def handle_player_dead_keys(key,mouse):
    key_char = chr(key.c)

    if key_char == 'i':
        return {AvailableActionsEnum.SHOW_INVENTORY: True}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {AvailableActionsEnum.FULLSCREEN: True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the menu
        return {AvailableActionsEnum.EXIT: True}

    return {}


def handle_inventory_keys(key,mouse):

    index = key.c - ord('a')
    if index >= 0:
        return {AvailableActionsEnum.INVENTORY_INDEX: index}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {AvailableActionsEnum.FULLSCREEN: True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the menu
        return {AvailableActionsEnum.EXIT: True}

    return {}

def handle_inventory_mouse(game_state,options,key, mouse,constants,con,player):

    index = determine_menu_index(game_state,options,con,constants,player,mouse)

    if index is not None:
        return {AvailableActionsEnum.INVENTORY_INDEX_MOUSE: index}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {AvailableActionsEnum.FULLSCREEN: True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the menu
        return {AvailableActionsEnum.EXIT: True}

    return {}


def handle_weapon_inventory_keys(key,mouse):

    index = key.c - ord('a')
    if index >= 0:
        return {AvailableActionsEnum.WEAPON_INVENTORY_INDEX: index}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {AvailableActionsEnum.FULLSCREEN: True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the menu
        return {AvailableActionsEnum.EXIT: True}

    return {}


def handle_weapon_inventory_mouse(game_state,options,key, mouse,constants,con,player):

    index = determine_menu_index(game_state,options, con, constants, player, mouse)
    if index is not None:
        return {AvailableActionsEnum.WEAPON_INVENTORY_INDEX_MOUSE: index}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {AvailableActionsEnum.FULLSCREEN: True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the menu
        return {AvailableActionsEnum.EXIT: True}

    return {}


def handle_armor_inventory_keys(key,mouse):
    index = key.c - ord('a')
    if index >= 0:
        return {AvailableActionsEnum.ARMOR_INVENTORY_INDEX: index}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {AvailableActionsEnum.FULLSCREEN: True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the menu
        return {AvailableActionsEnum.EXIT: True}

    return {}


def handle_armor_inventory_mouse(game_state,options,key, mouse,constants,con,player):

    index = determine_menu_index(game_state,options, con, constants, player, mouse)
    if index is not None:
        return {AvailableActionsEnum.ARMOR_INVENTORY_INDEX_MOUSE: index}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {AvailableActionsEnum.FULLSCREEN: True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the menu
        return {AvailableActionsEnum.EXIT: True}

    return {}


def handle_scroll_inventory_keys(key,mouse):

    index = key.c - ord('a')
    if index >= 0:
        return {AvailableActionsEnum.SCROLL_INVENTORY_INDEX: index}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {AvailableActionsEnum.FULLSCREEN: True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the menu
        return {AvailableActionsEnum.EXIT: True}

    return {}


def handle_scroll_inventory_mouse(game_state,options,key, mouse,constants,con,player):

    index = determine_menu_index(game_state,options, con, constants, player, mouse)
    if index is not None:
        return {AvailableActionsEnum.SCROLL_INVENTORY_INDEX_MOUSE: index}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {AvailableActionsEnum.FULLSCREEN: True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the menu
        return {AvailableActionsEnum.EXIT: True}

    return {}


def handle_quaff_inventory_keys(key,mouse):

    index = key.c - ord('a')
    if index >= 0:
        return {AvailableActionsEnum.QUAFF_INVENTORY_INDEX: index}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {AvailableActionsEnum.FULLSCREEN: True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the menu
        return {AvailableActionsEnum.EXIT: True}

    return {}


def handle_quaff_inventory_mouse(game_state,options,key, mouse,constants,con,player):

    index = determine_menu_index(game_state,options, con, constants, player, mouse)
    if index is not None:
        return {AvailableActionsEnum.QUAFF_INVENTORY_INDEX_MOUSE: index}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {AvailableActionsEnum.FULLSCREEN: True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the menu
        return {AvailableActionsEnum.EXIT: True}

    return {}


def handle_main_menu(key,mouse,game_state, options, con, constants, player):
    if key.pressed == False:
        index = determine_main_menu_index(game_state, options, con, constants, player, mouse)
        return get_main_menu_key(index)
    else:
        if key.vk == libtcod.KEY_ESCAPE:
            return {AvailableActionsEnum.EXIT: True}
        else:
            index = key.c - ord('a')
            return get_main_menu_key(index)

    return {}


def handle_level_up_menu(key,mouse):
    if key:
        index = key.c - ord('a')
        if index is not None and index >=0:
            return {AvailableActionsEnum.LEVEL_UP: get_level_up_key(index)}

    return {}


def handle_level_up_menu_mouse(game_state,options,key, mouse,constants,con,player):
    index = determine_menu_index(game_state,options, con, constants, player, mouse)
    if index is not None:
        return {AvailableActionsEnum.LEVEL_UP_MOUSE: get_level_up_key(index)}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {AvailableActionsEnum.FULLSCREEN: True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the menu
        return {AvailableActionsEnum.EXIT: True}

    return {}


def handle_character_screen(key,mouse):
    if key.vk == libtcod.KEY_ESCAPE:
        return {AvailableActionsEnum.EXIT: True}

    return {}


def handle_mouse(key,mouse,game_state,constants,con,player):
    (x, y) = (mouse.cx, mouse.cy)

    if mouse.lbutton_pressed:
        if game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY):
            options = player.inventory.items
            return handle_inventory_mouse(game_state,options,key, mouse,constants,con,player)
        elif game_state == GameStates.SHOW_WEAPON_INVENTORY:
            options = get_weapon_inventory_index_options(player)
            return handle_weapon_inventory_mouse(game_state,options,key, mouse,constants,con,player)
        elif game_state == GameStates.SHOW_ARMOR_INVENTORY:
            options = get_armor_inventory_index_options(player)
            return handle_armor_inventory_mouse(game_state,options,key, mouse,constants,con,player)
        elif game_state == GameStates.SHOW_SCROLL_INVENTORY:
            options = get_scroll_inventory_index_options(player)
            return handle_scroll_inventory_mouse(game_state,options,key, mouse,constants,con,player)
        elif game_state == GameStates.SHOW_QUAFF_INVENTORY:
            options = get_quaff_inventory_index_options(player)
            return handle_quaff_inventory_mouse(game_state,options,key, mouse,constants,con,player)
        elif game_state == GameStates.LEVEL_UP:
            options = get_level_up_index_options(player)
            return handle_level_up_menu_mouse(game_state,options,key, mouse,constants,con,player)
        else:
            return {AvailableActionsEnum.LEFT_CLICK: (x, y)}
    elif mouse.rbutton_pressed:
        return {AvailableActionsEnum.RIGHT_CLICK: (x, y)}

    return {}


def determine_menu_index(menu_name,options,con,constants,player,mouse):
    inventory_title = get_menu_title(menu_name)
    menu_width =  get_menu_width(menu_name)

    if inventory_title == "":
        header_height = 0
    else:
        header_height = libtcod.console_get_height_rect(con, 0, 0, menu_width,
                                                    constants['screen_height'], inventory_title)

    height = len(options) + header_height

    x = constants['screen_width'] / 2 - 50 / 2
    y = constants['screen_height'] / 2 - height / 2

    # Compute x and y offsets to convert console position to menu position
    x_offset = x  # x is the left edge of the menu
    y_offset = y + (header_height - (header_height / 5))  # The top edge of the menu

    (menu_x, menu_y) = (mouse.cx - x_offset, mouse.cy - y_offset)
    if menu_x >= 0 and menu_x < menu_width and menu_y >= 0 and menu_y < height - header_height:
        menu_y = int(math.ceil(menu_y)) - 1
        return menu_y
    else:
        return menu_y


def determine_main_menu_index(menu_name,options,con,constants,player,mouse):
    inventory_title = get_menu_title(menu_name)
    menu_width =  get_menu_width(menu_name)

    if inventory_title == "":
        header_height = 0
    else:
        header_height = libtcod.console_get_height_rect(con, 0, 0, menu_width,
                                                    get_menu_height(constants['screen_height']), inventory_title)

    height = len(options) + header_height

    x = get_menu_height(constants['screen_height']) / 2 - 50 / 2
    y = get_menu_height(constants['screen_height']) / 2 - height / 2

    # Compute x and y offsets to convert console position to menu position
    x_offset = x  # x is the left edge of the menu
    y_offset = y + (header_height - (header_height / 5)) - 1 # The top edge of the menu

    print("y_offset: " + str(y_offset))
    (menu_x, menu_y) = (mouse.cx - x_offset, mouse.cy - y_offset)
    if menu_x >= 0 and menu_x < menu_width and menu_y >= 0 and menu_y < height - header_height:
        menu_y = int(math.ceil(menu_y)) - 1
        return menu_y
    else:
        return menu_y