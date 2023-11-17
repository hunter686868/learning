def take_damage(building, attacker):
    building.health -= attacker.damage * 0.5
    print(f'Здоровье здания {building.health}')


def receive_damage(building, dmg):
    building.health -= dmg * 0.5
    print(f'Здоровье здания {building.health}')