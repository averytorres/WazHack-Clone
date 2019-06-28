from game_states import GameStates


def handle_quaff_inventory_index_input(player,quaff_inventory_index,game_state,player_turn_results,entities,fov_map):
    player_quaff_inv = get_quaff_inventory_index_entities(player)

    if(quaff_inventory_index >= len(player_quaff_inv)) or len(player_quaff_inv) == 0:
        return player_turn_results
    item = player_quaff_inv[int(quaff_inventory_index)]

    if game_state == GameStates.SHOW_INVENTORY:
        player_turn_results.extend(player.inventory.use(item, entities=entities, fov_map=fov_map))
    elif game_state == GameStates.SHOW_WEAPON_INVENTORY:
        player_turn_results.extend(player.inventory.use(item, entities=entities, fov_map=fov_map))
    elif game_state == GameStates.SHOW_SCROLL_INVENTORY:
        player_turn_results.extend(player.inventory.use(item, entities=entities, fov_map=fov_map))
    elif game_state == GameStates.SHOW_QUAFF_INVENTORY:
        player_turn_results.extend(player.inventory.use(item))
    elif game_state == GameStates.DROP_INVENTORY:
        player_turn_results.extend(player.inventory.drop_item(item))

    return player_turn_results


def get_quaff_inventory_index_options(player):
    player_quaff_inv = []

    for item in player.inventory.items:
        if (item.item.use_function is not None) and (
                ('POTION' in (item.first_name.upper()))):
            player_quaff_inv.append(item.first_name)
    return player_quaff_inv


def get_quaff_inventory_index_entities(player):
    player_quaff_inv = []

    for item in player.inventory.items:
        if (item.item.use_function is not None) and (
                ('POTION' in (item.first_name.upper()))):
            player_quaff_inv.append(item)
    return player_quaff_inv