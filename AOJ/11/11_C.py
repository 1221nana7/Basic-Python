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
    
    #水平に回転
    def diceroll(self):
        t = self.north
        self.north = self.east
        self.east = self.south
        self.south = self.west
        self.west = t
    
    #同じサイコロ->True
    def samedice(self, dice):
        if self.top == dice.top and self.north == dice.north and self.east == dice.east and self.south == dice.south and self.west == dice.west and self.bottom == dice.bottom:
            return True
        else:
            return False
    #サイコロ1,4回転->サイコロ2,4回転->同じ->True
                                #->違う->False->水平回転->右に回転
    def judge(self, dice):
        for i in range(4):
            for j in range(4):
                if self.samedice(dice) == True:
                    return True
                self.diceroll()
            self.roll_E()
    #サイコロ1,4回転->サイコロ2,4回転->同じ->True
                                #->違う->False->水平回転->後ろに回転
        for i in range(4):
            for j in range(4):
                if self.samedice(dice) == True:
                    return True
                self.diceroll()
            self.roll_N()
        return False

dice1 = Dice(list(map(int,input().split())))
dice2 = Dice(list(map(int,input().split())))

if dice1.judge(dice2) == True:
    print("Yes")
else:
    print("No")
