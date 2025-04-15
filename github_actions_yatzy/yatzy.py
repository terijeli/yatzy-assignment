import random

class Yatzy:
    def __init__(self):
        self.dice = [random.randint(1, 6) for _ in range(5)]
        self.locked = [False] * 5

    def roll(self):
        for i in range(5):
            if not self.locked[i]:
                self.dice[i] = random.randint(1, 6)

    def lock_dice(self, index):
        if 0 <= index < 5:
            self.locked[index] = True

    def unlock_dice(self, index):
        if 0 <= index < 5:
            self.locked[index] = False

    def score_number(self, number):
        return self.dice.count(number) * number

    def Ones(self): return self.score_number(1)
    def Twos(self): return self.score_number(2)
    def Threes(self): return self.score_number(3)
    def Fours(self): return self.score_number(4)
    def Fives(self): return self.score_number(5)
    def Sixes(self): return self.score_number(6)

    def OnePair(self):
        for i in range(6, 0, -1):
            if self.dice.count(i) >= 2:
                return i * 2
        return 0

    def TwoPairs(self):
        pairs = []
        for i in range(6, 0, -1):
            if self.dice.count(i) >= 2:
                pairs.append(i)
            if len(pairs) == 2:
                return sum(p * 2 for p in pairs)
        return 0

    def ThreeAlike(self):
        for i in range(6, 0, -1):
            if self.dice.count(i) >= 3:
                return i * 3
        return 0

    def FourAlike(self):
        for i in range(6, 0, -1):
            if self.dice.count(i) >= 4:
                return i * 4
        return 0

    def Small(self):
        if sorted(self.dice) == [1, 2, 3, 4, 5]:
            return 15
        return 0

    def Large(self):
        if sorted(self.dice) == [2, 3, 4, 5, 6]:
            return 20
        return 0

    def FullHouse(self):
        values = set(self.dice)
        if len(values) == 2:
            if self.dice.count(list(values)[0]) in [2, 3] and self.dice.count(list(values)[1]) in [2, 3]:
                return sum(self.dice)
        return 0

    def Chance(self):
        return sum(self.dice)

    def Yatzy(self):
        if self.dice.count(self.dice[0]) == 5:
            return 50
        return 0
