
def handle_level_up_input(player,level_up,previous_game_state):
    if level_up == 'hp':
        player.fighter.base_max_hp += 20
        player.fighter.hp += 20
    elif level_up == 'str':
        player.fighter.base_power += 1
    elif level_up == 'def':
        player.fighter.base_defense += 1

    game_state = previous_game_state

    return game_state
