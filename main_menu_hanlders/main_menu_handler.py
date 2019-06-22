import tcod as libtcod

from game_states import GameStates
from action_handlers.input_handler_main import handle_main_menu
from loader_functions.data_loaders import load_game
from menus import main_menu, message_box
from loader_functions.initialize_new_game import get_game_variables


def handle_main_menu_operations(con,main_menu_background_image,constants,show_load_error_message,key,mouse,player,entities,game_map,message_log,game_state,show_main_menu):
    exit_game_break = False
    main_menu(con, main_menu_background_image, constants['screen_width'],
              constants['screen_height'], constants['window_title'],key, mouse,game_state)

    if show_load_error_message:
        message_box(con, 'No save game to load', 50, constants['screen_width'], constants['screen_height'])

    libtcod.console_flush()

    action = handle_main_menu(key,mouse)

    new_game = action.get('new_game')
    load_saved_game = action.get('load_game')
    exit_game = action.get('exit')

    if show_load_error_message and (new_game or load_saved_game or exit_game):
        show_load_error_message = False
    elif new_game:
        player, entities, game_map, message_log, game_state = get_game_variables(constants)
        game_state = GameStates.PLAYERS_TURN

        show_main_menu = False
    elif load_saved_game:
        try:
            player, entities, game_map, message_log, game_state = load_game()
            show_main_menu = False
        except FileNotFoundError:
            show_load_error_message = True
    elif exit_game:
        exit_game_break = True

    return exit_game_break,action,show_load_error_message,player, entities, game_map, message_log, game_state,show_main_menu