from entity import get_blocking_entities_at_location
from game_states import GameStates

def handle_move_input(move,player,game_map,entities,player_turn_results,fov_recompute,game_state):
    dx, dy = move
    destination_x = player.x + dx
    destination_y = player.y + dy

    if not game_map.is_blocked(destination_x, destination_y):
        target = get_blocking_entities_at_location(entities, destination_x, destination_y)

        if target:
            attack_results = player.fighter.attack(target)
            player_turn_results.extend(attack_results)
        else:
            player.move(dx, dy)
            fov_recompute = True

        player.fighter.heal(.02)
        game_state = GameStates.ENEMY_TURN

    return player_turn_results, player, fov_recompute, game_state
