import tcod as libtcod

from game_messages import Message
from messages.attacks import get_generic_attack


class Fighter:
    def __init__(self, hp, defense, power, xp=0):
        self.base_max_hp = hp
        self.hp = hp
        self.base_defense = defense
        self.base_power = power
        self.xp = xp

    @property
    def max_hp(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.max_hp_bonus
        else:
            bonus = 0

        return self.base_max_hp + bonus

    @property
    def power(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.power_bonus
        else:
            bonus = 0

        return self.base_power + bonus

    @property
    def defense(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.defense_bonus
        else:
            bonus = 0

        return self.base_defense + bonus

    def take_damage(self, amount):
        results = []

        self.hp -= amount

        if self.hp <= 0:
            results.append({'dead': self.owner, 'xp': self.xp})

        return results

    def heal(self, amount):
        self.hp += amount

        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def attack(self, target):
        results = []

        damage = self.power - target.fighter.defense

        if self.owner.is_pc == True:
            disp_name = 'You'.capitalize()
            target_disp_name = target.first_name.capitalize() + ' ' + target.last_name
        else:
            disp_name = self.owner.first_name.capitalize() + ' ' + self.owner.last_name
            target_disp_name = 'You'.capitalize()

        attack_disp = get_generic_attack(self.owner.is_pc)

        if damage >= 0:
            results.append({'message': Message(attack_disp.format(
                disp_name,target_disp_name, str(damage)), libtcod.white)})
            results.extend(target.fighter.take_damage(damage))
        else:
            damage = 0
            results.append({'message': Message(attack_disp.format(
                disp_name, target_disp_name, str(damage)), libtcod.white)})

        return results
