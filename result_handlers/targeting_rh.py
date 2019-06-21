from game_states import GameStates


def handle_targeting_result(targeting,message_log):
    previous_game_state = GameStates.PLAYERS_TURN
    game_state = GameStates.TARGETING

    targeting_item = targeting

    message_log.add_message(targeting_item.item.targeting_message)

    return targeting_item,previous_game_state,game_state,message_log
