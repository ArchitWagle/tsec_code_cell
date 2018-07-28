def game(n):
    if(n%3==0):
        return 2
    else:
        return 1
    
print(game(22)+game(45)+game(26)+game(75))
#Using invariants
#let P(n) return W if player 1 wins with n marbles and L if player 1 cant win
#P(1) = W
#P(2) = W
#P(3) = L
#for n=4 player 1 can either go to state n = 3 or n = 1
#since he is playing optimally he will go to state 3 to give a losing position to player 2 in next round
#continue the sequence
