from enum import Enum


class GameStates(Enum):
    PLAYERS_TURN = 1
    ENEMY_TURN = 2
    PLAYER_DEAD = 3
    SHOW_INVENTORY = 4
    SHOW_WEAPON_INVENTORY = 5
    DROP_INVENTORY = 6
    TARGETING = 7
    LEVEL_UP = 8
    CHARACTER_SCREEN = 9
