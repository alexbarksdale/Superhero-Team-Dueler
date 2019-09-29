from random import randint, choice


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
    def defend(self, damage_amt=0):
        blocked = 0
        for armor in self.armors:
            block = armor.block()
            blocked += block
        return blocked

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

            if opponent.current_health <= 0:
                print(f'{self.name} won!')
                self.add_kill(1)
                opponent.add_deaths(1)
                break
            elif self.current_health <= 0:
                print(f'{opponent.name} beat {self.name} and won!')
                opponent.add_kill(1)
                self.add_deaths(1)
                break
            else:
                # Its a tie
                pass

    # Update kills with num_kills and add the number of kills to self.kills

    def add_kill(self, num_kills):
        self.kills += num_kills

    # Update deaths with num_deaths and add the number of deaths to self.deaths
    def add_deaths(self, num_deaths):
        self.deaths += num_deaths

    def add_weapon(self, weapon):
        self.abilities.append(weapon)


class Weapon(Ability):
    # Method returns a random value between half the power to the full attack power of the weapon
    def attack(self):
        return randint(self.max_damage // 2, self.max_damage)


class Team():
    # Initialize your team with its team name
    def __init__(self, name):
        self.name = name
        self.hero_list = []

    # Remove hero from heroes list, if hero isn't found return 0
    def remove_hero(self, name):
        for hero in self.hero_list:
            if hero.name == name:
                self.hero_list.remove(hero)
                break
        return 0

    # Prints out all heroes in the console
    def view_all_heroes(self):
        for hero in self.hero_list:
            print(hero.name)

    # Add hero object to self.heroes
    def add_hero(self, hero):
        self.hero_list.append(hero)

    def team_alive(self):
        heroes = []
        for hero in self.hero_list:
            if hero.is_alive():
                heroes.append(hero)
        return heroes

    # Randomly picks heros to attack until all of them are dead.
    # Acknowledgement: Got help from Gary Frederick during lab.
    def attack(self, other_team):
        while len(self.team_alive()) > 0 and len(other_team.team_alive()) > 0:

            print(self.team_alive()[0].current_health)
            heroes = choice(self.team_alive())
            enemy_list = choice(other_team.team_alive())

            heroes.fight(enemy_list)

    # Resets all of the heroes health back to the starting health
    def revive_heroes(self, health=100):
        for heroes in self.hero_list:
            heroes.current_health = heroes.starting_health

    # Prints the kill to death ratio for each hero KD = Kill Death
    def stats(self):

        for hero in self.hero_list:
            print(f'{hero.name} has {hero.kills} kills and {hero.deaths} deaths')

            # If hero didn't die return the kills as the KD
            kd = hero.kills / hero.deaths if hero.deaths > 0 else hero.kills
            print(f'{hero.name} has a KD of: {kd}')
        # TODO return value to print


class Arena:

    # Instance variables that will hold teams
    def __init__(self):
        self.team_one = Team('Team 1 Heroes')
        self.team_two = Team('Team 2 Heroes')

    # Allow the user to create an ability
    def create_ability(self):
        ability_name = input('Create an ability name: ')
        damage_input = int(
            input('Enter the max amount of damage for your ability: '))

        return Ability(ability_name, damage_input)

    # Allow the user to create a weapon
    def create_weapon(self):
        weapon_name = input('Create a weapon name: ')
        weapon_damage = int(input('Enter how much damage your item will do: '))

        return Weapon(weapon_name, weapon_damage)

    # Allow the user to create a piece of armor
    def create_armor(self):
        armor_name = input('Create an armor name: ')
        block_input = int(input('Enter how much your armor will block: '))

        return Armor(armor_name, block_input)

    # Allows the user to create a hero and specifiy if they want armor, weapons and abilities
    def create_hero(self):

        hero_name = input('Enter the name of your hero: ')
        health_input = int(
            input('Enter how much health your hero will have: '))

        user_hero = Hero(hero_name, health_input)

        user_ability = self.create_ability()
        user_weapon = self.create_weapon()
        user_armor = self.create_armor()

        while True:
            ask_ability = input('Would you like abilities? (Y/N): ').lower()
            if ask_ability == 'y':
                user_hero.add_ability(user_ability)
                break
            elif ask_ability == 'n':
                break
            else:
                print('\nYou must answer Y or N')

        while True:
            ask_weapon = input('Would you like weapons? (Y/N): ').lower()
            if ask_weapon == 'y':
                user_hero.add_weapon(user_weapon)
                break
            else:
                print('\nYou must answer Y or N')

        while True:
            ask_armor = input('Would you like armor? (Y/N): ').lower()
            if ask_armor == 'y':
                user_hero.add_armor(user_armor)
                break
            else:
                print('\nYou must answer Y or N')

        return user_hero

    # Allows the user to create team one and ask if how many heroes they want for each team
    def build_team_one(self):

        add_hero_team = int(
            input('How many heroes would you like on team one? '))

        for amount in range(add_hero_team):
            self.team_one.add_hero(self.create_hero())

        hero_list = [hero.name for hero in self.team_one.hero_list]
        print(f'Heroes on Team 1: {", ".join(hero_list)}')

    def build_team_two(self):

        add_hero_team = int(
            input('How many heroes would you like on team two? '))

        for amount in range(add_hero_team):
            self.team_two.add_hero(self.create_hero())

        hero_list = [hero.name for hero in self.team_two.hero_list]
        print(f'Heroes on Team 2: {", ".join(hero_list)}')

    # Battles the teams together
    def team_battle(self):
        self.team_one.attack(self.team_two)

    # Prints out the battle statistics including the team's average KD ratio
    def show_stats(self):
        print(f'Team one\'s stats: {self.team_one.stats()}')
        print(f'Team two\'s stats: {self.team_two.stats()}')

        # if len(self.team_one) > 0:
        #    print('Team 1 Won!')
        # else:
        #    print('Team 2 Won!')


if __name__ == "__main__":
    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 20)
    # ability2 = Ability("Super Eyes", 130)
    # ability3 = Ability("Wizard Wand", 80)
    # ability4 = Ability("Wizard Beard", 20)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero1.fight(hero2)

    arena = Arena()

    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()
