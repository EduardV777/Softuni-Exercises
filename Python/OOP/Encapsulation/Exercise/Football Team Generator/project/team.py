from project.player import Player

class Team:

    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player):
        for k in range(0, len(self.__players)):
            if self.__players[k].name == player.name:
                return f"Player {player.name} has already joined"
        
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        for k in range(0, len(self.__players)):
            if self.__players[k].name == player_name:
                res = self.__players[k]
                del self.__players[k]
                return res
        
        return f"Player {player_name} not found"