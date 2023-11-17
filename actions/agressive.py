import building.damage.take_damage as take_damage


def attack(attacker, target):
    take_damage.take_damage(target, attacker)
    print(f'{attacker.name} атакует {target.name}')
