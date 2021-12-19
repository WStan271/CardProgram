import random
class pokerCard:
    def __init__(self,suit,rank,value):
        self.suit = suit
        self.rank = rank
        self.value = value # DON'T KEEP VALUE HERE. Because its game dependent. So card becomes tainted, can't be reused across other games.
    def toString(self):
        print("{} of {} value of {} ".format(self.suit,self.rank,self.value))
    def getSuit(self):
        return self.suit
    def getRank(self):
        return self.rank
    def getValue(self):
        return self.value    
    
    #suits = ["Spades","Diamonds","Clubs","Hearts"]  # https://docs.python.org/3/library/enum.html
    #ranks = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]

    # DeckBuilderClass / GenerateCards
    for s in suits:
       for r in range(len(ranks)):
            self.cards.append(card(s,ranks[r],values[r]))
    
class deck:
    def __init__(self, generateCards):
        self.cards = generateCards()

    def toString(self):
        for c in self.cards:
            c.toString()
    def shuffle(self):
        for i in range(0,len(self.cards),+1):
            r = random.randint(0,len(self.cards)-1)
            self.cards[i] , self.cards[r] = self.cards[r] , self.cards[i]
    def deal(self):
        return self.cards.pop()
    # def returnCard(card)
        # self.cards.push(card)

class player:
    def __init__(self,name):
        self.hand = []
        self.name = name

    def draw(self, card):
        self.hand.append(card)
        return self

    def showHand(self):
        for c in self.hand:
            c.ctoString()
            
  # class dealer # derives from player
    # owns The deck
    # deal(card)
    

    
    
