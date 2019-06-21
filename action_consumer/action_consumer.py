import tcod as libtcod

from game_states import GameStates
from input_handlers.input_handler_main import handle_keys, handle_mouse
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
from action_consumer.available_actions import get_available_actions


def consume_actions(key,mouse,game_state,player,game_map, entities,fov_recompute,fov_map,message_log,constants,con,targeting_item,previous_game_state):
    action = handle_keys(key, game_state)
    mouse_action = handle_mouse(mouse)
    exit_pressed = False

    avail_actions = get_available_actions(action, mouse_action)

    player_turn_results = []

    if avail_actions['move'] and game_state == GameStates.PLAYERS_TURN:
        player_turn_results, player, fov_recompute, game_state = handle_move_input(avail_actions['move'], player,
                                                                                   game_map, entities,
                                                                                   player_turn_results, fov_recompute,
                                                                                   game_state)

    elif avail_actions['wait']:
        player.fighter.heal(.2)
        game_state = GameStates.ENEMY_TURN

    elif avail_actions['pickup'] and game_state == GameStates.PLAYERS_TURN:
        player_turn_results, message_log = handle_pickup_input(entities, player, player_turn_results, message_log)

    if avail_actions['show_inventory']:
        previous_game_state = game_state
        game_state = GameStates.SHOW_INVENTORY

    if avail_actions['show_weapon_inventory']:
        previous_game_state = game_state
        game_state = GameStates.SHOW_WEAPON_INVENTORY

    if avail_actions['show_scroll_inventory']:
        previous_game_state = game_state
        game_state = GameStates.SHOW_SCROLL_INVENTORY

    if avail_actions['drop_inventory']:
        previous_game_state = game_state
        game_state = GameStates.DROP_INVENTORY

    if avail_actions['inventory_index'] is not None and previous_game_state != GameStates.PLAYER_DEAD and avail_actions[
        'inventory_index'] < len(
            player.inventory.items):
        player_turn_results = handle_inventory_index_input(player, avail_actions['inventory_index'], game_state,
                                                           player_turn_results, entities, fov_map)

    if avail_actions['weapon_inventory_index'] is not None and previous_game_state != GameStates.PLAYER_DEAD and \
            avail_actions['weapon_inventory_index'] < len(
            player.inventory.items):
        player_turn_results = handle_weapon_inventory_index_input(player, avail_actions['weapon_inventory_index'],
                                                                  game_state, player_turn_results, entities, fov_map)

    if avail_actions['scroll_inventory_index'] is not None and previous_game_state != GameStates.PLAYER_DEAD and \
            avail_actions['scroll_inventory_index'] < len(
            player.inventory.items):
        player_turn_results = handle_scroll_inventory_index_input(player, avail_actions['scroll_inventory_index'],
                                                                  game_state, player_turn_results, entities, fov_map)

    if avail_actions['take_stairs_down'] and game_state == GameStates.PLAYERS_TURN:
        player, entities, game_map, message_log, game_state, fov_map, fov_recompute = handle_take_stairs_down_input(
            entities, player, game_map, message_log, game_state, constants, con, fov_map, fov_recompute)

    if avail_actions['take_stairs_up'] and game_state == GameStates.PLAYERS_TURN:
        player, entities, game_map, message_log, game_state, fov_map, fov_recompute = handle_take_stairs_up_input(
            entities, player, game_map, message_log, game_state, constants, con, fov_map, fov_recompute)

    if avail_actions['level_up']:
        player, game_state = handle_level_up_input(player, avail_actions['level_up'], previous_game_state)

    if avail_actions['show_character_screen']:
        previous_game_state = game_state
        game_state = GameStates.CHARACTER_SCREEN

    if game_state == GameStates.TARGETING:
        player_turn_results = handle_targeting_input(avail_actions['left_click'], avail_actions['right_click'], player,
                                                     targeting_item, entities, fov_map, player_turn_results)

    if avail_actions['exit']:
        game_state, player_turn_results, exit_pressed = handle_exit_input(player, game_state, previous_game_state,
                                                                          player_turn_results, entities, game_map,
                                                                          message_log)

    if avail_actions['fullscreen']:
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

    return action,entities,fov_map,fov_recompute,game_map,game_state,message_log,mouse_action,player,player_turn_results,previous_game_state,exit_pressed
