from game_states import GameStates
from loader_functions.data_loaders import save_game
from action_handlers.inventory_index_ih import get_inventory_states


def handle_exit_input(player,game_state,previous_game_state,player_turn_results,entities,game_map,message_log):
    exit_pressed = False
    if game_state in (get_inventory_states()):
        game_state = previous_game_state
    elif game_state == GameStates.TARGETING:
        player_turn_results.append({'targeting_cancelled': True})
    else:
        save_game(player, entities, game_map, message_log, game_state)
        exit_pressed = True

    return game_state, player_turn_results, exit_pressed

