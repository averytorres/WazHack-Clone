from item_probability.weapon_chances_values.knive_chances import get_knive_chances
from item_probability.weapon_chances_values.sword_chances import get_sword_chances
from item_probability.weapon_chances_values.greatsword_chances import get_greatsword_chances
from item_probability.weapon_chances_values.backsword_chances import get_backsword_chances
from item_probability.weapon_chances_values.axe_chances import get_axe_chances
from item_probability.weapon_chances_values.club_chances import get_club_chances
from item_probability.weapon_chances_values.polearm_chances import get_polearm_chances
from item_probability.weapon_chances_values.bow_chances import get_bow_chances
from item_probability.weapon_chances_values.throwing_chances import get_throwing_chances
from item_probability.weapon_chances_values.arrow_chances import get_arrow_chances


def get_weapon_chances(game_map):
    chances = {}

    chances.update(get_knive_chances(game_map))
    chances.update(get_sword_chances(game_map))
    chances.update(get_greatsword_chances(game_map))
    chances.update(get_backsword_chances(game_map))
    chances.update(get_axe_chances(game_map))
    chances.update(get_club_chances(game_map))
    chances.update(get_polearm_chances(game_map))
    chances.update(get_bow_chances(game_map))
    chances.update(get_throwing_chances(game_map))
    chances.update(get_arrow_chances(game_map))

    return chances
