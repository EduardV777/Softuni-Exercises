from .pokemon import Pokemon

class Trainer:

    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        for pokemoni in self.pokemons:
            if pokemon.name == pokemoni.name:
                return f"This pokemon is already caught"

        self.pokemons.append(pokemon)
        return f"Caught {pokemon.name} with health {pokemon.health}"
    
    def release_pokemon(self, pokemon_name: str):
        for k in range(0, len(self.pokemons)):
            if pokemon_name == self.pokemons[k].name:
                del self.pokemons[k]
                return f"You have released {pokemon_name}"
        
        return "Pokemon is not caught"

    def trainer_data(self):
        output = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"

        for k in range(0, len(self.pokemons)):
            output += "- " + self.pokemons[k].pokemon_details()

            if k != len(self.pokemons) - 1:
                output += "\n"

        return output
