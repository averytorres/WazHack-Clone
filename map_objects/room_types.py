from random import randint


def determine_room_type(room, self):

    room_choice = randint(0, 110)

    if room_choice > 50:
        default_room(room, self)
    elif room_choice > 40:
        diamond_room(room, self)
    elif room_choice > 30:
        default_room(room, self)
        circle_room(room, self)
    else:
        default_room(room, self)
        clover_room(room, self)


def default_room(room, self):
    # go through the tiles in the rectangle and make them passable
    for x in range(room.x1 + 1, room.x2):
        for y in range(room.y1 + 1, room.y2):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False


def circle_room(room, self):
    enable_cell(room.x1 + 1, room.y1, self)
    enable_cell(room.x1 , room.y1 + 1, self)

    enable_cell(room.x1, room.y2 - 1, self)
    enable_cell(room.x1 + 1, room.y2, self)

    enable_cell(room.x2 - 1, room.y1, self)
    enable_cell(room.x2, room.y1 + 1, self)

    enable_cell(room.x2, room.y2 - 1, self)
    enable_cell(room.x2 - 1, room.y2, self)

    enable_horizontal_line(room.x1 + 1, room.x2 - 1, room.y1, self)
    enable_horizontal_line(room.x1 + 1, room.x2 - 1, room.y2, self)

    enable_vertical_line(room.y1 + 1, room.y2 - 1, room.x1, self)
    enable_vertical_line(room.y1 + 1, room.y2 - 1, room.x2, self)


def diamond_room(room, self):

    for x in range(0, int((room.x1 + room.x2)/2)):
        center_x = int((room.x1 + room.x2)/2)
        if ((center_x - x) >= room.x1) and ((center_x + x) <= room.x2):
            enable_horizontal_line(center_x - x, center_x + x, room.y1 + x, self)

    for x in range(0, int((room.x1 + room.x2)/2+1)):
        center_x = int((room.x1 + room.x2)/2)
        if ((center_x - x) >= room.x1) and ((center_x + x) <= room.x2):
            enable_horizontal_line(center_x - x, center_x + x, room.y2 - x, self)

    enable_horizontal_line(room.x1 + 1 , room.x2 - 1, int((room.y1 + room.y2)/2), self)
    enable_vertical_line(room.y1 + 1, room.y2 - 1, int((room.x1 + room.x2)/2), self)


def clover_room(room, self):
    enable_cell(room.x1 + 1, room.y1, self)
    enable_cell(room.x1 , room.y1 + 1, self)

    enable_cell(room.x1, room.y2 - 1, self)
    enable_cell(room.x1 + 1, room.y2, self)

    enable_cell(room.x2 - 1, room.y1, self)
    enable_cell(room.x2, room.y1 + 1, self)

    enable_cell(room.x2, room.y2 - 1, self)
    enable_cell(room.x2 - 1, room.y2, self)


def enable_horizontal_line(x1, x2, y, self):
    for x in range(x1, x2):
        enable_cell(x, y, self)


def enable_vertical_line(y1, y2, x, self):
    for y in range(y1, y2):
        enable_cell(x, y, self)


def enable_cell (x,y, self):
    self.tiles[x][y].blocked = False
    self.tiles[x][y].block_sight = False


def disable_cell (x,y, self):
    self.tiles[x][y].blocked = True
    self.tiles[x][y].block_sight = True