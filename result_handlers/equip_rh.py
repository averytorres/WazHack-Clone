from game_messages import Message
from game_states import GameStates

def handle_equip_result(player,equip,message_log):
    equip_results = player.equipment.toggle_equip(equip)

    for equip_result in equip_results:
        equipped = equip_result.get('equipped')
        dequipped = equip_result.get('dequipped')

        if equipped:
            message_log.add_message(Message('You equipped the {0}'.format(equipped.first_name)))

        if dequipped:
            message_log.add_message(Message('You dequipped the {0}'.format(dequipped.first_name)))

    game_state = GameStates.ENEMY_TURN

    return message_log, game_state, player
