import tcod as libtcod
from components.equipment import EquipmentSlots
from components.equippable import Equippable
from entity import Entity
from item_choice_definition.weapon_choices_values.knive_choices import get_knife_choices
from item_choice_definition.weapon_choices_values.sword_choices import get_sword_choices
from item_choice_definition.weapon_choices_values.greatsword_choices import get_greatsword_choices
from item_choice_definition.weapon_choices_values.backsword_choices import get_backsword_choices
from item_choice_definition.weapon_choices_values.axe_choices import get_axe_choices
from item_choice_definition.weapon_choices_values.club_choices import get_club_choices
from item_choice_definition.weapon_choices_values.polearm_choices import get_polearm_choices
from item_choice_definition.weapon_choices_values.bow_choices import get_bow_choices
from item_choice_definition.weapon_choices_values.throwing_choices import get_throwing_choices
from item_choice_definition.weapon_choices_values.arrow_choices import get_arrow_choices


def get_weapon_choice(item_choice, x, y):
    wp_en = '-weapon'
    disp_name = item_choice.replace(wp_en,"")
    item = None

    if item is None:
        item = get_knife_choices(item_choice,wp_en,x,y,disp_name)
    if item is None:
        item = get_sword_choices(item_choice, wp_en, x, y, disp_name)
    if item is None:
        item = get_greatsword_choices(item_choice, wp_en, x, y, disp_name)
    if item is None:
        item = get_backsword_choices(item_choice, wp_en, x, y, disp_name)
    if item is None:
        item = get_axe_choices(item_choice, wp_en, x, y, disp_name)
    if item is None:
        item = get_club_choices(item_choice, wp_en, x, y, disp_name)
    if item is None:
        item = get_polearm_choices(item_choice, wp_en, x, y, disp_name)
    if item is None:
        item = get_bow_choices(item_choice, wp_en, x, y, disp_name)
    if item is None:
        item = get_throwing_choices(item_choice, wp_en, x, y, disp_name)
    if item is None:
        item = get_arrow_choices(item_choice, wp_en, x, y, disp_name)
    if item is None:
        equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=0)
        item = Entity(x, y, '?', libtcod.black, 'ERROR WEAPON'+item_choice, equippable=equippable_component)

    return item
