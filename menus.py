import tcod as libtcod
import math
from menu_info.menu_details import get_main_menu_options
from menu_info.menu_details import get_menu_width, get_menu_title, get_menu_height
from action_handlers.quaff_inventory_index_ih import get_quaff_inventory_index_options
from action_handlers.weapon_inventory_index_ih import get_weapon_inventory_index_options
from action_handlers.armor_inventory_index_ih import get_armor_inventory_index_options
from action_handlers.scroll_inventory_index_ih import get_scroll_inventory_index_options
from action_handlers.inventory_index_ih import get_inventory_index_options, set_inventory_index
from global_operations import colorize_text, colorize_text_custom
from game_states import GameStates


def menu(con, header, options, width, SCREEN_WIDTH, SCREEN_HEIGHT,key, mouse,menu_name,offset=3):
    width += 5
    header = colorize_text(header, libtcod.COLCTRL_2)
    if len(options) > 26:
        raise ValueError("Cannot have a menu with more than 26 options")

    # Calculate total height for the header (after auto-wrap) and one line per options
    if header == "":
        header_height = 0
    else:
        header_height = libtcod.console_get_height_rect(con, 0, 0, width, SCREEN_HEIGHT, header)

    header_height +=1
    height = len(options) + header_height
    height += 8

    # Create an off-screen console that represents the menu's window
    window = libtcod.console_new(width, height)

    # Print the header, with auto-wrap
    libtcod.console_set_default_foreground(window, libtcod.white)

    border_corner = "*"
    border_top_bottom = "="
    border_left_right = "|"
    menu_border_tb=border_corner
    for x in range(width-3):
        menu_border_tb = str(menu_border_tb) + str(border_top_bottom)

    menu_border_tb = str(menu_border_tb) + str(border_corner)
    r,g,b = 255,102,102
    menu_border_tb = colorize_text_custom(menu_border_tb, r,g,b)
    libtcod.console_print_rect_ex(window, 0, 0, width, height, libtcod.BKGND_NONE, libtcod.LEFT, menu_border_tb)
    libtcod.console_print_ex(window, 0, 1, libtcod.BKGND_NONE, libtcod.LEFT, colorize_text_custom(border_left_right, r, g, b))
    libtcod.console_print_ex(window, width-2, 1, libtcod.BKGND_NONE, libtcod.LEFT, colorize_text_custom(border_left_right, r, g, b))
    libtcod.console_print_ex(window, 0, 2, libtcod.BKGND_NONE, libtcod.LEFT, colorize_text_custom(border_left_right, r, g, b))
    libtcod.console_print_ex(window, width-2, 2, libtcod.BKGND_NONE, libtcod.LEFT, colorize_text_custom(border_left_right, r, g, b))
    libtcod.console_print_ex(window, 0, 3, libtcod.BKGND_NONE, libtcod.LEFT, colorize_text_custom(border_left_right, r, g, b))
    libtcod.console_print_ex(window, width-2, 3, libtcod.BKGND_NONE, libtcod.LEFT, colorize_text_custom(border_left_right, r, g, b))
    libtcod.console_print_ex(window, 0, height-3, libtcod.BKGND_NONE, libtcod.LEFT, colorize_text_custom(border_left_right, r, g, b))
    libtcod.console_print_ex(window, width-2, height - 3, libtcod.BKGND_NONE, libtcod.LEFT,colorize_text_custom(border_left_right, r, g, b))
    # libtcod.console_print_ex(window, 0, len(options) + header_height, libtcod.BKGND_NONE, colorize_text_custom(border_left_right, r, g, b))
    libtcod.console_print_ex(window, 0, len(options) + header_height, libtcod.BKGND_NONE, libtcod.LEFT,colorize_text(border_left_right, libtcod.COLCTRL_5))
    libtcod.console_print_ex(window, width-2, len(options) + header_height, libtcod.BKGND_NONE, libtcod.LEFT,colorize_text_custom(border_left_right, r, g, b))
    libtcod.console_print_ex(window, 0, 4, libtcod.BKGND_NONE, libtcod.LEFT,
                             colorize_text_custom(border_left_right, r, g, b))
    libtcod.console_print_ex(window, width - 2, 4, libtcod.BKGND_NONE, libtcod.LEFT,
                             colorize_text_custom(border_left_right, r, g, b))
    libtcod.console_print_ex(window, 0, 5, libtcod.BKGND_NONE, libtcod.LEFT,
                             colorize_text_custom(border_left_right, r, g, b))
    libtcod.console_print_ex(window, width - 2, 5, libtcod.BKGND_NONE, libtcod.LEFT,
                             colorize_text(border_left_right, libtcod.COLCTRL_5))
    libtcod.console_print_rect_ex(window, 2, 3, width - 4, height, libtcod.BKGND_NONE, libtcod.LEFT, header)
    libtcod.console_print_rect_ex(window, 0, len(options) + header_height + 1, width, height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, "")
    libtcod.console_print_rect_ex(window, 0, len(options) + header_height + 2, width, height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, "")
    libtcod.console_print_rect_ex(window, 0, len(options) + header_height + 5, width, height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, menu_border_tb)

    libtcod.console_print_ex(window, 0, len(options) + header_height+3, libtcod.BKGND_NONE, libtcod.LEFT,
                             colorize_text(border_left_right, libtcod.COLCTRL_5))
    libtcod.console_print_ex(window, width - 2, len(options) + header_height+3, libtcod.BKGND_NONE, libtcod.LEFT,
                             colorize_text_custom(border_left_right, r, g, b))
    libtcod.console_print_ex(window, 0, len(options) + header_height + 4, libtcod.BKGND_NONE, libtcod.LEFT,
                             colorize_text(border_left_right, libtcod.COLCTRL_5))
    libtcod.console_print_ex(window, width - 2, len(options) + header_height + 4, libtcod.BKGND_NONE, libtcod.LEFT,
                             colorize_text_custom(border_left_right, r, g, b))
    libtcod.console_print_ex(window, 0, header_height + 2, libtcod.BKGND_NONE, libtcod.LEFT,
                             colorize_text_custom(border_left_right, r, g, b))
    libtcod.console_print_ex(window, width - 2, header_height + 2, libtcod.BKGND_NONE, libtcod.LEFT,
                             colorize_text_custom(border_left_right, r, g, b))


    # Print all the options
    y = header_height
    letter_index = ord("a")

    libtcod.console_print_rect_ex(window, 0, len(options) + header_height, width, height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, "")
    y = header_height + 3
    for option_text in options:
        colorize_letter = colorize_text_custom('({0})', 102,255,204)
        text = colorize_letter+" {1}"
        text = text.format(chr(letter_index), option_text)
        libtcod.console_print_ex(window, 0, y, libtcod.BKGND_NONE, libtcod.LEFT, colorize_text_custom(border_left_right, r, g, b))
        libtcod.console_print_ex(window, width-2, y, libtcod.BKGND_NONE, libtcod.LEFT, colorize_text_custom(border_left_right, r, g, b))
        libtcod.console_print_ex(window, 2, y, libtcod.BKGND_NONE, libtcod.LEFT, text)
        y += 1
        letter_index += 1

    # Calculate coordinates
    x = SCREEN_WIDTH / 2 - width / 2
    y = SCREEN_HEIGHT / 2 - height / 2

    # Compute x and y offsets to convert console position to menu position
    x_offset = x  # x is the left edge of the menu
    y_offset = y + (header_height - (header_height/4))  # The top edge of the menu

    # Now we'll blit the contents of "window" to the root console
    # The last two parameters of this next function control the foreground transparency
    # and the background transparency, respectively
    x = int(x)
    y = int(y)
    libtcod.console_blit(window, 0, 0, width, height, 0, x, y, 1.0, 0.7)

    current_index = offset - 1
    while True:
        (menu_x, menu_y) = (mouse.cx - x_offset, mouse.cy - y_offset)
        custom_offset = offset
        if menu_x >= 0 and menu_x < width and menu_y >= 0 and menu_y < height - header_height:

            menu_y = int(math.ceil(menu_y)) - 1
            if menu_y >= custom_offset and menu_y < len(options) + custom_offset:
                current_index = menu_y
                window.draw_rect(1, int(menu_y + custom_offset + 1), width - custom_offset-1, 1, ch=0, bg=libtcod.darker_gray)
                libtcod.console_print_ex(window, 1, menu_y+custom_offset+1, libtcod.BKGND_NONE, libtcod.LEFT, ">")
                for i in range(height):
                    if i > 0 and i <= height - 5 and i != menu_y+custom_offset+1:
                        window.draw_rect(1, i, width-custom_offset, 1, ch=0, bg=libtcod.black)
                        libtcod.console_print_ex(window, 1, i, libtcod.BKGND_NONE, libtcod.LEFT,
                                                 colorize_text_custom(">", 1, 1, 1))

                libtcod.console_blit(window, 0, 0, width, height, 0, x, y, 1.0, 0.7)
            else:
                menu_y = int(math.ceil(menu_y)) - 1
                if menu_y > 0 and menu_y <= height - 7:
                    for i in range(height):
                        if i > 0 and i <= height - 5:
                            window.draw_rect(1, i, width-custom_offset, 1, ch=0, bg=libtcod.black)
                            libtcod.console_print_ex(window, 1, i, libtcod.BKGND_NONE, libtcod.LEFT,
                                                     colorize_text_custom(">", 1, 1, 1))
                    libtcod.console_blit(window, 0, 0, width, height, 0, x, y, 1.0, 0.7)
        # else:
        #     for i in range(height):
        #         if i > 0 and i <= height-5:
        #             window.draw_rect(1, i, width-custom_offset, 1, ch=0, bg=libtcod.black)
        #             libtcod.console_print_ex(window, 1, i, libtcod.BKGND_NONE, libtcod.LEFT, colorize_text_custom(">",1,1,1))
        #     libtcod.console_blit(window, 0, 0, width, height, 0, x, y, 1.0, 0.7)
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
        if index >= 0 and index < len(options):
            return index

        key_char = chr(key.c)
        if key.vk == libtcod.KEY_UP or key_char == 'k':
            current_index -= 1
            menu_move = 0
            if GameStates.LEVEL_UP == menu_name:
                menu_move = 1

            if current_index < 3:
                current_index = 3
            if current_index > (2 + len(options)):
                current_index = 2 + len(options)

            for i in range(height):
                if i > 0 and i <= height - 5:
                    window.draw_rect(1, i, width - custom_offset, 1, ch=0, bg=libtcod.black)
                    libtcod.console_print_ex(window, 1, i, libtcod.BKGND_NONE, libtcod.LEFT,
                                             colorize_text_custom(">", 1, 1, 1))

            window.draw_rect(1, int(current_index + custom_offset - menu_move), width - custom_offset - 1, 1, ch=0,
                             bg=libtcod.black)
            libtcod.console_print_ex(window, 1, current_index + custom_offset, libtcod.BKGND_NONE, libtcod.LEFT,
                                     colorize_text_custom(">", 1, 1, 1))
            window.draw_rect(1, int(current_index + custom_offset + 1 - menu_move), width - custom_offset - 1, 1, ch=0,
                             bg=libtcod.darker_gray)
            libtcod.console_print_ex(window, 1, current_index + custom_offset + 1 - menu_move, libtcod.BKGND_NONE, libtcod.LEFT,
                                     ">")
            libtcod.console_blit(window, 0, 0, width, height, 0, x, y, 1.0, 0.7)

        elif key.vk == libtcod.KEY_DOWN or key_char == 'j':
            current_index += 1
            menu_move = 0
            if GameStates.LEVEL_UP == menu_name:
                menu_move = 1

            if current_index < 3:
                current_index = 3
            if current_index > (2 + len(options)):
                current_index = 2 + len(options)

            for i in range(height):
                if i > 0 and i <= height - 5:
                    window.draw_rect(1, i , width - custom_offset, 1, ch=0, bg=libtcod.black)
                    libtcod.console_print_ex(window, 1, i, libtcod.BKGND_NONE, libtcod.LEFT,
                                             colorize_text_custom(">", 1, 1, 1))

            window.draw_rect(1, int(current_index + custom_offset - menu_move), width - custom_offset - 1, 1, ch=0,
                             bg=libtcod.black)
            libtcod.console_print_ex(window, 1, current_index + custom_offset - menu_move, libtcod.BKGND_NONE, libtcod.LEFT,
                                     colorize_text_custom(">", 1, 1, 1))
            window.draw_rect(1, int(current_index + custom_offset + 1 - menu_move), width - custom_offset - 1, 1, ch=0,
                             bg=libtcod.darker_gray)
            libtcod.console_print_ex(window, 1, current_index + custom_offset + 1 - menu_move, libtcod.BKGND_NONE, libtcod.LEFT, ">")
            libtcod.console_blit(window, 0, 0, width, height, 0, x, y, 1.0, 0.7)

        elif key.vk == libtcod.KEY_ENTER:
            current_index = int(math.ceil(current_index))
            set_inventory_index(current_index)
            return current_index

        # If they hit a letter that is not an option, return None
        if index >= 0 and index <= 26:
            return None


def main_menu_priv(con, header, options, width, SCREEN_WIDTH, SCREEN_HEIGHT,key, mouse,menu_name):

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
    y_offset = y + (header_height - (header_height/4))  # The top edge of the menu

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
            menu_y = menu_y +.5
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
        if index >= 0 and index < len(options):
            return index

        # If they hit a letter that is not an option, return None
        if index >= 0 and index <= 26:
            return None


def inventory_menu(con, header, player, inventory_width, screen_width, screen_height,key, mouse,game_state):
    # show a menu with each item of the inventory as an option
    if len(player.inventory.items) == 0:
        options = ['Inventory is empty.']
    else:
        options = get_inventory_index_options(player)

    menu(con, header, options, inventory_width, screen_width, screen_height,key, mouse,game_state)


def weapon_inventory_menu(con, header, player, inventory_width, screen_width, screen_height,key, mouse,game_state):
    # show a menu with each weapon item of the inventory as an option
    options = get_weapon_inventory_index_options(player)
    if len(options) == 0:
        options = ['Weapon inventory is empty.']

    menu(con, header, options, inventory_width, screen_width, screen_height,key, mouse,game_state)


def armor_inventory_menu(con, header, player, inventory_width, screen_width, screen_height,key, mouse,game_state):
    # show a menu with each weapon item of the inventory as an option
    options = get_armor_inventory_index_options(player)
    if len(options) == 0:
        options = ['Armor inventory is empty.']

    menu(con, header, options, inventory_width, screen_width, screen_height,key, mouse,game_state)


def scroll_inventory_menu(con, header, player, inventory_width, screen_width, screen_height,key, mouse,game_state):
    # show a menu with each scroll item of the inventory as an option
    options = get_scroll_inventory_index_options(player)
    if len(options) == 0:
        options = ['Scroll inventory is empty.']

    menu(con, header, options, inventory_width, screen_width, screen_height,key, mouse,game_state)


def quaff_inventory_menu(con, header, player, inventory_width, screen_width, screen_height,key, mouse,game_state):
    # show a menu with each scroll item of the inventory as an option
    options = get_quaff_inventory_index_options(player)
    if len(options) == 0:
        options = ['Quaff inventory is empty.']

    menu(con, header, options, inventory_width, screen_width, screen_height,key, mouse,game_state)


def main_menu(con, background_image, screen_width, screen_height,window_title,key, mouse,game_state):
    libtcod.image_blit_2x(background_image, None, 0, 0, sx=0, sy=0, w=-1, h=-1)

    libtcod.console_set_default_foreground(0, libtcod.light_yellow)
    libtcod.console_print_ex(0, int(screen_width / 2), int(screen_height*.9) - 4, libtcod.BKGND_NONE, libtcod.CENTER,
                             window_title)
    libtcod.console_print_ex(0, int(screen_width / 2), int(screen_height - 2), libtcod.BKGND_NONE, libtcod.CENTER,
                             '')
    main_menu_priv(con, get_menu_title(game_state), get_main_menu_options(), get_menu_width(game_state), screen_width, get_menu_height(screen_height),key, mouse,game_state)


def level_up_menu(con, header, player, menu_width, screen_width, screen_height,key, mouse,game_state,options):
    menu(con, header, options, menu_width, screen_width, screen_height,key, mouse,game_state,offset=2)


def character_screen(title, player, character_screen_width, character_screen_height, screen_width, screen_height,key, mouse,game_state):
    window = libtcod.console_new(character_screen_width, character_screen_height)

    libtcod.console_set_default_foreground(window, libtcod.white)

    libtcod.console_print_rect_ex(window, 0, 1, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
                                  libtcod.LEFT, title)
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


def message_box(con, header, width, screen_width, screen_height,key, mouse,game_state):
    menu(con, header, [], width, screen_width, screen_height,key, mouse,game_state)