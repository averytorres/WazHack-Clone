
def get_available_actions(action,mouse_action):

    available_actions = {}

    #Keyboard Actions
    available_actions.update({'move':action.get('move')})
    available_actions.update({'wait':action.get('wait')})
    available_actions.update({'pickup': action.get('pickup')})
    available_actions.update({'show_inventory': action.get('show_inventory')})
    available_actions.update({'show_weapon_inventory': action.get('show_weapon_inventory')})
    available_actions.update({'show_armor_inventory': action.get('show_armor_inventory')})
    available_actions.update({'show_scroll_inventory': action.get('show_scroll_inventory')})
    available_actions.update({'show_quaff_inventory': action.get('show_quaff_inventory')})
    available_actions.update({'drop_inventory': action.get('drop_inventory')})
    available_actions.update({'inventory_index': action.get('inventory_index')})
    available_actions.update({'weapon_inventory_index': action.get('weapon_inventory_index')})
    available_actions.update({'armor_inventory_index': action.get('armor_inventory_index')})
    available_actions.update({'scroll_inventory_index': action.get('scroll_inventory_index')})
    available_actions.update({'quaff_inventory_index': action.get('quaff_inventory_index')})
    available_actions.update({'take_stairs_down': action.get('take_stairs_down')})
    available_actions.update({'take_stairs_up': action.get('take_stairs_up')})
    available_actions.update({'level_up': action.get('level_up')})
    available_actions.update({'show_character_screen': action.get('show_character_screen')})
    available_actions.update({'exit': action.get('exit')})
    available_actions.update({'fullscreen': action.get('fullscreen')})

    #Mouse Actions
    available_actions.update({'left_click': mouse_action.get('left_click')})
    available_actions.update({'right_click': mouse_action.get('right_click')})
    available_actions.update({'inventory_index_mouse': mouse_action.get('inventory_index_mouse')})
    available_actions.update({'weapon_inventory_index_mouse': mouse_action.get('weapon_inventory_index_mouse')})
    available_actions.update({'armor_inventory_index_mouse': mouse_action.get('armor_inventory_index_mouse')})
    available_actions.update({'scroll_inventory_index_mouse': mouse_action.get('scroll_inventory_index_mouse')})
    available_actions.update({'quaff_inventory_index_mouse': mouse_action.get('quaff_inventory_index_mouse')})
    available_actions.update({'level_up_mouse': mouse_action.get('level_up_mouse')})

    return available_actions
