from game_states import GameStates


def get_menu_title(menu_name):
    menu_titles = {}

    menu_titles.update({GameStates.SHOW_INVENTORY:'Press the key next to an item to use it, or Esc to cancel.\n'})
    menu_titles.update({GameStates.DROP_INVENTORY: 'Press the key next to an item to drop it, or Esc to cancel.\n'})
    menu_titles.update({GameStates.SHOW_WEAPON_INVENTORY: 'Press the key next to an item to equip/unequip it, or Esc to cancel.\n'})
    menu_titles.update({GameStates.SHOW_ARMOR_INVENTORY: 'Press the key next to an item to equip/unequip it, or Esc to cancel.\n'})
    menu_titles.update({GameStates.SHOW_SCROLL_INVENTORY: 'Press the key next to an item to read it, or Esc to cancel.\n'})
    menu_titles.update({GameStates.SHOW_QUAFF_INVENTORY: 'Press the key next to an item to quaff it, or Esc to cancel.\n'})
    menu_titles.update({GameStates.LEVEL_UP: 'Level up! Choose a stat to raise:'})
    menu_titles.update({GameStates.CHARACTER_SCREEN: 'Character Information'})
    menu_titles.update({GameStates.PLAYERS_TURN: ''})
    menu_titles.update({None: ''})

    return menu_titles[menu_name]


def get_menu_width(menu_name):
    menu_width = {}

    menu_width.update({GameStates.SHOW_INVENTORY: 50})
    menu_width.update({GameStates.DROP_INVENTORY: 50})
    menu_width.update({GameStates.SHOW_WEAPON_INVENTORY: 50})
    menu_width.update({GameStates.SHOW_ARMOR_INVENTORY: 50})
    menu_width.update({GameStates.SHOW_SCROLL_INVENTORY: 50})
    menu_width.update({GameStates.SHOW_QUAFF_INVENTORY: 50})
    menu_width.update({GameStates.LEVEL_UP: 40})
    menu_width.update({GameStates.CHARACTER_SCREEN: 10})
    menu_width.update({GameStates.PLAYERS_TURN: 24})
    menu_width.update({None: 24})

    return menu_width[menu_name]


def get_menu_height(screen_height):
    return int(screen_height * 1.8)


def get_main_menu_options():
    return ['Play a new game', 'Continue last game', 'Quit']


def get_main_menu_key(index):
    index = int(index)
    if index == 0:
        return {'new_game': True}
    elif index == 1:
        return {'load_game': True}
    elif index == 2:
        return {'exit': True}
    else:
        return {}

