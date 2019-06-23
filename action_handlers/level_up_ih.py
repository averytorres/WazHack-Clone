from global_operations import colorize_text_custom


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
    r, g, b = 102, 255, 103
    options = []
    
    constitution = 'Constitution ' + colorize_text_custom('(+20 HP, from {0})', r, g, b)
    strength = 'Strength ' + colorize_text_custom('(+1 attack, from {0})', r, g, b)
    agility = 'Agility ' + colorize_text_custom('(+1 defense, from {0})', r, g, b)

    options.append(constitution.format(player.fighter.max_hp))
    options.append(strength.format(player.fighter.power))
    options.append(agility.format(player.fighter.defense))

    return options
