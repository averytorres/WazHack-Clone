import tcod as libtcod

from loader_functions.data_loaders import save_floor, load_floor
from fov_functions import initialize_fov


def handle_take_stairs_up_input(player,game_state,entities, game_map, message_log, constants, con, fov_map, fov_recompute):
    for entity in entities:
        if entity.stairs and entity.x == player.x and entity.y == player.y and entity.stairs.direction == -1:
            save_floor(player, entities, game_map, message_log, game_state)
            direction = entity.stairs.direction
            player, entities, game_map, message_log, game_state, existingfloor = load_floor(
                game_map.dungeon_level + direction, player, entities, game_map, message_log,
                game_state)
            if existingfloor is None:
                entities = game_map.next_floor(player, message_log, constants, entity.stairs.direction)
            else:
                if direction > 0:
                    player.x = game_map.up_x
                    player.y = game_map.up_y
                else:
                    player.x = game_map.down_x
                    player.y = game_map.down_y

            fov_map = initialize_fov(game_map)
            fov_recompute = True
            libtcod.console_clear(con)

            break
    # else:
    #     message_log.add_message(Message('There are no stairs here.', libtcod.yellow))

    return fov_map, fov_recompute, entities
