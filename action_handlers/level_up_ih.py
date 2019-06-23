
def handle_level_up_input(player,level_up,previous_game_state):
    if level_up == 'hp':
        player.fighter.base_max_hp += 20
        player.fighter.hp += 20
    elif level_up == 'str':
        player.fighter.base_power += 1
    elif level_up == 'def':
        player.fighter.base_defense += 1
    game_state = previous_game_state

    return player, game_state


def get_level_up_key(index):
    index = int(index)
    if index == 0:
        return 'hp'
    elif index == 1:
        return 'str'
    elif index == 2:
        return 'def'
    else:
        return 'ERROR_LEVEL_UP'


def get_level_up_index_options(player):
    options = ['Constitution (+20 HP, from {0})'.format(player.fighter.max_hp),
               'Strength (+1 attack, from {0})'.format(player.fighter.power),
               'Agility (+1 defense, from {0})'.format(player.fighter.defense)]
    return options
