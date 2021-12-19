from Main import card,deck,player
# you should never import from main.  Main imports from other things. Main's sole purpose is to be the start of the program / intiialize what program needs to start

# game class
# bj derives from game class
        #computeCardValue
        #setupGame()
def bjScore(hand):
        score = 0
        aces = 0
        for c in hand:
            score += c.getValue()      
                #self.getCardValue(card)
            if c.getRank() == "Ace":    
                aces += 1
        while aces > 0 and score > 21:  
            score -= 10                
            aces -= 1
        
        return score
    
#playername = input("Enter username:")
# gameSEtup (numberOfPlayers)
        #instantiate each Player
        # + 1 dealer Player

player1 = player("Stan")
status = True #isGameActive
playerScore = 0
dealerScore = 0 # both should be in player class
print("Ok {} Lets play BlackJack\n".format(player1.name)) # this should be in black jack game class
bjDeck = deck([2,3,4,5,6,7,8,9,10,10,10,10,11])
bjDeck.shuffle()
dealer = player("Dealer")


# gameStart
dealer.draw(bjDeck)
dealer.draw(bjDeck)
player1.draw(bjDeck)
player1.draw(bjDeck)
print("{}'s hand:".format(player1.name))
player1.showHand()
print("\n{}'s hand:".format(dealer.name))
print("One facedown card")
#dealer.hand[1].ctoString()
dealer.showHand(showHidden)

#Loop that runs the entire Black Jack game
while status == True: 
    playerMove = input("\nHit(1) or Stand(2) \n")
        # parsePlayerInput
                #immediately validate good vs. bad input
                #return enumeration of type PLAYER_ACTION
                
     
        #playerGetInput should be different per BJHumanPlayer class vs BJDealerPlayer class
                #HumanPlayer should have the input above
                #DealerPlayer should have the AI 16 points, ect. logic below
            
     # the big if block below, is really a loop over allPlayers.GetAction() / executateAction


    #if playerMove == "1":
    if playerMove == PLAYER_ACTION.HIT:
        print("You choose hit\n")
        #player1.draw(bjDeck) # dealer.deals player receives card delt
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
        print("\nDealer score:{}".format(dealerScore)) #playerPrintScore
        print("Player score:{}\n".format(playerScore))
        #If dealer score is 16 or under they must draw another card
        if dealerScore <= 16: 
            print("Dealer score is under 17 and must draw\n")
            dealer.draw(bjDeck)
            print("Dealer hand is now:")   
            dealer.showHand()
            dealerScore = bjScore(dealer) 
            print("\nDealer score:{}".format(dealerScore)) 
        
        #evaluateWinCondition
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
    
   
    
    
    
    
    
