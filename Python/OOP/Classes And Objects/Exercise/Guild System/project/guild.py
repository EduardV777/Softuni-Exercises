from project.player import Player

class Guild:
    
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if not player.guild == self.name and player.guild == "Unaffiliated":
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"

        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        foundPlayer = False

        for k in range(0, len(self.players)):
            if self.players[k].name == player_name:
                foundPlayer = True
                self.players[k].guild = "Unaffiliated"
                del self.players[k]
                break

        if foundPlayer == True:
            return f"Player {player_name} has been removed from the guild."
        else:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        output = f"Guild: {self.name}\n"

        for k in range(0, len(self.players)):
            output += self.players[k].player_info()

            if k != len(self.players) - 1:
                output += "\n"
            
        return output