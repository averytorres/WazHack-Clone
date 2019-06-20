from random import randint


def get_generic_death():
    deaths = []

    deaths.append('{0} is dead!')
    deaths.append('{0} slumps over!')
    deaths.append('{0} slumps over!')
    deaths.append('{0} loses the will to survive!')

    return deaths[randint(0, len(deaths) - 1)]