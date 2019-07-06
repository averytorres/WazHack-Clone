import tcod as libtcod

from random import randint
from random_utils import from_dungeon_level,random_choice_from_dict
from components.ai import BasicMonster
from components.fighter import Fighter
from components.stairs import Stairs
from entity import Entity
from map_objects.rectangle import Rect
from map_objects.tile import Tile
from render_functions import RenderOrder
from messages.names import get_generic_first_name
from item_probability.item_chances import get_item_chances
from item_choice_definition.item_choice import get_item_choice
from map_objects.room_types import determine_room_type


class GameMap:
    def __init__(self, width, height, dungeon_level=1, prev_dungeon_level=0,up_x=0,down_x=0,up_y=0,down_y=0):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

        self.dungeon_level = dungeon_level
        self.prev_dungeon_level = prev_dungeon_level

        self.up_x = up_x
        self.up_y = up_y
        self.down_x = down_x
        self.down_y = down_y

    def initialize_tiles(self):
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]

        return tiles

    def make_map(self, max_rooms, room_min_size, room_max_size, map_width, map_height, player, entities):

        rooms = []
        num_rooms = 0

        center_of_last_room_x = None
        center_of_last_room_y = None

        for r in range(max_rooms):
            # random width and height
            w = randint(room_min_size, room_max_size)
            h = randint(room_min_size, room_max_size)
            # random position without going out of the boundaries of the map
            x = randint(0, map_width - w - 1)
            y = randint(0, map_height - h - 1)

            # "Rect" class makes rectangles easier to work with
            new_room = Rect(x, y, w, h)

            # run through the other rooms and see if they intersect with this one
            for other_room in rooms:
                if new_room.intersect(other_room):
                    break
            else:
                # this means there are no intersections, so this room is valid

                # "paint" it to the map's tiles
                determine_room_type(new_room, self)

                # center coordinates of new room, will be useful later
                (new_x, new_y) = new_room.center()

                center_of_last_room_x = new_x
                center_of_last_room_y = new_y

                if num_rooms == 0:
                    # this is the first room, where the player starts at
                    player.x = new_x
                    player.y = new_y
                else:
                    # all rooms after the first:
                    # connect it to the previous room with a tunnel

                    # center coordinates of previous room
                    (prev_x, prev_y) = rooms[num_rooms - 1].center()

                    # flip a coin (random number that is either 0 or 1)
                    if randint(0, 1) == 1:
                        # first move horizontally, then vertically
                        self.create_h_tunnel(prev_x, new_x, prev_y)
                        self.create_v_tunnel(prev_y, new_y, new_x)
                    else:
                        # first move vertically, then horizontally
                        self.create_v_tunnel(prev_y, new_y, prev_x)
                        self.create_h_tunnel(prev_x, new_x, new_y)

                self.place_entities(new_room, entities)

                # finally, append the new room to the list
                rooms.append(new_room)
                num_rooms += 1

        if self.prev_dungeon_level > self.dungeon_level:
            self.up_x = center_of_last_room_x
            self.up_y = center_of_last_room_y
            self.down_x = player.x
            self.down_y = player.y
        else:
            self.up_x = player.x
            self.up_y = player.y
            self.down_x = center_of_last_room_x
            self.down_y = center_of_last_room_y

        stairs_component = Stairs(self.dungeon_level + 1, 1)
        down_stairs = Entity(self.down_x, self.down_y, '>', libtcod.white, 'Stairs Down',
                             render_order=RenderOrder.STAIRS, stairs=stairs_component)
        entities.append(down_stairs)

        if self.dungeon_level > 0:
            stairs_component = Stairs(self.dungeon_level - 1, -1)
            up_stairs = Entity(self.up_x, self.up_y, '<', libtcod.white, 'Stairs Up',
                               render_order=RenderOrder.STAIRS, stairs=stairs_component)
            entities.append(up_stairs)

    def create_room(self, room):
        # go through the tiles in the rectangle and make them passable
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False

    def create_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def create_v_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def place_entities(self, room, entities):
        max_monsters_per_room = from_dungeon_level([[2, 1], [3, 4], [5, 6]], self.dungeon_level)
        max_items_per_room = from_dungeon_level([[1, 1], [2, 4]], self.dungeon_level)

        # Get a random number of monsters
        number_of_monsters = randint(0, max_monsters_per_room)

        # Get a random number of items
        number_of_items = randint(0, max_items_per_room)

        monster_chances = {
            'orc': 80,
            'troll': from_dungeon_level([[15, 3], [30, 5], [60, 7]], self.dungeon_level)
        }

        item_chances = get_item_chances(self)

        for i in range(number_of_monsters):
            # Choose a random location in the room that is not blocked
            open_tile_found = False
            while not open_tile_found:
                x = randint(room.x1 + 1, room.x2 - 1)
                y = randint(room.y1 + 1, room.y2 - 1)
                if self.tiles[x][y].blocked == False:
                    open_tile_found = True

            # Check if an entity is already in that location
            if not any([entity for entity in entities if entity.x == x and entity.y == y]):
                monster_choice = random_choice_from_dict(monster_chances)
                monster_f_name = get_generic_first_name()
                if monster_choice == 'orc':
                    fighter_component = Fighter(hp=20, defense=0, power=4, xp=35)
                    ai_component = BasicMonster()

                    monster = Entity(x, y, 'o', libtcod.desaturated_green, monster_f_name , 'the Orc', blocks=True,
                                     render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
                else:
                    fighter_component = Fighter(hp=30, defense=2, power=8, xp=100)
                    ai_component = BasicMonster()

                    monster = Entity(x, y, 'T', libtcod.darker_green, monster_f_name, 'the Troll', blocks=True, fighter=fighter_component,
                                     render_order=RenderOrder.ACTOR, ai=ai_component)

                entities.append(monster)

        for i in range(number_of_items):
            open_tile_found = False
            while not open_tile_found:
                x = randint(room.x1 + 1, room.x2 - 1)
                y = randint(room.y1 + 1, room.y2 - 1)
                if self.tiles[x][y].blocked == False:
                    open_tile_found = True

            if not any([entity for entity in entities if entity.x == x and entity.y == y]):
                item_choice = random_choice_from_dict(item_chances)
                item = get_item_choice(item_choice, x, y)

                entities.append(item)

    def is_blocked(self, x, y):
        try:
            if self.tiles[x][y].blocked:
                return True
            else:
                return False
        except:
            return True


    def next_floor(self, player, message_log, constants, direction):
        self.prev_dungeon_level = self.dungeon_level
        self.dungeon_level += direction
        entities = [player]

        self.tiles = self.initialize_tiles()
        self.make_map(constants['max_rooms'], constants['room_min_size'], constants['room_max_size'],
                      constants['map_width'], constants['map_height'], player, entities)

        #this line heals the player as they move down, may turn back on later
        #player.fighter.heal(player.fighter.max_hp // 2)
        #message_log.add_message(Message('You take a moment to rest, and recover your strength.', libtcod.light_violet))

        return entities