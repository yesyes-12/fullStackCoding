class Player:
    
    def __init__(self, name, team):
        self.name = name
        self.xp = 1500
        self.team = team
        
    def introduce(self):
        print(f"Hello! im {self.name} and I play for {self.team}")

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []
        
    def add_player(self, name):
        new_player = Player(name, self.team_name)
        self.players.append(new_player)
        
    def show_players(self):
        for player in self.players:
            player.introduce()
            
    def delete_player(self, del_name):
        for player in self.players:
            if player.name == del_name:
                self.players.remove(player)
                print(f"{del_name} has been removed from {self.team_name}")
                
    def show_team_XP(self):
        total_XP = 0
        for player in self.players:
            total_XP += player.xp
        print(f"Total {self.team_name}'s XP: {total_XP}")
        

team_A = Team("Team A")

team_A.add_player("verm")

team_B = Team("Team B")

team_B.add_player("nico")
team_B.add_player("test2")
team_B.add_player("test4")

team_B.show_players()

team_B.delete_player("nico")

team_B.show_team_XP()
team_A.show_team_XP()