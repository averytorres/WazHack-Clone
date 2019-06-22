import tcod as libtcod

from game_states import GameStates
from menu_info.menu_details import get_menu_title, get_menu_width
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
    elif game_state == GameStates.SHOW_SCROLL_INVENTORY:
        return handle_scroll_inventory_keys(key,mouse)
    elif game_state == GameStates.LEVEL_UP:
        return handle_level_up_menu(key,mouse)
    elif game_state == GameStates.CHARACTER_SCREEN:
        return handle_character_screen(key,mouse)

    return {}


def handle_player_turn_keys(key,mouse):
    key_char = chr(key.c)

    # Movement keys
    if key.vk == libtcod.KEY_UP or key_char == 'k':
        return {'move': (0, -1)}
    elif key.vk == libtcod.KEY_DOWN or key_char == 'j':
        return {'move': (0, 1)}
    elif key.vk == libtcod.KEY_LEFT or key_char == 'h':
        return {'move': (-1, 0)}
    elif key.vk == libtcod.KEY_RIGHT or key_char == 'l':
        return {'move': (1, 0)}
    elif key_char == 'y':
        return {'move': (-1, -1)}
    elif key_char == 'u':
        return {'move': (1, -1)}
    elif key_char == 'b':
        return {'move': (-1, 1)}
    elif key_char == 'n':
        return {'move': (1, 1)}
    elif key.vk == libtcod.KEY_TAB:
        return {'wait': True}

    if key_char == 'g':
        return {'pickup': True}

    elif key_char == 'i':
        return {'show_inventory': True}

    elif key_char == 'w':
        return {'show_weapon_inventory': True}

    elif key_char == 'r':
        return {'show_scroll_inventory': True}

    elif key_char == 'd':
        return {'drop_inventory': True}

    elif key_char == '.':
        return {'take_stairs_down': True}

    elif key_char == ',':
        return {'take_stairs_up': True}

    elif key_char == 'c':
        return {'show_character_screen': True}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}

    # No key was pressed
    return {}


def handle_targeting_keys(key,mouse):
    if key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}

    return {}


def handle_player_dead_keys(key,mouse):
    key_char = chr(key.c)

    if key_char == 'i':
        return {'show_inventory': True}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the menu
        return {'exit': True}

    return {}


def handle_inventory_keys(key,mouse):

    index = key.c - ord('a')
    if index >= 0:
        return {'inventory_index': index}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the menu
        return {'exit': True}

    return {}

def handle_inventory_mouse(game_state,key, mouse,constants,con,player):

    index = determine_menu_index(game_state,con,constants,player,mouse)

    if index is not None:
        return {'inventory_index': index}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the menu
        return {'exit': True}

    return {}


def handle_weapon_inventory_keys(key,mouse):

    index = key.c - ord('a')

    if index >= 0:
        return {'weapon_inventory_index': index}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the menu
        return {'exit': True}

    return {}


def handle_weapon_inventory_mouse(game_state,key, mouse,constants,con,player):

    index = determine_menu_index(game_state, con, constants, player, mouse)
    if index is not None:
        return {'weapon_inventory_index': index}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the menu
        return {'exit': True}

    return {}


def handle_scroll_inventory_keys(key,mouse):

    index = key.c - ord('a')
    if index >= 0:
        return {'scroll_inventory_index': index}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the menu
        return {'exit': True}

    return {}


def handle_main_menu(key,mouse):
    key_char = chr(key.c)

    if key_char == 'a':
        return {'new_game': True}
    elif key_char == 'b':
        return {'load_game': True}
    elif key_char == 'c' or key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}

    return {}


def handle_level_up_menu(key,mouse):
    if key:
        key_char = chr(key.c)

        if key_char == 'a':
            return {'level_up': 'hp'}
        elif key_char == 'b':
            return {'level_up': 'str'}
        elif key_char == 'c':
            return {'level_up': 'def'}

    return {}


def handle_character_screen(key,mouse):
    if key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}

    return {}


def handle_mouse(key,mouse,game_state,constants,con,player):
    (x, y) = (mouse.cx, mouse.cy)

    if mouse.lbutton_pressed:
        if game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY):
            return handle_inventory_mouse(game_state,key, mouse,constants,con,player)
        elif game_state == GameStates.SHOW_WEAPON_INVENTORY:
            return handle_weapon_inventory_mouse(game_state,key, mouse,constants,con,player)
        else:
            return {'left_click': (x, y)}
    elif mouse.rbutton_pressed:
        return {'right_click': (x, y)}

    return {}


def determine_menu_index(menu_name,con,constants,player,mouse):
    inventory_title = get_menu_title(menu_name)
    header_height = libtcod.console_get_height_rect(con, 0, 0, get_menu_width(menu_name),
                                                    constants['screen_height'], inventory_title)
    options = player.inventory.items
    height = len(options) + header_height

    x = constants['screen_width'] / 2 - 50 / 2
    y = constants['screen_height'] / 2 - height / 2

    # Compute x and y offsets to convert console position to menu position
    x_offset = x  # x is the left edge of the menu
    y_offset = y + (header_height - (header_height / 5))  # The top edge of the menu

    (menu_x, menu_y) = (mouse.cx - x_offset, mouse.cy - y_offset)
    menu_y = int(math.ceil(menu_y)) - 1
    index = int(menu_y)

    return index