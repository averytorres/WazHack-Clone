import tcod as libtcod
import math
from components.equipment import EquipmentSlots


def menu(con, header, options, width, SCREEN_WIDTH, SCREEN_HEIGHT,key, mouse):

    if len(options) > 26:
        raise ValueError("Cannot have a menu with more than 26 options")

    # Calculate total height for the header (after auto-wrap) and one line per options
    if header == "":
        header_height = 0
    else:
        header_height = libtcod.console_get_height_rect(con, 0, 0, width, SCREEN_HEIGHT, header)
    height = len(options) + header_height

    # Create an off-screen console that represents the menu's window
    window = libtcod.console_new(width, height)

    # Print the header, with auto-wrap
    libtcod.console_set_default_foreground(window, libtcod.white)
    libtcod.console_print_rect_ex(window, 0, 0, width, height, libtcod.BKGND_NONE, libtcod.LEFT, header)

    # Print all the options
    y = header_height
    letter_index = ord("a")

    for option_text in options:
        text = "({0}) {1}".format(chr(letter_index), option_text)
        libtcod.console_print_ex(window, 0, y, libtcod.BKGND_NONE, libtcod.LEFT, text)
        y += 1
        letter_index += 1

    # Calculate coordinates
    x = SCREEN_WIDTH / 2 - width / 2
    y = SCREEN_HEIGHT / 2 - height / 2

    # Compute x and y offsets to convert console position to menu position
    x_offset = x  # x is the left edge of the menu
    y_offset = y + (header_height - (header_height/5))  # The top edge of the menu

    # Now we'll blit the contents of "window" to the root console
    # The last two parameters of this next function control the foreground transparency
    # and the background transparency, respectively
    x = int(x)
    y = int(y)
    libtcod.console_blit(window, 0, 0, width, height, 0, x, y, 1.0, 0.7)

    while True:
        # Present the root console to the player and wait for a key press
        libtcod.console_flush()
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)

        if mouse.lbutton_pressed:
            (menu_x, menu_y) = (mouse.cx - x_offset, mouse.cy - y_offset)

            # Check if click is within the menu and on a choice
            if menu_x >= 0 and menu_x < width and menu_y >= 0 and menu_y < height - header_height:
                menu_y = int(math.ceil(menu_y)) - 1
                return menu_y

        if mouse.rbutton_pressed or key.vk == libtcod.KEY_ESCAPE:
            return None  # Cancel if the player right clicked or hit escape

        if key.vk == libtcod.KEY_ENTER and key.lalt:  # Check for alt + enter to fullscreen
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

        # Convert the ASCII code to an index; if it corresponds to an option, return it
        index = key.c - ord('a')
        if index >= 0 and index < len(options): return index

        # If they hit a letter that is not an option, return None
        if index >= 0 and index <= 26: return None


def inventory_menu(con, header, player, inventory_width, screen_width, screen_height,key, mouse):
    # show a menu with each item of the inventory as an option
    if len(player.inventory.items) == 0:
        options = ['Inventory is empty.']
    else:
        options = []

        for item in player.inventory.items:
            if player.equipment.main_hand == item:
                options.append('{0} (on main hand)'.format(item.first_name))
            elif player.equipment.off_hand == item:
                options.append('{0} (on off hand)'.format(item.first_name))
            else:
                options.append(item.first_name)

    menu(con, header, options, inventory_width, screen_width, screen_height,key, mouse)


def weapon_inventory_menu(con, header, player, inventory_width, screen_width, screen_height,key, mouse):
    # show a menu with each weapon item of the inventory as an option
    if len(player.inventory.items) == 0:
        options = ['Weapon inventory is empty.']
    else:
        options = []

        for item in player.inventory.items:
            if (item.equippable is not None) and (item.equippable.slot in (EquipmentSlots.MAIN_HAND, EquipmentSlots.OFF_HAND)):
                if player.equipment.main_hand == item:
                    options.append('{0} (on main hand)'.format(item.first_name))
                elif player.equipment.off_hand == item:
                    options.append('{0} (on off hand)'.format(item.first_name))
                else:
                    options.append(item.first_name)

    menu(con, header, options, inventory_width, screen_width, screen_height,key, mouse)


def scroll_inventory_menu(con, header, player, inventory_width, screen_width, screen_height,key, mouse):
    # show a menu with each scroll item of the inventory as an option
    if len(player.inventory.items) == 0:
        options = ['Weapon inventory is empty.']
    else:
        options = []

        for item in player.inventory.items:
            if (item.item.use_function is not None) and (('SCROLL' in (item.first_name.upper()) or ('BOOK' in (item.first_name.upper())))):
                    options.append(item.first_name)

    menu(con, header, options, inventory_width, screen_width, screen_height,key, mouse)


def main_menu(con, background_image, screen_width, screen_height,window_title,key, mouse):
    libtcod.image_blit_2x(background_image, None, 0, 0, sx=0, sy=0, w=-1, h=-1)

    libtcod.console_set_default_foreground(0, libtcod.light_yellow)
    libtcod.console_print_ex(0, int(screen_width / 2), int(screen_height*.9) - 4, libtcod.BKGND_NONE, libtcod.CENTER,
                             window_title)
    libtcod.console_print_ex(0, int(screen_width / 2), int(screen_height - 2), libtcod.BKGND_NONE, libtcod.CENTER,
                             '')

    menu(con, '', ['Play a new game', 'Continue last game', 'Quit'], 24, screen_width, int(screen_height*1.8),key, mouse)


def level_up_menu(con, header, player, menu_width, screen_width, screen_height,key, mouse):
    options = ['Constitution (+20 HP, from {0})'.format(player.fighter.max_hp),
               'Strength (+1 attack, from {0})'.format(player.fighter.power),
               'Agility (+1 defense, from {0})'.format(player.fighter.defense)]

    menu(con, header, options, menu_width, screen_width, screen_height,key, mouse)


def character_screen(player, character_screen_width, character_screen_height, screen_width, screen_height,key, mouse):
    window = libtcod.console_new(character_screen_width, character_screen_height)

    libtcod.console_set_default_foreground(window, libtcod.white)

    libtcod.console_print_rect_ex(window, 0, 1, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, 'Character Information')
    libtcod.console_print_rect_ex(window, 0, 2, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, 'Level: {0}'.format(player.level.current_level))
    libtcod.console_print_rect_ex(window, 0, 3, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, 'Experience: {0}'.format(player.level.current_xp))
    libtcod.console_print_rect_ex(window, 0, 4, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, 'Experience to Level: {0}'.format(player.level.experience_to_next_level))
    libtcod.console_print_rect_ex(window, 0, 6, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, 'Maximum HP: {0}'.format(player.fighter.max_hp))
    libtcod.console_print_rect_ex(window, 0, 7, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, 'Attack: {0}'.format(player.fighter.power))
    libtcod.console_print_rect_ex(window, 0, 8, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, 'Defense: {0}'.format(player.fighter.defense))

    x = screen_width // 2 - character_screen_width // 2
    y = screen_height // 2 - character_screen_height // 2
    libtcod.console_blit(window, 0, 0, character_screen_width, character_screen_height, 0, x, y, 1.0, 0.7)


def message_box(con, header, width, screen_width, screen_height,key, mouse):
    menu(con, header, [], width, screen_width, screen_height,key, mouse)