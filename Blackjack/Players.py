from random import choice

class Player:
    """base class for the player"""

    def __init__(self,name: str) -> None:
        self.name = name
        self._total_points = 0
        self.cards = {
            'A_Clubs': 0, '2_Clubs': 0, '3_Clubs': 0, '4_Clubs': 0, '5_Clubs': 0, '6_Clubs': 0, '7_Clubs': 0, '8_Clubs': 0, '9_Clubs': 0, '10_Clubs': 0, 'J_Clubs': 0, 'Q_Clubs': 0, 'K_Clubs': 0,
            'A_Diamonds': 0, '2_Diamonds': 0, '3_Diamonds': 0, '4_Diamonds': 0, '5_Diamonds': 0, '6_Diamonds': 0, '7_Diamonds': 0, '8_Diamonds': 0, '9_Diamonds': 0, '10_Diamonds': 0, 'J_Diamonds': 0, 'Q_Diamonds': 0, 'K_Diamonds': 0,
            'A_Hearts': 0, '2_Hearts': 0, '3_Hearts': 0, '4_Hearts': 0, '5_Hearts': 0, '6_Hearts': 0, '7_Hearts': 0, '8_Hearts': 0, '9_Hearts': 0, '10_Hearts': 0, 'J_Hearts': 0, 'Q_Hearts': 0, 'K_Hearts': 0,
            'A_Spades': 0, '2_Spades': 0, '3_Spades': 0, '4_Spades': 0, '5_Spades': 0, '6_Spades': 0, '7_Spades': 0, '8_Spades': 0, '9_Spades': 0, '10_Spades': 0, 'J_Spades': 0, 'Q_Spades': 0, 'K_Spades': 0,
        } 

    @property
    def _total_points(self) -> int:
        """returning the value of total points"""
        return self.__total_points

    @_total_points.setter
    def _total_points(self, value: int) -> None:
        """setting the value of total points"""

        if value < 0:
            print("_total_points cant be negative")
            raise ValueError("_total_points cant be negative")
        else:
            self.__total_points = value

    def reset_cards(self) -> None:
        """setting all cards to 0"""
        self.cards = {card_name : 0 for card_name in self.cards}

    def amount_of_cards(self) -> int:
        """returning the number of cards"""
        return sum([value for value in self.cards.values()])

    def show_cards_on_hand(self) -> dict:
        """returning current cards on hand"""
        return print({kkey:vvalue for kkey, vvalue in self.cards.items() if self.cards[kkey]})


    def add_card(self, name: str, show_card_name: bool = True) -> None:
        """adding the card to the cards we have on hand"""
        if name in self.cards.keys():
            self.cards[name] += 1 
            name = '\''+name+'\'' if show_card_name else name
            print(f"{self.name} picked a {name+' ' if show_card_name else ''}card. Total cards on hand: {self.amount_of_cards()}")
            return True
        else:
            return False

    def check_ace_points(self, total_points: int ,number_ace: int = 0) -> int:
        """
        function for calculating points for the count of aces
        """
        if number_ace > 0:     
            if number_ace == 1:
                if total_points <= 10:
                    return 11
                else: 
                    return 1
                ace_count -= 1
            else :
                return self.check_ace_points(total_points+1,number_ace-1) + 1
        else :
            return 0

    def calculate_points(self) -> int:
        """calculating points from the cards on hand       
        """
        self._total_points = 0
        ace_count = 0
        for card, count in self.cards.items():
            if self.cards[card]: # returning only none zero vlues
                if card[0] in ['J','Q','K']:
                    self._total_points += 10 * self.cards[card]
                elif card[0] == 'A':
                    ace_count += self.cards[card]
                else:
                    index_end = card.find('_')
                    self._total_points += int(card[0:index_end]) * self.cards[card]
        
        self._total_points += self.check_ace_points(self._total_points,ace_count)

        return self._total_points
    
    def blackjack_is_true(self) -> bool:
        """returning True if blackjakc is in cards"""
        if self.calculate_points() == 21 and len({kkey:vvalue for kkey, vvalue in self.cards.items() if self.cards[kkey]}) == 2:
            return True
        else:
            return False
    

class HumanPlayer(Player):
    """class to manage the human player"""
    def __init__(self, name: str, start_money: float = 0.0) -> None:
        self._total_money = start_money
        super().__init__(name)
        

    @property
    def _total_money(self) -> float:
        """returning the total money"""
        return round(self.__total_money,2)

    @_total_money.setter
    def _total_money(self, value: float) -> None:
        """setting the value of total_money"""

        if value < 0:
            print("_total_money cant be negative")
            raise ValueError("_total_money cant be negative")
        else:
            self.__total_money = float(int(value * 100)/100) #leaving only two places after the coma
    

    def add_money(self, money: float) -> bool:
        """adding money"""
        if money > 0.0:
            self._total_money += money
            print(f"Added ${money:.2f} to {self.name}")
            return True
        else :
            print("It has to be a value greater than $0.00")
            return False
         
    def deduct_money(self, money: float) -> bool:
        """deducting money"""
        if money > 0.0:
            if self._total_money - money >= 0:
                self._total_money -= money
                print(f"Deducted ${money:.2f} from {self.name}")
                return True
            else:
                print("Not enough money !!")
                return False
        else :
            print("It has to be a value greater than $0.00")
            return False

    def check_total_money(self) -> float:
        """returning the total amount of money"""
        return self._total_money

    def __str__(self) -> str:
        """magic method for depicting the player"""
        return f"{self.name} has ${self._total_money}"

class ComputerPlayer(Player):
    """
    Managing the dealer / computer player !
    """

    def __init__(self, name: str, decks: int = 6) -> None:
        self.decks = decks
        self.cards_all_decks = {
            'A_Clubs': 0, '2_Clubs': 0, '3_Clubs': 0, '4_Clubs': 0, '5_Clubs': 0, '6_Clubs': 0, '7_Clubs': 0, '8_Clubs': 0, '9_Clubs': 0, '10_Clubs': 0, 'J_Clubs': 0, 'Q_Clubs': 0, 'K_Clubs': 0,
            'A_Diamonds': 0, '2_Diamonds': 0, '3_Diamonds': 0, '4_Diamonds': 0, '5_Diamonds': 0, '6_Diamonds': 0, '7_Diamonds': 0, '8_Diamonds': 0, '9_Diamonds': 0, '10_Diamonds': 0, 'J_Diamonds': 0, 'Q_Diamonds': 0, 'K_Diamonds': 0,
            'A_Hearts': 0, '2_Hearts': 0, '3_Hearts': 0, '4_Hearts': 0, '5_Hearts': 0, '6_Hearts': 0, '7_Hearts': 0, '8_Hearts': 0, '9_Hearts': 0, '10_Hearts': 0, 'J_Hearts': 0, 'Q_Hearts': 0, 'K_Hearts': 0,
            'A_Spades': 0, '2_Spades': 0, '3_Spades': 0, '4_Spades': 0, '5_Spades': 0, '6_Spades': 0, '7_Spades': 0, '8_Spades': 0, '9_Spades': 0, '10_Spades': 0, 'J_Spades': 0, 'Q_Spades': 0, 'K_Spades': 0,
        }
        self.set_cards_init(decks)
        super().__init__(name)

    @property
    def decks(self) -> int:
        """returning the number of decks"""
        return self._decks

    @decks.setter
    def decks(self, value: int) -> None:
        """setting the value of decks"""
        if value < 0:
            print("number of decks cant be negative")
            raise ValueError("decks cant be negative")
        else:
            self._decks = value

    def set_cards_init(self, nr_decks: int = 6) -> None:
        """restoring the original amount of cards
        """
        self.cards_all_decks = {keys:nr_decks for keys in self.cards_all_decks }
        
    def remaining_cards(self) -> int:
        """returning the total sum of cards"""
        return sum([value for value in self.cards_all_decks.values()])

    def return_random_card(self) -> str:
        """returning a random card from the deck/s"""
        if self.remaining_cards() > 20:
            list_of_cards = [card_name for card_name in self.cards_all_decks if self.cards_all_decks[card_name]]
            random_card = choice(list_of_cards)
            self.cards_all_decks[random_card] -= 1
            return random_card
        else:
            print("You are running low on cards. Shuffel the decks !! ")
            print("You have only {} cards left. You cant play with them anymore".format(self.remaining_cards()))