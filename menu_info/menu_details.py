

def get_menu_title(menu_name):
    menu_titles = {}
    menu_titles.update({"inventory_title":'Press the key next to an item to use it, or Esc to cancel.\n'})

    return menu_titles[menu_name]


def get_menu_width(menu_name):
    menu_width = {}
    menu_width.update({"inventory_title": 50})

    return menu_width[menu_name]