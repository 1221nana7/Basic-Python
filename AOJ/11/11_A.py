class Dice:
    def __init__(self, num):
        self.top = num[0]
        self.east = num[1]
        self.north = num[2]
        self.south = num[3]
        self.west = num[4]
        self.bottom = num[5]
        

    def roll_E(self):#E右に回転
        t = self.top
        self.top = self.south
        self.south = self.bottom
        self.bottom = self.north
        self.north = t

    def roll_N(self):#N後ろに回転
        t = self.top
        self.top = self.east
        self.east = self.bottom
        self.bottom = self.west
        self.west = t

    def roll_S(self):#S前に回転
        t = self.top
        self.top = self.west
        self.west = self.bottom
        self.bottom = self.east
        self.east = t

    def roll_W(self):#W左に回転
        t = self.top
        self.top = self.north
        self.north = self.bottom
        self.bottom = self.south
        self.south = t
    
    def roll(self, order):
        for i in order:
            if i == 'E':
                self.roll_E()
            elif i == 'N':
                self.roll_N()
            elif i == 'S':
                self.roll_S()
            elif i == 'W':
                self.roll_W()
    #上面を表示
    def dice_top(self):
        print(self.top)
        

dice_side = list(map(int, input().split()))
line = input()

dice = Dice(dice_side)
dice.roll(line)
dice.dice_top()
