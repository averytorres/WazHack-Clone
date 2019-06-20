import tcod as libtcod
from render_functions import RenderOrder
from game_states import GameStates
from game_messages import Message
from messages.deaths import get_generic_death


def kill_player(player):
    player.char = '%'
    player.color = libtcod.dark_red

    return Message(get_generic_death().format(player.first_name.capitalize()), libtcod.red), GameStates.PLAYER_DEAD


def kill_monster(monster):
    death_message = Message(get_generic_death().format(monster.first_name.capitalize()), libtcod.orange)

    monster.char = '%'
    monster.color = libtcod.dark_red
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.first_name = 'Remains of ' + monster.first_name.capitalize()
    monster.render_order = RenderOrder.CORPSE

    return death_message