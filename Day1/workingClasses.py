class Character:
    def __init__(self, name, speed, health):
        self.name = name
        self.speed = speed
        self.health = health


    def ShowStats(self):
        return f'Player {self.name} stats: \n Speed: {self.speed} Health: {self.health}'



# create the character

player = Character('kurt',80,100)

print(player.ShowStats())