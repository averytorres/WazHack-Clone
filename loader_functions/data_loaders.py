import os

import shelve


def save_game(player, entities, game_map, message_log, game_state):
    with shelve.open('savegame', 'n') as data_file:
        data_file['player_index'] = entities.index(player)
        data_file['entities'] = entities
        data_file['game_map'] = game_map
        data_file['message_log'] = message_log
        data_file['game_state'] = game_state


def load_game():
    if not os.path.isfile('savegame.dat'):
        raise FileNotFoundError

    with shelve.open('savegame', 'r') as data_file:
        player_index = data_file['player_index']
        entities = data_file['entities']
        game_map = data_file['game_map']
        message_log = data_file['message_log']
        game_state = data_file['game_state']

    player = entities[player_index]

    return player, entities, game_map, message_log, game_state


def save_floor(entities, game_map, game_state):
    mapid = 'floor' + str(game_map.dungeon_level)
    with shelve.open('savegame', 'n') as data_file:
        data_file[mapid+'entities'] = entities
        data_file[mapid+'game_map'] = game_map
        data_file[mapid+'game_state'] = game_state


def load_floor(inputfloor,entities, game_map, game_state):
    mapid = 'floor' + str(inputfloor)
    if os.path.isfile('savegame.dat'):
        print("floor loaded")
        #raise FileNotFoundError

        with shelve.open('savegame', 'r') as data_file:
            entities = data_file[mapid+'entities']
            game_map = data_file[mapid+'game_map']
            game_state = data_file[mapid+'game_state']

        return entities, game_map, game_state, True
    else:
        print("floor NOT loaded")
        return entities, game_map, game_state, None
