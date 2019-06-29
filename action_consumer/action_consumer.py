import tcod as libtcod

from game_states import GameStates
from action_handlers.input_handler_main import handle_keys, handle_mouse
from action_handlers.inventory_index_ih import handle_inventory_index_input
from action_handlers.weapon_inventory_index_ih import handle_weapon_inventory_index_input, get_weapon_inventory_index_options
from action_handlers.armor_inventory_index_ih import handle_armor_inventory_index_input, get_armor_inventory_index_options
from action_handlers.scroll_inventory_index_ih import handle_scroll_inventory_index_input, get_scroll_inventory_index_options
from action_handlers.quaff_inventory_index_ih import handle_quaff_inventory_index_input, get_quaff_inventory_index_options
from action_handlers.take_stairs_down_ih import handle_take_stairs_down_input
from action_handlers.take_stairs_up_ih import handle_take_stairs_up_input
from action_handlers.level_up_ih import handle_level_up_input
from action_handlers.targeting_ih import handle_targeting_input
from action_handlers.exit_ih import handle_exit_input
from action_handlers.move_ih import handle_move_input
from action_handlers.pickup_ih import handle_pickup_input
from action_consumer.available_actions import get_available_actions
from action_consumer.available_actions_enum import AvailableActionsEnum


def consume_actions(key,mouse,game_state,player,game_map, entities,fov_recompute,fov_map,message_log,constants,con,targeting_item,previous_game_state):
    action = handle_keys(key,mouse,game_state)
    mouse_action = handle_mouse(key,mouse,game_state,constants,con,player)
    exit_pressed = False

    avail_actions = get_available_actions(action, mouse_action)

    player_turn_results = []

    if avail_actions[AvailableActionsEnum.MOVE] and game_state == GameStates.PLAYERS_TURN:
        player_turn_results, player, fov_recompute, game_state = handle_move_input(avail_actions[AvailableActionsEnum.MOVE], player,
                                                                                   game_map, entities,
                                                                                   player_turn_results, fov_recompute,
                                                                                   game_state)

    elif avail_actions[AvailableActionsEnum.WAIT]:
        player.fighter.heal(.2)
        game_state = GameStates.ENEMY_TURN

    elif avail_actions[AvailableActionsEnum.PICKUP] and game_state == GameStates.PLAYERS_TURN:
        player_turn_results, message_log = handle_pickup_input(entities, player, player_turn_results, message_log)

    if avail_actions[AvailableActionsEnum.SHOW_INVENTORY]:
        previous_game_state = game_state
        game_state = GameStates.SHOW_INVENTORY

    if avail_actions[AvailableActionsEnum.SHOW_WEAPON_INVENTORY]:
        previous_game_state = game_state
        game_state = GameStates.SHOW_WEAPON_INVENTORY

    if avail_actions[AvailableActionsEnum.SHOW_ARMOR_INVENTORY]:
        previous_game_state = game_state
        game_state = GameStates.SHOW_ARMOR_INVENTORY

    if avail_actions[AvailableActionsEnum.SHOW_SCROLL_INVENTORY]:
        previous_game_state = game_state
        game_state = GameStates.SHOW_SCROLL_INVENTORY

    if avail_actions[AvailableActionsEnum.SHOW_QUAFF_INVENTORY]:
        previous_game_state = game_state
        game_state = GameStates.SHOW_QUAFF_INVENTORY

    if avail_actions[AvailableActionsEnum.DROP_INVENTORY]:
        previous_game_state = game_state
        game_state = GameStates.DROP_INVENTORY

    curr_avail_action_check = AvailableActionsEnum.INVENTORY_INDEX
    curr_avail_action_check_mouse = AvailableActionsEnum.INVENTORY_INDEX_MOUSE
    if ((avail_actions[curr_avail_action_check] is not None and avail_actions[curr_avail_action_check] < len(player.inventory.items))
        or (avail_actions[curr_avail_action_check_mouse] is not None and avail_actions[curr_avail_action_check_mouse] < len(player.inventory.items))) \
            and previous_game_state != GameStates.PLAYER_DEAD:
        if avail_actions[curr_avail_action_check] is not None:
            inventory_index = avail_actions[curr_avail_action_check]
        else:
            inventory_index = avail_actions[curr_avail_action_check_mouse]
        player_turn_results = handle_inventory_index_input(player, inventory_index, game_state,
                                                           player_turn_results, entities, fov_map)

    curr_avail_action_check = AvailableActionsEnum.WEAPON_INVENTORY_INDEX
    curr_avail_action_check_mouse = AvailableActionsEnum.WEAPON_INVENTORY_INDEX_MOUSE
    if ((avail_actions[curr_avail_action_check] is not None and avail_actions[curr_avail_action_check] < len(get_weapon_inventory_index_options(player)))
        or (avail_actions[curr_avail_action_check_mouse] is not None and avail_actions[curr_avail_action_check_mouse] < len(player.inventory.items))) \
            and previous_game_state != GameStates.PLAYER_DEAD:
        if avail_actions[curr_avail_action_check] is not None:
            inventory_index = avail_actions[curr_avail_action_check]
        else:
            inventory_index = avail_actions[curr_avail_action_check_mouse]
        player_turn_results = handle_weapon_inventory_index_input(player, inventory_index,
                                                                  game_state, player_turn_results, entities, fov_map)

    curr_avail_action_check = AvailableActionsEnum.ARMOR_INVENTORY_INDEX
    curr_avail_action_check_mouse = AvailableActionsEnum.ARMOR_INVENTORY_INDEX_MOUSE
    if ((avail_actions[curr_avail_action_check] is not None and avail_actions[curr_avail_action_check] < len(
            get_armor_inventory_index_options(player)))
        or (avail_actions[curr_avail_action_check_mouse] is not None and avail_actions[
                curr_avail_action_check_mouse] < len(player.inventory.items))) \
            and previous_game_state != GameStates.PLAYER_DEAD:
        if avail_actions[curr_avail_action_check] is not None:
            inventory_index = avail_actions[curr_avail_action_check]
        else:
            inventory_index = avail_actions[curr_avail_action_check_mouse]
        player_turn_results = handle_armor_inventory_index_input(player, inventory_index,
                                                                  game_state, player_turn_results, entities, fov_map)

    curr_avail_action_check = AvailableActionsEnum.SCROLL_INVENTORY_INDEX
    curr_avail_action_check_mouse = AvailableActionsEnum.SCROLL_INVENTORY_INDEX_MOUSE
    if ((avail_actions[curr_avail_action_check] is not None and avail_actions[curr_avail_action_check] < len(get_scroll_inventory_index_options(player)))
        or (avail_actions[curr_avail_action_check_mouse] is not None and avail_actions[curr_avail_action_check_mouse] < len(player.inventory.items))) \
            and previous_game_state != GameStates.PLAYER_DEAD:
        if avail_actions[curr_avail_action_check] is not None:
            inventory_index = avail_actions[curr_avail_action_check]
        else:
            inventory_index = avail_actions[curr_avail_action_check_mouse]
        player_turn_results = handle_scroll_inventory_index_input(player, inventory_index,
                                                                  game_state, player_turn_results, entities, fov_map)

    curr_avail_action_check = AvailableActionsEnum.QUAFF_INVENTORY_INDEX
    curr_avail_action_check_mouse = AvailableActionsEnum.QUAFF_INVENTORY_INDEX_MOUSE
    if ((avail_actions[curr_avail_action_check] is not None and avail_actions[curr_avail_action_check] < len(
            get_quaff_inventory_index_options(player)))
        or (avail_actions[curr_avail_action_check_mouse] is not None and avail_actions[
                curr_avail_action_check_mouse] < len(player.inventory.items))) \
            and previous_game_state != GameStates.PLAYER_DEAD:
        if avail_actions[curr_avail_action_check] is not None:
            inventory_index = avail_actions[curr_avail_action_check]
        else:
            inventory_index = avail_actions[curr_avail_action_check_mouse]
        player_turn_results = handle_quaff_inventory_index_input(player, inventory_index,
                                                                  game_state, player_turn_results, entities, fov_map)

    if avail_actions[AvailableActionsEnum.TAKE_STAIRS_DOWN] and game_state == GameStates.PLAYERS_TURN:
        player, entities, game_map, message_log, game_state, fov_map, fov_recompute = handle_take_stairs_down_input(
            entities, player, game_map, message_log, game_state, constants, con, fov_map, fov_recompute)

    if avail_actions[AvailableActionsEnum.TAKE_STAIRS_UP] and game_state == GameStates.PLAYERS_TURN:
        player, entities, game_map, message_log, game_state, fov_map, fov_recompute = handle_take_stairs_up_input(
            entities, player, game_map, message_log, game_state, constants, con, fov_map, fov_recompute)

    curr_avail_action_check = AvailableActionsEnum.LEVEL_UP
    curr_avail_action_check_mouse = AvailableActionsEnum.LEVEL_UP_MOUSE
    if avail_actions[curr_avail_action_check] or avail_actions[curr_avail_action_check_mouse]:
        if avail_actions[curr_avail_action_check] is not None:
            inventory_index = avail_actions[curr_avail_action_check]
        else:
            inventory_index = avail_actions[curr_avail_action_check_mouse]
        player, game_state = handle_level_up_input(player, inventory_index, previous_game_state)

    if avail_actions[AvailableActionsEnum.SHOW_CHARACTER_SCREEN]:
        previous_game_state = game_state
        game_state = GameStates.CHARACTER_SCREEN

    if game_state == GameStates.TARGETING:
        player_turn_results = handle_targeting_input(avail_actions[AvailableActionsEnum.LEFT_CLICK], avail_actions[AvailableActionsEnum.RIGHT_CLICK], player,
                                                     targeting_item, entities, fov_map, player_turn_results)

    if avail_actions[AvailableActionsEnum.EXIT]:
        game_state, player_turn_results, exit_pressed = handle_exit_input(player, game_state, previous_game_state,
                                                                          player_turn_results, entities, game_map,
                                                                          message_log)

    if avail_actions[AvailableActionsEnum.FULLSCREEN]:
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

    return action,entities,fov_map,fov_recompute,game_map,game_state,message_log,mouse_action,player,player_turn_results,previous_game_state,exit_pressed
