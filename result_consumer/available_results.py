
def get_available_results(player_turn_result):

    available_results = {}

    message = player_turn_result.get('message')
    dead_entity = player_turn_result.get('dead')
    item_added = player_turn_result.get('item_added')
    item_consumed = player_turn_result.get('consumed')
    item_dropped = player_turn_result.get('item_dropped')
    equip = player_turn_result.get('equip')
    targeting = player_turn_result.get('targeting')
    targeting_cancelled = player_turn_result.get('targeting_cancelled')
    xp = player_turn_result.get('xp')

    available_results.update({'message':message})
    available_results.update({'dead_entity': dead_entity})
    available_results.update({'item_added': item_added})
    available_results.update({'item_consumed': item_consumed})
    available_results.update({'item_dropped': item_dropped})
    available_results.update({'equip': equip})
    available_results.update({'targeting': targeting})
    available_results.update({'targeting_cancelled': targeting_cancelled})
    available_results.update({'xp': xp})

    return available_results
