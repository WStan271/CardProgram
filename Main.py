import random
class card:
    def __init__(self,suit,rank,value):
        self.suit = suit
        self.rank = rank
        self.value = value
    def ctoString(self):
        print("{} of {} value of {} ".format(self.suit,self.rank,self.value))
    def getSuit(self):
        return self.suit
    def getRank(self):
        return self.rank
    def getValue(self):
        return self.value    
class deck:
    def __init__(self,values):
        self.cards = []
        suits = ["Spades","Diamonds","Clubs","Hearts"]
        ranks = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
        for s in suits:
            for r in range(len(ranks)):
                self.cards.append(card(s,ranks[r],values[r]))
    def dtoString(self):
        for c in self.cards:
            c.ctoString()
    def shuffle(self):
        for i in range(0,len(self.cards),+1):
            r = random.randint(0,len(self.cards)-1)
            self.cards[i] , self.cards[r] = self.cards[r] , self.cards[i]
    def deal(self):
        return self.cards.pop()
class player:
    def __init__(self,name):
        self.hand = []
        self.name = name
    def draw(self, deck):
        self.hand.append(deck.deal())
        return self
    def showHand(self):
        for c in self.hand:
            c.ctoString()
    

    
    