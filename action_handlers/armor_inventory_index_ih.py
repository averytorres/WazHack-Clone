import tcod as libtcod
from game_states import GameStates
from components.equipment import EquipmentSlots
from global_operations import colorize_text


def handle_armor_inventory_index_input(player,armor_inventory_index,game_state,player_turn_results,entities,fov_map):
    player_armor_inv = get_armor_inventory_index_entities(player)

    if armor_inventory_index >= len(player_armor_inv) or len(player_armor_inv) == 0:
        return player_turn_results
    item = player_armor_inv[int(armor_inventory_index)]

    if game_state == GameStates.SHOW_INVENTORY:
        player_turn_results.extend(player.inventory.use(item, entities=entities, fov_map=fov_map))
    elif game_state == GameStates.SHOW_WEAPON_INVENTORY:
        player_turn_results.extend(player.inventory.use(item, entities=entities, fov_map=fov_map))
    elif game_state == GameStates.SHOW_SCROLL_INVENTORY:
        player_turn_results.extend(player.inventory.use(item, entities=entities, fov_map=fov_map))
    elif game_state == GameStates.SHOW_ARMOR_INVENTORY:
        player_turn_results.extend(player.inventory.use(item, entities=entities, fov_map=fov_map))
    elif game_state == GameStates.DROP_INVENTORY:
        player_turn_results.extend(player.inventory.drop_item(item))

    return player_turn_results


def get_armor_classes():
    armor_classes = []

    armor_classes.append(EquipmentSlots.HANDS)
    armor_classes.append(EquipmentSlots.CHEST)
    armor_classes.append(EquipmentSlots.EYES)
    armor_classes.append(EquipmentSlots.FACE)
    armor_classes.append(EquipmentSlots.FEET)
    armor_classes.append(EquipmentSlots.HEAD)
    armor_classes.append(EquipmentSlots.LEGS)

    return armor_classes


def get_armor_inventory_index_entities(player):
    player_armor_inv = []
    for item in player.inventory.items:
        if (item.equippable is not None) and (
                item.equippable.slot in (get_armor_classes())):
            player_armor_inv.append(item)
    return player_armor_inv


def get_armor_inventory_index_options(player):
    player_armor_inv = []
    for item in player.inventory.items:
        if (item.equippable is not None) and (
                item.equippable.slot in (get_armor_classes())):
            player_armor_inv.append(get_armor_inventory_description(item,player))
    return player_armor_inv


def get_armor_inventory_description(item,player):
    ret = None

    if (item.equippable is not None) and (
            item.equippable.slot in (get_armor_classes())):
        if player.equipment.hands == item:
            ret = format_armor_display_text('(on hands)', item)
        elif player.equipment.chest == item:
            ret = format_armor_display_text('(on chest)', item)
        elif player.equipment.eyes == item:
            ret = format_armor_display_text('(on eyes)', item)
        elif player.equipment.face == item:
            ret = format_armor_display_text('(on face)', item)
        elif player.equipment.feet == item:
            ret = format_armor_display_text('(on feet)', item)
        elif player.equipment.head == item:
            ret = format_armor_display_text('(on head)', item)
        elif player.equipment.legs == item:
            ret = format_armor_display_text('(on legs)', item)
        else:
            ret = item.first_name
    return ret


def format_armor_display_text(display_text, item):

    wep_qual = colorize_text(display_text, libtcod.COLCTRL_3)
    wep_qual = '{0} ' + wep_qual
    ret = wep_qual.format(item.first_name)

    return ret