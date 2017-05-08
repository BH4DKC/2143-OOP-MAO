import random #import necessary libraray for the project


class RoulettWheel(object):
    def __init__(self):
        """
        @Function: __init__
        @Description: initiate the class
        @Returns: no return
        """
        self.wheel=['00']
        for i in range(36):
            self.wheel.append(i)

    def spin(self):
        """
        @Function: spin
        @Description: random select a number in wheel and return its color
        @Returns: a class include number selected, color, even/odd
        """
        self.result={}
        self.number=random.choice(self.wheel) #random choice from the wheel
        self.result["number"]=self.number
        if self.number == 0 or self.number == '00': #determine the wheel's color and evern or odd
            self.result["color"] = 'green'
            self.result["div2"] = 'None'
        elif self.number <=10:
            if self.number%2 == 1:
                self.result["color"] = 'red'
                self.result["div2"] = 'odd'
            else:
                self.result["color"] = 'black'
                self.result["div2"] = 'even'
        elif self.number <= 18:
            if self.number%2 == 1:
                self.result["color"] = 'black'
                self.result["div2"] = 'odd'
            else:
                self.result["color"] = 'red'
                self.result["div2"] = 'even'
        elif self.number <= 28:
            if self.number%2 == 1:
                self.result["color"] = 'red'
                self.result["div2"] = 'odd'
            else:
                self.result["color"] = 'black'
                self.result["div2"] = 'even'
        else:
            if self.number%2 == 1:
                self.result["color"] = 'black'
                self.result["div2"] = 'odd'
            else:
                self.result["color"] = 'red'
                self.result["div2"] = 'even'
        return self.result


class RoulettTable(object):
    def __init__(self):
        self.bet_payout = {35:["single"],17:["split"],8:["corner"],
                           2:["c1","c2","c3","d1","d2","d3"],1:["even","odd","red","black","1-18","19-36"]}
        # Define each type and what they include
        self.type = {"c1":[1,4,7,10,13,16,19,22,25,28,31,34],"c2":[2,5,8,11,14,17,20,23,26,29,32,35],
                     "c3":[3,6,9,12,15,18,21,24,27,30,33,36],"d1":[1,2,3,4,5,6,7,8,9,10,11,12],
                     "d2":[13,14,15,16,17,18,19,20,21,22,23,24],"d3":[25,26,27,28,29,30,31,32,33,34,35,36],
                     "even":[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36],
                     "odd":[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35],
                     "red":[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36],
                     "black": [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35],
                     "1-18":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],
                     "19-36":[19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]}
        self.bet_type = ["straight", "split", "corner", "c1","c2","c3","d1","d2","d3",
                         "even", "odd", "red", "black", "1-18", "19-36"]

    def payout(self, bet):
        """
        @Function: payout
        @Description: check bet type and decide pay
        @Returns: number of the payout
        """
        for k, v in self.bet_payout.items():
            if bet[0] in v:
                pao = k
        return pao


class Player(object):
    def __init__(self, name=None, total=0, bet_amount=0, bet=None):
        self.name = name
        self.total_bank = total
        self.current_bet_amount = bet_amount
        self.current_bet = bet

    def makebet(self, bet_amount=0, bet=None):
        self.current_bet_amount = bet_amount
        self. current_bet = bet


class Game(object):
    def __init__(self,name=None, total=0):
        self.current_player = Player(name, total)
        self.wheel = RoulettWheel()
        self.table = RoulettTable()

    def start(self):
        self.result = self.wheel.spin() #generate the result
        self.p = self.table.payout(self.current_player.current_bet)
        pass

    def result(self): # returns how much payout and what kind of win
        pass

a=RoulettWheel()
print(a.spin())
