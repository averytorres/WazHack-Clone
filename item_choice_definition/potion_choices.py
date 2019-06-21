import tcod as libtcod

from item_functions import heal
from components.item import Item
from entity import Entity
from render_functions import RenderOrder


def get_potion_choice(item_choice, x, y):

    if item_choice == 'healing_potion':
        item_component = Item(use_function=heal, amount=40)
        item = Entity(x, y, '!', libtcod.violet, 'Healing Potion', render_order=RenderOrder.ITEM,
                      item=item_component)
    else:
        item_component = Item(use_function=None, amount=0)
        item = Entity(x, y, '?', libtcod.violet, 'ERROR POTION', render_order=RenderOrder.ITEM,
                      item=item_component)

    return item
