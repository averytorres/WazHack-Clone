
def handle_targeting_input(player,left_click,right_click,targeting_item,entities,fov_map,player_turn_results):
    if left_click:
        target_x, target_y = left_click

        item_use_results = player.inventory.use(targeting_item, entities=entities, fov_map=fov_map,
                                                target_x=target_x, target_y=target_y)
        player_turn_results.extend(item_use_results)
    elif right_click:
        player_turn_results.append({'targeting_cancelled': True})

    return player_turn_results
