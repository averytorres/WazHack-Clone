import tcod as libtcod
from game_messages import Message
from item_functions import cast_confuse, cast_fireball, cast_lightning, heal
from components.item import Item
from entity import Entity
from render_functions import RenderOrder


def get_scroll_choice(item_choice, x, y):
    if item_choice == 'fireball_scroll':
        item_component = Item(use_function=cast_fireball, targeting=True, targeting_message=Message(
            'Left-click a target tile for the fireball, or right-click to cancel.', libtcod.light_cyan),
                              damage=25, radius=3)
        item = Entity(x, y, '#', libtcod.red, 'Fireball Scroll', render_order=RenderOrder.ITEM,
                      item=item_component)

    elif item_choice == 'confusion_scroll':
        item_component = Item(use_function=cast_confuse, targeting=True, targeting_message=Message(
            'Left-click an enemy to confuse it, or right-click to cancel.', libtcod.light_cyan))
        item = Entity(x, y, '#', libtcod.light_pink, 'Confusion Scroll', render_order=RenderOrder.ITEM,
                      item=item_component)
    elif item_choice == 'lightning_scroll':
        item_component = Item(use_function=cast_lightning, damage=40, maximum_range=5)
        item = Entity(x, y, '#', libtcod.yellow, 'Lightning Scroll', render_order=RenderOrder.ITEM,
                      item=item_component)
    else:
        item_component = Item(use_function=None, damage=0, maximum_range=0)
        item = Entity(x, y, '?', libtcod.yellow, 'ERROR SCROLL', render_order=RenderOrder.ITEM,
                      item=item_component)

    return item
