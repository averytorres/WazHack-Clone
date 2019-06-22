from game_states import GameStates

def get_menu_title(menu_name):
    menu_titles = {}
    menu_titles.update({GameStates.SHOW_INVENTORY:'Press the key next to an item to use it, or Esc to cancel.\n'})
    menu_titles.update({GameStates.SHOW_WEAPON_INVENTORY: 'Press the key next to an item to equip/unequip it, or Esc to cancel.\n'})

    return menu_titles[menu_name]


def get_menu_width(menu_name):
    menu_width = {}
    menu_width.update({GameStates.SHOW_INVENTORY: 50})
    menu_width.update({GameStates.SHOW_WEAPON_INVENTORY: 50})

    return menu_width[menu_name]