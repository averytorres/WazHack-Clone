import tcod as libtcod
from game_states import GameStates
from components.equipment import EquipmentSlots
from global_operations import colorize_text


def handle_weapon_inventory_index_input(player,weapon_inventory_index,game_state,player_turn_results,entities,fov_map):
    player_weapon_inv = get_weapon_inventory_index_entities(player)

    if weapon_inventory_index >= len(player_weapon_inv) or len(player_weapon_inv) == 0:
        return player_turn_results
    item = player_weapon_inv[int(weapon_inventory_index)]

    if game_state == GameStates.SHOW_INVENTORY:
        player_turn_results.extend(player.inventory.use(item, entities=entities, fov_map=fov_map))
    elif game_state == GameStates.SHOW_WEAPON_INVENTORY:
        player_turn_results.extend(player.inventory.use(item, entities=entities, fov_map=fov_map))
    elif game_state == GameStates.SHOW_SCROLL_INVENTORY:
        player_turn_results.extend(player.inventory.use(item, entities=entities, fov_map=fov_map))
    elif game_state == GameStates.DROP_INVENTORY:
        player_turn_results.extend(player.inventory.drop_item(item))

    return player_turn_results


def get_weapon_inventory_index_entities(player):
    player_weapon_inv = []
    for item in player.inventory.items:
        if (item.equippable is not None) and (
                item.equippable.slot in (EquipmentSlots.MAIN_HAND, EquipmentSlots.OFF_HAND)):
            player_weapon_inv.append(item)
    return player_weapon_inv


def get_weapon_inventory_index_options(player):
    player_weapon_inv = []
    for item in player.inventory.items:
        if (item.equippable is not None) and (
                item.equippable.slot in (EquipmentSlots.MAIN_HAND, EquipmentSlots.OFF_HAND)):
            player_weapon_inv.append(get_weapon_inventory_description(item,player))
    return player_weapon_inv


def get_weapon_inventory_description(item,player):
    ret = None
    if (item.equippable is not None) and (
            item.equippable.slot in (EquipmentSlots.MAIN_HAND, EquipmentSlots.OFF_HAND)):
        if player.equipment.main_hand == item:
            wep_qual = colorize_text('(on main hand)', libtcod.COLCTRL_3)
            wep_qual = '{0} ' + wep_qual
            ret = wep_qual.format(item.first_name)
        elif player.equipment.off_hand == item:
            wep_qual = colorize_text('(on off hand)', libtcod.COLCTRL_3)
            wep_qual = '{0} ' + wep_qual
            ret = wep_qual.format(item.first_name)
        else:
            ret = item.first_name
    return ret