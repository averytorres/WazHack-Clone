from game_states import GameStates
from game_messages import Message
from result_handlers.dead_entity_rh import handle_dead_entity_result
from result_handlers.equip_rh import handle_equip_result
from result_handlers.targeting_rh import handle_targeting_result
from result_handlers.xp_rh import handle_xp_result
from result_consumer.available_results import get_available_results


def consume_results(player_turn_result,message_log,entities,player,game_state,targeting_item, previous_game_state):
    available_results = get_available_results(player_turn_result)

    if available_results['message']:
        message_log.add_message(available_results['message'])

    if available_results['dead_entity']:
        available_results['message'], game_state, message_log = handle_dead_entity_result(available_results['dead_entity'], player,
                                                                     game_state, message_log)

    if available_results['item_added']:
        entities.remove(available_results['item_added'])
        game_state = GameStates.ENEMY_TURN

    if available_results['item_consumed']:
        game_state = GameStates.ENEMY_TURN

    if available_results['item_dropped']:
        entities.append(available_results['item_dropped'])

        game_state = GameStates.ENEMY_TURN

    if available_results['equip']:
        message_log, game_state, player = handle_equip_result(player, available_results['equip'], message_log)

    if available_results['targeting']:
        targeting_item, previous_game_state, game_state, message_log = handle_targeting_result(
            available_results['targeting'], message_log)

    if available_results['targeting_cancelled']:
        game_state = previous_game_state
        message_log.add_message(Message('Targeting cancelled'))

    if available_results['xp']:
        player, message_log, previous_game_state, game_state = handle_xp_result(player, available_results['xp'],
                                                                                message_log, game_state,
                                                                                previous_game_state)

    return available_results,message_log,available_results['message'],game_state,entities,player,game_state,targeting_item, previous_game_state

