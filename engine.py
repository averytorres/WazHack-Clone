import tcod as libtcod

from death_functions import kill_monster, kill_player
from fov_functions import initialize_fov, recompute_fov
from game_messages import Message
from game_states import GameStates
from input_handlers.input_handler_main import handle_keys, handle_mouse, handle_main_menu
from loader_functions.initialize_new_game import get_constants, get_game_variables
from loader_functions.data_loaders import load_game
from menus import main_menu, message_box
from render_functions import clear_all, render_all
from input_handlers.inventory_index_ih import handle_inventory_index_input
from input_handlers.weapon_inventory_index_ih import handle_weapon_inventory_index_input
from input_handlers.scroll_inventory_index_ih import handle_scroll_inventory_index_input
from input_handlers.take_stairs_down_ih import handle_take_stairs_down_input
from input_handlers.take_stairs_up_ih import handle_take_stairs_up_input
from input_handlers.level_up_ih import handle_level_up_input
from input_handlers.targeting_ih import handle_targeting_input
from input_handlers.exit_ih import handle_exit_input
from input_handlers.move_ih import handle_move_input
from input_handlers.pickup_ih import handle_pickup_input


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

        action = handle_keys(key, game_state)
        mouse_action = handle_mouse(mouse)

        move = action.get('move')
        wait = action.get('wait')
        pickup = action.get('pickup')
        show_inventory = action.get('show_inventory')
        show_weapon_inventory = action.get('show_weapon_inventory')
        show_scroll_inventory = action.get('show_scroll_inventory')
        drop_inventory = action.get('drop_inventory')
        inventory_index = action.get('inventory_index')
        weapon_inventory_index = action.get('weapon_inventory_index')
        scroll_inventory_index = action.get('scroll_inventory_index')
        take_stairs_down = action.get('take_stairs_down')
        take_stairs_up = action.get('take_stairs_up')
        level_up = action.get('level_up')
        show_character_screen = action.get('show_character_screen')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        left_click = mouse_action.get('left_click')
        right_click = mouse_action.get('right_click')

        player_turn_results = []

        if move and game_state == GameStates.PLAYERS_TURN:
            player_turn_results, player, fov_recompute, game_state = handle_move_input(move,player,game_map,entities,player_turn_results,fov_recompute,game_state)

        elif wait:
            player.fighter.heal(.2)
            game_state = GameStates.ENEMY_TURN

        elif pickup and game_state == GameStates.PLAYERS_TURN:
            player_turn_results,message_log = handle_pickup_input(entities,player,player_turn_results,message_log)

        if show_inventory:
            previous_game_state = game_state
            game_state = GameStates.SHOW_INVENTORY

        if show_weapon_inventory:
            previous_game_state = game_state
            game_state = GameStates.SHOW_WEAPON_INVENTORY

        if show_scroll_inventory:
            previous_game_state = game_state
            game_state = GameStates.SHOW_SCROLL_INVENTORY

        if drop_inventory:
            previous_game_state = game_state
            game_state = GameStates.DROP_INVENTORY

        if inventory_index is not None and previous_game_state != GameStates.PLAYER_DEAD and inventory_index < len(
                player.inventory.items):
            player_turn_results = handle_inventory_index_input(player,inventory_index,game_state,player_turn_results,entities,fov_map)

        if weapon_inventory_index is not None and previous_game_state != GameStates.PLAYER_DEAD and weapon_inventory_index < len(
                player.inventory.items):
            player_turn_results = handle_weapon_inventory_index_input(player,weapon_inventory_index,game_state,player_turn_results,entities,fov_map)

        if scroll_inventory_index is not None and previous_game_state != GameStates.PLAYER_DEAD and scroll_inventory_index < len(
                player.inventory.items):
            player_turn_results = handle_scroll_inventory_index_input(player,scroll_inventory_index,game_state,player_turn_results,entities,fov_map)

        if take_stairs_down and game_state == GameStates.PLAYERS_TURN:
            player, entities, game_map, message_log, game_state, fov_map, fov_recompute = handle_take_stairs_down_input(entities,player,game_map,message_log,game_state,constants,con,fov_map,fov_recompute)

        if take_stairs_up and game_state == GameStates.PLAYERS_TURN:
            player, entities, game_map, message_log, game_state, fov_map, fov_recompute = handle_take_stairs_up_input(
                entities, player, game_map, message_log, game_state, constants, con, fov_map, fov_recompute)

        if level_up:
            player, game_state = handle_level_up_input(player,level_up,previous_game_state)

        if show_character_screen:
            previous_game_state = game_state
            game_state = GameStates.CHARACTER_SCREEN

        if game_state == GameStates.TARGETING:
            player_turn_results = handle_targeting_input(left_click,right_click,player,targeting_item,entities,fov_map,player_turn_results)

        if exit:
            game_state, player_turn_results, exit_pressed = handle_exit_input(player,game_state,previous_game_state,player_turn_results,entities,game_map,message_log)
            if exit_pressed:
                return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

        for player_turn_result in player_turn_results:
            message = player_turn_result.get('message')
            dead_entity = player_turn_result.get('dead')
            item_added = player_turn_result.get('item_added')
            item_consumed = player_turn_result.get('consumed')
            item_dropped = player_turn_result.get('item_dropped')
            equip = player_turn_result.get('equip')
            targeting = player_turn_result.get('targeting')
            targeting_cancelled = player_turn_result.get('targeting_cancelled')
            xp = player_turn_result.get('xp')

            if message:
                message_log.add_message(message)

            if dead_entity:
                if dead_entity == player:
                    message, game_state = kill_player(dead_entity)
                else:
                    message = kill_monster(dead_entity)

                message_log.add_message(message)

            if item_added:
                entities.remove(item_added)

                game_state = GameStates.ENEMY_TURN

            if item_consumed:
                game_state = GameStates.ENEMY_TURN

            if item_dropped:
                entities.append(item_dropped)

                game_state = GameStates.ENEMY_TURN

            if equip:
                equip_results = player.equipment.toggle_equip(equip)

                for equip_result in equip_results:
                    equipped = equip_result.get('equipped')
                    dequipped = equip_result.get('dequipped')

                    if equipped:
                        message_log.add_message(Message('You equipped the {0}'.format(equipped.first_name)))

                    if dequipped:
                        message_log.add_message(Message('You dequipped the {0}'.format(dequipped.first_name)))

                game_state = GameStates.ENEMY_TURN

            if targeting:
                previous_game_state = GameStates.PLAYERS_TURN
                game_state = GameStates.TARGETING

                targeting_item = targeting

                message_log.add_message(targeting_item.item.targeting_message)

            if targeting_cancelled:
                game_state = previous_game_state

                message_log.add_message(Message('Targeting cancelled'))

            if xp:
                leveled_up = player.level.add_xp(xp)
                exp_disp = 'You gain %c{0}%cxp'% (libtcod.COLCTRL_2, libtcod.COLCTRL_STOP)
                message_log.add_message(Message(exp_disp.format(xp)))

                if leveled_up:

                    previous_game_state = game_state
                    game_state = GameStates.LEVEL_UP

        if game_state == GameStates.ENEMY_TURN:
            player.fighter.heal(.01)
            for entity in entities:
                if entity.ai:
                    enemy_turn_results = entity.ai.take_turn(player, fov_map, game_map, entities)

                    for enemy_turn_result in enemy_turn_results:
                        message = enemy_turn_result.get('message')
                        dead_entity = enemy_turn_result.get('dead')

                        if message:
                            message_log.add_message(message)

                        if dead_entity:
                            if dead_entity == player:
                                message, game_state = kill_player(dead_entity)
                            else:
                                message = kill_monster(dead_entity)

                            message_log.add_message(message)

                            if game_state == GameStates.PLAYER_DEAD:
                                break

                    if game_state == GameStates.PLAYER_DEAD:
                        break
            else:
                game_state = GameStates.PLAYERS_TURN


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