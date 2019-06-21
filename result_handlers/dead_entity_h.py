from death_functions import kill_monster, kill_player


def handle_dead_entity_result(dead_entity,player,game_state,message_log):
    if dead_entity == player:
        message, game_state = kill_player(dead_entity)
    else:
        message = kill_monster(dead_entity)

    message_log.add_message(message)

    return message,game_state,message_log
