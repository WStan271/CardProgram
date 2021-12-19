from Main import card,deck,player

def bjScore(hand):
        score = 0
        aces = 0
        for c in hand:
            score += c.getValue()      
            if c.getRank() == "Ace":    
                aces += 1
        while aces > 0 and score > 21:  
            score -= 10                
        aces -= 1
        return score
    
#playername = input("Enter username:")
player1 = player("Stan")
status = True 
playerScore = 0
dealerScore = 0
print("Ok {} Lets play BlackJack\n".format(player1.name))
bjDeck = deck([2,3,4,5,6,7,8,9,10,10,10,10,11])
bjDeck.shuffle()
dealer = player("Dealer")
dealer.draw(bjDeck)
dealer.draw(bjDeck)
player1.draw(bjDeck)
player1.draw(bjDeck)
print("{}'s hand:".format(player1.name))
player1.showHand()
print("\n{}'s hand:".format(dealer.name))
print("One facedown card")
dealer.hand[1].ctoString()

#Loop that runs the entire Black Jack game
while status == True: 
    playerMove = input("\nHit(1) or Stand(2) \n")
     
    if playerMove == "1":
        print("You choose hit\n")
        player1.draw(bjDeck)
        player1.showHand()
        playerScore = bjScore(player1)
        print("\nPlayer score:{}".format(playerScore))
        if playerScore>21:
            print("\nYou busted")
            status = False
        
    elif playerMove == "2":
        print("You choose stand\n")
        #flip dealer cards then check if win or lose
        print("Dealers flips hidden card:")
        dealer.showHand() 
        playerScore = bjScore(player1)
        dealerScore = bjScore(dealer)
        print("\nDealer score:{}".format(dealerScore))
        print("Player score:{}\n".format(playerScore))
        #If dealer score is 16 or under they must draw another card
        if dealerScore <= 16: 
            print("Dealer score is under 17 and must draw\n")
            dealer.draw(bjDeck)
            print("Dealer hand is now:")   
            dealer.showHand()
            dealerScore = bjScore(dealer) 
            print("\nDealer score:{}".format(dealerScore)) 
        
        if playerScore == dealerScore:
            print("\nTie no one wins")
            status = False
        elif dealerScore>21:
            print("\nDealer busted you win")
            status = False
        elif playerScore > dealerScore:
            print("\nPlayer wins")
            status = False
        elif playerScore < dealerScore:
            print("\nDealer wins")
            status = False
    #Incase user doesn't give 1 or 2
    else: 
        print("\nNot an option")
        continue
    
   
    
    
    
    
    