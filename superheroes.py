from random import randint

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
            total_damage += ability.attack()
        return total_damage

    # Add armor to self.armors = Armor object
    def add_armor(self, armor):
        self.armors.append(armor)

    # Runs 'block' method on each armor.
    def defend(self, damage_amt):
        blocked = 0
        for armor in self.armors:
            block = armor.block()
            blocked += block
        return blocked - damage_amt

    # Updates self.current_health to reflect the damage minus the defense
    def take_damage(self, damage):
        current_heath = self.current_health
        damage_defense = self.defend(damage)

        self.current_health = current_heath - damage_defense

    # Returns true or false depending on whether the hero is alive or not
    def is_alive(self):
        return self.current_health > 0

    # Current hero will take turns fighting the opponent hero passed in and determines who wins
    def fight(self, opponent):
        while self.is_alive() and opponent.is_alive():
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())

            if opponent.current_health < self.current_health:
                print(f'{self.name} won!')
                self.add_kill(1)
                opponent.add_deaths(1)
            else:
                print(f'{opponent.name} beat {self.name} and won!')
                opponent.add_kill(1)
                self.add_deaths(1)
            break

    # Update kills with num_kills and add the number of kills to self.kills
    def add_kill(self, num_kills):
        self.kills += num_kills

    # Update deaths with num_deaths and add the number of deaths to self.deaths
    def add_deaths(self, num_deaths):
        self.deaths += num_deaths


if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 20)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
