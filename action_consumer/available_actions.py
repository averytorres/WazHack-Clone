
def get_available_actions(action,mouse_action):

    available_actions = {}

    #Keyboard Actions
    move = action.get('move')
    wait = action.get('wait')
    pickup = action.get('pickup')
    show_inventory = action.get('show_inventory')
    show_weapon_inventory = action.get('show_weapon_inventory')
    show_scroll_inventory = action.get('show_scroll_inventory')
    drop_inventory = action.get('drop_inventory')
    inventory_index = action.get('inventory_index')
    weapon_inventory_index = action.get('weapon_inventory_index')
    scroll_inventory_index = action.get('scroll_inventory_index')
    take_stairs_down = action.get('take_stairs_down')
    take_stairs_up = action.get('take_stairs_up')
    level_up = action.get('level_up')
    show_character_screen = action.get('show_character_screen')
    exit = action.get('exit')
    fullscreen = action.get('fullscreen')

    available_actions.update({'move':move})
    available_actions.update({'wait':wait})
    available_actions.update({'pickup': pickup})
    available_actions.update({'show_inventory': show_inventory})
    available_actions.update({'show_weapon_inventory': show_weapon_inventory})
    available_actions.update({'show_scroll_inventory': show_scroll_inventory})
    available_actions.update({'drop_inventory': drop_inventory})
    available_actions.update({'inventory_index': inventory_index})
    available_actions.update({'weapon_inventory_index': weapon_inventory_index})
    available_actions.update({'scroll_inventory_index': scroll_inventory_index})
    available_actions.update({'take_stairs_down': take_stairs_down})
    available_actions.update({'take_stairs_up': take_stairs_up})
    available_actions.update({'level_up': level_up})
    available_actions.update({'show_character_screen': show_character_screen})
    available_actions.update({'exit': exit})
    available_actions.update({'fullscreen': fullscreen})

    #Mouse Actions
    left_click = mouse_action.get('left_click')
    right_click = mouse_action.get('right_click')
    mouse_inventory_index = mouse_action.get('inventory_index')
    mouse_weapon_inventory_index = mouse_action.get('weapon_inventory_index')
    mouse_scroll_inventory_index = mouse_action.get('scroll_inventory_index')

    available_actions.update({'left_click': left_click})
    available_actions.update({'right_click': right_click})
    available_actions.update({'inventory_index': mouse_inventory_index})
    available_actions.update({'weapon_inventory_index': mouse_weapon_inventory_index})
    available_actions.update({'scroll_inventory_index': mouse_scroll_inventory_index})

    return available_actions
