from random import randint, shuffle

# TODO: Add better comments/doc strings


class Ability:
    # Instance properties
    def __init__(self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
        # Return a value between 0 and the value set by self.max_damage
        return randint(0, self.max_damage)


class Armor:
    # Instance properties
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return randint(0, self.max_block)


class Hero:
    # Instance properties
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.kills = 0
        self.deaths = 0

    # Add ability to abilities list
    def add_ability(self, ability):
        self.abilities.append(ability)

    # Calculate the total damage from all ability attacks
    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_dmg += ability.attack()
        return total_damage

    # Add armor to self.armors = Armor object
    def add_armor(self, armor):
        self.armors.append(armor)
