from game_states import GameStates
from loader_functions.data_loaders import save_game


def handle_exit_input(player,game_state,previous_game_state,player_turn_results,entities,game_map,message_log):
    exit_pressed = False
    if game_state in (GameStates.SHOW_INVENTORY, GameStates.SHOW_WEAPON_INVENTORY, GameStates.SHOW_SCROLL_INVENTORY,
                      GameStates.SHOW_QUAFF_INVENTORY, GameStates.DROP_INVENTORY, GameStates.CHARACTER_SCREEN):
        game_state = previous_game_state
    elif game_state == GameStates.TARGETING:
        player_turn_results.append({'targeting_cancelled': True})
    else:
        save_game(player, entities, game_map, message_log, game_state)
        exit_pressed = True

    return game_state, player_turn_results, exit_pressed
