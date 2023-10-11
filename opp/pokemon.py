#inheritance

class Pokemon:
    pass
    def __init__(self, pokemon_name, pokemon_type):
        self.pokemon_name = pokemon_name
        self.pokemon_type = pokemon_type

    def description(self):
        return '{} is a {} type pokemon'.format(self.pokemon_name, self.pokemon_type)
    

class Pikachu (Pokemon):
    def attack(self, attacktype):
        return '{} used {}!!!'.format(self.pokemon_name, attacktype)
    
class Charizard (Pokemon):
    def attack(self, attacktype):
        return 'Rival {} used {}!!!'.format(self.pokemon_name, attacktype)


player_pokemon = Pikachu('Pikachu', 'electric')
print(player_pokemon.description())
print(player_pokemon.attack("Volt Tackle"))
print(" ")
rival_pokemon = Charizard('Charizard', 'Fire/Flying')
print(rival_pokemon.description())
print(rival_pokemon.attack("Hades Flame"))
print(" ")
print("Rival Charizard fainted!!!")