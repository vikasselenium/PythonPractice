

class Player:


    def __init__(self,x,y):
        self.x=0
        self.y=0

    def move_up(self, change=5):
        self.y= self.y+change

    def move_down(self, change=5):
        self.y= self.y-change

    def move_left(self, change=2):
        self.x = self.x-change

    def move_right(self, change=2):
        self.x = self.x+change

player1=Player(4,5)
print(player1.x,player1.y)

player1.move_up()
print(player1.x,player1.y)

player1.move_up()
print(player1.x,player1.y)


player1.move_down()
print(player1.x,player1.y)
print(player1.x,player1.y)

player1.move_up(49)
print(player1.x,player1.y)