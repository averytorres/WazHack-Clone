from random import randint
import tcod as libtcod

def get_generic_attack(is_pc):
    attacks = []

    subject = '%c{0}%c '
    result = ' %c-{2}hp%c '
    actions = []
    actions.append("attack")
    actions.append("hit")
    actions.append("barrage")
    actions.append("strike")
    if is_pc:

        action = actions[randint(0, len(actions) - 1)]
        attacks.append(subject% (libtcod.COLCTRL_2, libtcod.COLCTRL_STOP)
                       + action+' %c{1}%c.'% (libtcod.COLCTRL_1, libtcod.COLCTRL_STOP)
                       + result% (libtcod.COLCTRL_3, libtcod.COLCTRL_STOP))
    else:
        actions = [action + 's' for action in actions]

        action = actions[randint(0, len(actions) - 1)]
        attacks.append(subject % (libtcod.COLCTRL_1, libtcod.COLCTRL_STOP)
                       + action + ' %c{1}%c.' % (libtcod.COLCTRL_2, libtcod.COLCTRL_STOP)
                       + result% (libtcod.COLCTRL_4, libtcod.COLCTRL_STOP))

    return attacks[0]