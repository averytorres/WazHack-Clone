from game_states import GameStates


def handle_scroll_inventory_index_input(player,scroll_inventory_index,game_state,player_turn_results,entities,fov_map):
    player_scroll_inv = get_scroll_inventory_index_entities(player)

    if(scroll_inventory_index >= len(player_scroll_inv)) or len(player_scroll_inv) == 0:
        return player_turn_results
    item = player_scroll_inv[int(scroll_inventory_index)]

    if game_state == GameStates.SHOW_INVENTORY:
        player_turn_results.extend(player.inventory.use(item, entities=entities, fov_map=fov_map))
    elif game_state == GameStates.SHOW_WEAPON_INVENTORY:
        player_turn_results.extend(player.inventory.use(item, entities=entities, fov_map=fov_map))
    elif game_state == GameStates.SHOW_SCROLL_INVENTORY:
        player_turn_results.extend(player.inventory.use(item, entities=entities, fov_map=fov_map))
    elif game_state == GameStates.DROP_INVENTORY:
        player_turn_results.extend(player.inventory.drop_item(item))

    return player_turn_results


def get_scroll_inventory_index_options(player):
    player_scroll_inv = []

    for item in player.inventory.items:
        if (item.item.use_function is not None) and (
                ('SCROLL' in (item.first_name.upper()) or ('BOOK' in (item.first_name.upper())))):
            player_scroll_inv.append(item.first_name)
    return player_scroll_inv


def get_scroll_inventory_index_entities(player):
    player_scroll_inv = []

    for item in player.inventory.items:
        if (item.item.use_function is not None) and (
                ('SCROLL' in (item.first_name.upper()) or ('BOOK' in (item.first_name.upper())))):
            player_scroll_inv.append(item)
    return player_scroll_inv