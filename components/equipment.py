from equipment_slots import EquipmentSlots


class Equipment:
    def __init__(self, main_hand=None, off_hand=None, head=None, neck_1=None, neck_2=None, eyes=None,
                 right_ear=None, left_ear=None, face=None, chest=None, fingers=None,
                 hands=None, legs=None, feet=None, back=None):
        self.main_hand = main_hand
        self.off_hand = off_hand
        self.head = head
        self.neck_1 = neck_1
        self.neck_2 = neck_2
        self.eyes = eyes
        self.right_ear = right_ear
        self.left_ear = left_ear
        self.face = face
        self.chest = chest
        self.fingers = fingers
        self.hands = hands
        self.legs = legs
        self.feet = feet
        self.back = back

    @property
    def max_hp_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.max_hp_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.max_hp_bonus

        return bonus

    @property
    def power_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.power_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.power_bonus

        return bonus

    @property
    def defense_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.defense_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.defense_bonus

        return bonus

    def toggle_equip(self, equippable_entity):
        results = []

        slot = equippable_entity.equippable.slot
        attr_name = str(get_attribute_name(slot))
        curr_slot = getattr(self,attr_name)
        curr_slot,results = compute_equipable_action(equippable_entity, curr_slot, results)
        setattr(self, attr_name, curr_slot)

        return results


def compute_equipable_action(equippable_entity,curr_slot,results):
    if curr_slot == equippable_entity:
        curr_slot = None
        results.append({'dequipped': equippable_entity})
    else:
        if curr_slot:
            results.append({'dequipped': curr_slot})

        curr_slot = equippable_entity
        results.append({'equipped': equippable_entity})
    return curr_slot,results


def get_attribute_name(slot):
    attribute_name = str(slot).replace("EquipmentSlots.", "").lower()
    return attribute_name
