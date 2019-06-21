import tcod as libtcod
from game_messages import Message


def handle_pickup_input(entities,player,player_turn_results,message_log):
    for entity in entities:
        if entity.item and entity.x == player.x and entity.y == player.y:
            pickup_results = player.inventory.add_item(entity)
            player_turn_results.extend(pickup_results)

            break
    else:
        message_log.add_message(Message('There is nothing here to pick up.', libtcod.yellow))
    return player_turn_results,message_log
