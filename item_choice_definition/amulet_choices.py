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


def get_amulet_choice(item_choice, x, y):
    suffix = '-amulet'
    display_icon = 'o'
    display_color = libtcod.gold
    equipment_slot = EquipmentSlots.NECK_1

    disp_name = item_choice.replace(suffix,"")
    item = None

    if item_choice == 'Amulet of Dweomery' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=3)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Amulet of ESP' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Amulet of Life Saving' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Amulet of magical breathing' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Amulet of Reflection' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Amulet of Restful Sleep' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Amulet of Slow Digestion' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Amulet of Strangulation' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Amulet of Unchanging' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'Amulet of Versus Poison' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)
    elif item_choice == 'The Amulet of Zaw' + suffix:
        equippable_component = Equippable(equipment_slot, power_bonus=1)
        item = Entity(x, y, display_icon, display_color, disp_name, equippable=equippable_component)

    return item
