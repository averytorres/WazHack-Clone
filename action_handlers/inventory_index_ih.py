from game_states import GameStates
from components.equipment import EquipmentSlots
from action_handlers.weapon_inventory_index_ih import get_weapon_inventory_description
from action_handlers.armor_inventory_index_ih import get_armor_classes, get_armor_inventory_description


def handle_inventory_index_input(player,inventory_index,game_state,player_turn_results,entities,fov_map):
    if (inventory_index >= len(player.inventory.items)) or len(player.inventory.items) == 0:
        return player_turn_results
    item = player.inventory.items[int(inventory_index)]

    if game_state == GameStates.SHOW_INVENTORY:
        player_turn_results.extend(player.inventory.use(item, entities=entities, fov_map=fov_map))
    elif game_state == GameStates.SHOW_WEAPON_INVENTORY:
        player_turn_results.extend(player.inventory.use(item, entities=entities, fov_map=fov_map))
    elif game_state == GameStates.SHOW_SCROLL_INVENTORY:
        player_turn_results.extend(player.inventory.use(item, entities=entities, fov_map=fov_map))
    elif game_state == GameStates.DROP_INVENTORY:
        player_turn_results.extend(player.inventory.drop_item(item))

    return player_turn_results


def get_inventory_index_options(player):
    player_inv_desc = []
    for item in player.inventory.items:
        if (item.equippable is not None) and (
                item.equippable.slot in (EquipmentSlots.MAIN_HAND, EquipmentSlots.OFF_HAND)):
            player_inv_desc.append(get_weapon_inventory_description(item,player))
        elif (item.equippable is not None) and (
                item.equippable.slot in (get_armor_classes())):
            player_inv_desc.append(get_armor_inventory_description(item,player))
        else:
            player_inv_desc.append(item.first_name)
    return player_inv_desc


def get_inventory_states():
    invent_states = []

    invent_states.append(GameStates.SHOW_INVENTORY)
    invent_states.append(GameStates.SHOW_WEAPON_INVENTORY)
    invent_states.append(GameStates.SHOW_ARMOR_INVENTORY)
    invent_states.append(GameStates.SHOW_SCROLL_INVENTORY)
    invent_states.append(GameStates.SHOW_QUAFF_INVENTORY)
    invent_states.append(GameStates.DROP_INVENTORY)
    invent_states.append(GameStates.CHARACTER_SCREEN)

    return invent_states