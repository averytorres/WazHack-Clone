from random import randint


def get_generic_attack(is_pc):
    attacks = []

    if is_pc:
        attacks.append('{0} attack {1} for {2} hit points.')
        attacks.append('{0} hit {1} generating {2} hit points to be lost.')
        attacks.append('{0} whack {1} causing {2} hit points to drop.')
        attacks.append('{0} barrage {1} leading to {2} hit points lost.')
        attacks.append('{0} strike {1} for {2} hit points.')
    else:
        attacks.append('{0} attacks {1} for {2} hit points.')
        attacks.append('{0} hits {1} causing {2} hit points to drop.')
        attacks.append('{0} barrages {1} generating {2} hit points to be lost.')
        attacks.append('{0} strikes {1} leading to {2} hit points lost.')

    return attacks[randint(0, len(attacks) - 1)]