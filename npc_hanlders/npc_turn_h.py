from game_states import GameStates
from death_functions import kill_monster, kill_player


def handle_npc_turn(game_state,player,entities,fov_map,game_map,message_log):
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
    return player,message_log,game_state
