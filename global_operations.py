import tcod as libtcod
import os


def colorize_text(text, color):
    format_text = '%c'+str(text)+'%c'
    output = format_text%(color, libtcod.COLCTRL_STOP)

    return str(output)


def colorize_text_custom(text,r,g,b):
    format_text = '%c%c%c%c'+str(text)+'%c'
    output = format_text%(libtcod.COLCTRL_FORE_RGB,r,g,b,libtcod.COLCTRL_STOP)

    return str(output)


def reset_game():
    if os.path.isfile('savegame'):
        os.remove("savegame")