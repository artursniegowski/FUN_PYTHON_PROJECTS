# secret auction
from logging import PlaceHolder
from main_ASCI_ART import BLACKJACK
from Players import ComputerPlayer
from Players import HumanPlayer


def how_many_players(message: str) -> int:
    """takes the input of the user and returs it if it's a vlid number,
    else return None
    """ 
    number_players = 0
    number_players = input(message)
    try:
        number_players = int(number_players)
    except ValueError:
        print(f"{number_players} This is not a valid number (1-4) !!")
    except Exception as e:
        print(f"Exception {e} was caught")
        print(type(e))
    else : # if no exception caught
        if 0 < number_players < 5:
            return number_players

    # if number not in the right range
    print(f"{number_players} This is not a a number between 1-4 !!")
    return None

def deposit_money_bank(name: str) -> float:
    """depositing money to the table"""
    money = input(f"How much money does player {name} wants to play with (min 20.00)?: $")
    try:
        money = float(int(float(money)*100)/100)
    except ValueError:
        print(f"{money} This is not a valid amount of $ !! TRY AGAIN !")
        money = 0.0
        deposit_money_bank(name)
    except Exception as e:
        print(f"Exception {e} was caught")
        print(type(e))
    else : # if no exception caught
        if money > 20.0 :
            print(f"{name} is depositing ${money}")
        else :
            print(f"{money}$ is not greater than 20$ (min Bet). Try again !!")
            money = deposit_money_bank(name)
            
    
    return money

def populating_users(player_number: int = 1) -> list[HumanPlayer] :
    """creating HumanPlayer instances,
    and returnig a list of all palyers
    """
    if not (0 < player_number < 5):
        raise("Wrong input number. player_number has to be between 1-4 !!")
        return None
        
    players = []
    
    for n in range(player_number):
        name = input(f"What is the name of player nr {n+1}: ")
        money = deposit_money_bank(name)
        new_player = HumanPlayer(name,money)
        players.append(new_player)

    return players

def check_if_enough_money(players: list[HumanPlayer], money: float) -> list[HumanPlayer]:
    """deleting the users who cant afford to place at least one bet"""
    for player in players:
        if player.check_total_money() < 20.00:
            print(f"{player.name} dosent have the minimum $20.00 to place a bet. His balnace stands at ${player.check_total_money()}. The Dealer makes {player.name} leave the table !!")
            players.remove(player)
            

    return players

def won_info_1(player: HumanPlayer, dealer: ComputerPlayer, Bet_size: float) -> None:
    """Winning message"""
    print(f"\n\nYou have WON {player.name}!!")
    print(f"{player.name} cards :")
    player.show_cards_on_hand()
    print(f"{dealer.name} cards :")
    dealer.show_cards_on_hand()
    print(f"Player: {player.name} has {player.calculate_points()}. {dealer.name} has over 21 points ({dealer.calculate_points()}). YOU have WON !!!")
    player.add_money(Bet_size)
    print("\n\n")

def won_info_2(player: HumanPlayer, dealer: ComputerPlayer, Bet_size: float) -> None:
    """Winning message"""
    print(f"\n\nYou have WON {player.name}!!")
    print(f"{player.name} cards :")
    player.show_cards_on_hand()
    print(f"{dealer.name} cards :")
    dealer.show_cards_on_hand()
    print(f"Player: {player.name} has {player.calculate_points()} which is more than the {dealer.name} with points ({dealer.calculate_points()}). YOU have WON !!!")
    player.add_money(Bet_size)
    print("\n\n")

def won_info_blackjack(player: HumanPlayer, Bet_size: float) -> None:
    """Winning message - blackjack"""
    print(f"\n\nYou have WON {player.name}. You have a blackjack!!")
    print(f"{player.name} cards :")
    player.show_cards_on_hand()
    player.add_money(Bet_size)
    print("\n\n")

def draw_info(player: HumanPlayer, dealer: ComputerPlayer, Bet_size: float) -> None:
    """Draw message"""
    print(f"\n\nIt is a DRAW {player.name}!!")
    print(f"{player.name} cards :")
    player.show_cards_on_hand()
    print(f"{dealer.name} cards :")
    dealer.show_cards_on_hand()
    print(f"Player: {player.name} has {player.calculate_points()} which is the same as the {dealer.name} with {dealer.calculate_points()} points. It's a draw !!!\n\n")

def lose_info(player: HumanPlayer, dealer: ComputerPlayer, Bet_size: float) -> None:
    """Losing message"""
    print(f"\n\nYou have lost {player.name}!!")
    print(f"{player.name} cards :")
    player.show_cards_on_hand()
    print(f"{dealer.name} cards :")
    dealer.show_cards_on_hand()
    print(f"Player: {player.name} has {player.calculate_points()} which is less than the {dealer.name} with {dealer.calculate_points()} points. You have lost !!!")
    player.deduct_money(Bet_size)
    print("\n\n")

def lose_info_blackjack(player: HumanPlayer, dealer: ComputerPlayer, Bet_size: float) -> None:
    """Losing message"""
    print(f"\n\nYou have lost {player.name}!! The Dealer has a blackjack!!")
    print(f"{player.name} cards :")
    player.show_cards_on_hand()
    print(f"{dealer.name} cards :")
    dealer.show_cards_on_hand()
    player.deduct_money(Bet_size)
    print("\n\n")



# initial values for the game
play_game_message = "Do you want to play a game of Blackjack? Type 'y' or 'n': "
another_card_message = "Do you want another card? (y/n), 'q' to leave the table: " 
how_many_players_message = "How many players will join the game? "
Bet_size = 20.00
play_game = False
human_players = []



# intro
print(BLACKJACK)

# creating the dealer instance
NUMBER_DECKS = 8
dealer = ComputerPlayer('Dealer', NUMBER_DECKS)
print(f"{dealer.name} prepares the table with {dealer.decks} decks of cards. The bets for each game are set to ${Bet_size}")
print("Max number of players is 4.")
print(f"Each game is ${Bet_size} bet. \n")

number_players = how_many_players(how_many_players_message)
if number_players :
    play_game = True
else:
    play_game = False
    print("The Dealer is kicking you out!! You didnt provided the right number of players (1-4)")


if play_game: 
    human_players = populating_users(number_players)
    for players in human_players:
        print(f"Player {players.name} is joining the table with ${players.check_total_money()}.")

#player_name = 'Mark Brum'#input("What is your name? ")
# creating player_nr1 instance with a base money value of 1000$
#player_name_nr1 = HumanPlayer(player_name,1000)


while play_game:

    # reset all cards back to 8th decks / NUMBER_DECKS
    # when there were 2 decks of card played
    if dealer.remaining_cards() < (NUMBER_DECKS-2) * 52 :
        print("Remaining cards dropped low. Shuffling all decks.")
        dealer.set_cards_init(NUMBER_DECKS)

    #print(dealer.cards_all_decks)
    print("\nStarting the game !!!")
    print(f"Cards left in the game: {dealer.remaining_cards()}, from {dealer.decks} decks.\n")

    # filtering players who actually have enough money to place a bet
    if not check_if_enough_money(human_players,Bet_size):
        print("No players left to play the game")
        break

    # adding first random card from the decks choosen
    dealer.add_card(dealer.return_random_card())
    # showing the first card from the dealer
    dealer.show_cards_on_hand()
    # adding the second card to the dealear - keeping it hidden at the begining
    dealer.add_card(dealer.return_random_card(),show_card_name=False)
    print(f"{dealer.name} has picked his cards. Now it is your turn! \n")

    players_wanting_to_leave = []

    for player in human_players:

        # players turn 
        print('\n')
        print(player)
        # choosing the first card 
        player.add_card(dealer.return_random_card())
        # showing players cards
        player.show_cards_on_hand()
        print(f"{player.name} has {player.calculate_points()} points")

        # next cards 
        while (choice_another_card := input(another_card_message).lower().strip()) == 'y':
            # another card
            print("\n")
            player.add_card(dealer.return_random_card())
            player.show_cards_on_hand()
            print(f"{player.name} has {player.calculate_points()} points")

            if player.calculate_points() > 21:
                print(f"{player.name} went over 21 points !! NEXT PLAYER TURN\n")
                break
        
        if choice_another_card == 'q':
            player.deduct_money(Bet_size)
            print(f"{player.name} leaves the table with ${player.check_total_money()}")
            players_wanting_to_leave.append(player)
    else:

        # removing players who wish to leave
        for player in players_wanting_to_leave:
            print("\n")
            print(player)
            print("Left...")
            human_players.remove(player)


    # checking which player went above 21
    for player in human_players:
        total_points_player = player.calculate_points()
        if total_points_player > 21:
            print("\n\nYou have lost !!")
            player.show_cards_on_hand()
            print(f"Player: {player.name} has {total_points_player} which is over 21. YOU have LOST !!!")
            player.deduct_money(Bet_size)
            print("\n\n")

    # checking if the players has a valid score
    human_players_total_points = [player.calculate_points() if player.calculate_points() <= 21 else 0  for player in human_players]
    if any(human_players_total_points):

        while dealer.calculate_points() < 17:
            print("\n")
            # choosing the next card 
            dealer.add_card(dealer.return_random_card())
            # showing player_1 cards
            dealer.show_cards_on_hand()
            print(f"{dealer.name} has {dealer.calculate_points()} points\n")

        total_points_dealer = dealer.calculate_points()

        for player in human_players:

            total_points_player = player.calculate_points()

            if total_points_player <= 21:
                
                if player.blackjack_is_true():
                    won_info_blackjack(player,Bet_size)

                elif dealer.blackjack_is_true():
                    lose_info_blackjack(player,dealer,Bet_size)

                elif total_points_dealer > 21:
                    won_info_1(player,dealer,Bet_size)

                elif total_points_player > total_points_dealer:
                    won_info_2(player,dealer,Bet_size)

                elif total_points_player == total_points_dealer:
                    draw_info(player,dealer,Bet_size)

                else:
                    lose_info(player,dealer,Bet_size)
          
    # discarding cards from the dealer and players
    # setting back all cards from the dealer
    dealer.reset_cards()
    # setting back all cards from the player nr 1
    for player in human_players:
        player.reset_cards()
