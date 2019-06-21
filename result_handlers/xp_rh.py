import tcod as libtcod
from game_messages import Message
from game_states import GameStates

def handle_xp_result(player,xp,message_log,game_state,previous_game_state):
    leveled_up = player.level.add_xp(xp)
    exp_disp = 'You gain %c{0}%cxp' % (libtcod.COLCTRL_2, libtcod.COLCTRL_STOP)
    message_log.add_message(Message(exp_disp.format(xp)))

    if leveled_up:
        previous_game_state = game_state
        game_state = GameStates.LEVEL_UP

    return player,message_log,previous_game_state,game_state