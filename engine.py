import tcod as libtcod

from death_functions import kill_player
from fov_functions import initialize_fov, recompute_fov
from game_messages import Message
from game_states import GameStates
from action_handlers.input_handler_main import handle_main_menu
from loader_functions.initialize_new_game import get_constants, get_game_variables
from loader_functions.data_loaders import load_game
from menus import main_menu, message_box
from render_functions import clear_all, render_all
from action_consumer.action_consumer import consume_actions
from result_consumer.result_consumer import consume_results
from npc_hanlders.npc_turn_h import handle_npc_turn


def play_game(player, entities, game_map, message_log, game_state, con, panel, constants):
    fov_recompute = True

    fov_map = initialize_fov(game_map)

    key = libtcod.Key()
    mouse = libtcod.Mouse()

    game_state = GameStates.PLAYERS_TURN
    previous_game_state = game_state

    targeting_item = None

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)

        if fov_recompute:
            message_log.add_message(Message('TEST', libtcod.black))
            recompute_fov(fov_map, player.x, player.y, constants['fov_radius'], constants['fov_light_walls'],
                          constants['fov_algorithm'])

        dead_check = player.fighter.hp
        if dead_check <= 0:
            message, game_state = kill_player(player)

        render_all(con, panel, entities, player, game_map, fov_map, fov_recompute, message_log,
                   constants['screen_width'], constants['screen_height'], constants['bar_width'],
                   constants['panel_height'], constants['panel_y'], mouse, constants['colors'], game_state)

        fov_recompute = False

        libtcod.console_flush()

        clear_all(con, entities)

        #Consume player actions
        action,entities,fov_map,fov_recompute,game_map,game_state,message_log,mouse_action,player,player_turn_results,previous_game_state,exit_pressed = consume_actions(key,mouse,game_state,player,game_map, entities,fov_recompute,fov_map,message_log,constants,con,targeting_item,previous_game_state)
        if exit_pressed:
            return True

        #Consume action results
        for player_turn_result in player_turn_results:
            available_results,message_log,message,game_state,entities,player,game_state,targeting_item, previous_game_state = consume_results(player_turn_result,message_log,entities,player,game_state,targeting_item, previous_game_state)

        #consume NPC actions
        player,message_log,game_state = handle_npc_turn(game_state,player,entities,fov_map,game_map,message_log)



def main():
    constants = get_constants()

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    libtcod.console_init_root(constants['screen_width'], constants['screen_height'], constants['window_title'], False)

    con = libtcod.console_new(constants['screen_width'], constants['screen_height'])
    panel = libtcod.console_new(constants['screen_width'], constants['panel_height'])

    player = None
    entities = []
    game_map = None
    message_log = None
    game_state = None

    show_main_menu = True
    show_load_error_message = False

    main_menu_background_image = libtcod.image_load(constants['menu_background'])

    key = libtcod.Key()
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)

        if show_main_menu:
            main_menu(con, main_menu_background_image, constants['screen_width'],
                      constants['screen_height'],constants['window_title'],)

            if show_load_error_message:
                message_box(con, 'No save game to load', 50, constants['screen_width'], constants['screen_height'])

            libtcod.console_flush()

            action = handle_main_menu(key)

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
                break

        else:
            libtcod.console_clear(con)
            play_game(player, entities, game_map, message_log, game_state, con, panel, constants)

            show_main_menu = True


if __name__ == '__main__':
    main()