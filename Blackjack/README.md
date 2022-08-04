# Blackjack

https://en.wikipedia.org/wiki/Blackjack  

Blackjack is the most widely played casino banking game in the world. 
It uses decks of 52 cards, it's also known as Twenty-One. 
In the game, the players compete only against the dealer.   

This is a simplified version of the popular game Blackjack, written in Python. 
The game keeps track of the probability of cards based on the decks played 
and cards removed from them. The base scenario is with 8 decks of cards and 
after playing 2 decks of cards, all decks will get reshuffled, in order to 
reset the probabilities.   

First, the user is asked to state the number of HumanPlayers 
(anything between 1-4 is a valid number). Next, each player has to write down 
his/her name and the amount of money brought to the table. The bet size is set 
to a constant value of $20.00. In each game, the dealer starts by taking 
two cards, but showing only the first card. In the next step, each of the 
users will get one card and will be continuously asked about another card until 
they decide not to take any more cards or leave the table. In case of choosing 
to leave the table, the user will lose his/her bet of $20.00 and be removed 
from the list of players. In the case of choosing not to take any more cards, 
the points will be calculated based on the cards on hand. 
If the points are above 21, it will result in an automatic loss, 
and if the points are equal or less than 21, the dealer will finish picking 
his cards based on the rule: taking a card until the points are less than 17. 
In the next step, based on the blackjack rules, points will be calculated and 
determined who won. Winning will result in changing the balance of the user 
by adding $20.00 and losing will result in a deduction of the same amount. 
  
If any user has a balance that is less than the minimum bet of $20.00 they will 
be removed from the list of players and asked to leave the table. 
The program will stop executing when the list of players is empty.  
 
To run the game, simply execute the main_blackjack.py