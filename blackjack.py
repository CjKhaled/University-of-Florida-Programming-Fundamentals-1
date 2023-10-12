
#Just copy and pasted the P1Random file here
class P1Random:
    def __init__(self):
        self._next = 0
        self._MULTIPLIER = 1103515245
        self._ADDEND = 12345
        self._DIVISOR = 65536

    def next_short(self, limit=2 ** 15 - 1):
        self._next = (self._next * self._MULTIPLIER + self._ADDEND) % 2 ** 64
        if self._next > 2 ** 63 - 1:
            self._next -= 2 ** 64

        # using (next // DIVISOR) results in incorrect value for negative numbers
        value = int(self._next / self._DIVISOR) % 2 ** 64
        if value > 2 ** 63 - 1:
            value -= 2 ** 64

        if value < 0:
            value = value % limit - limit
        else:
            value = value % limit

        return abs(value)

    def next_int(self, limit=2 ** 31 - 1):
        val = self.next_short() << 16
        val %= 2 ** 32
        if val > 2 ** 31 - 1:
            val -= 2 ** 32
        return (val | self.next_short()) % limit

rng = P1Random()

game_continue = True
game_number = 0
wins = 0
losses = 0
ties = 0

#Using a dictionary because I want to check the card before dealing it to player
cards = {1: 'ACE', 11: 'JACK', 12: 'QUEEN', 13: 'KING'}

#Traversing the entire dictionary- then locally replacing the random card value with the respective item
def check_card(card):
    for key, item in cards.items():
        if card == key:
            card = item
    print(f"Your card is a {card}!")

def play_menu():
    print(f"1. Get another card")
    print(f"2. Hold hand")
    print(f"3. Print statistics")
    print(f"4. Exit")

#Stats table
def game_stats(games_played, number_wins, number_loss, number_ties):
    games_played = game_number - 1
    number_wins = wins
    number_loss = losses
    number_ties = ties
    win_percentage = (wins / games_played) * 100
    print(
          f"Number of Player wins: {number_wins}\n"
          f"Number of Dealer wins: {number_loss}\n"
          f"Number of tie games: {number_ties}\n"
          f"Total # of games played is: {games_played}\n"
          f"Percentage of Player wins: {win_percentage:.1f}%")


while game_continue is True:
    game_number += 1
    print(f"START GAME #{game_number}")
    print()
    player_hand = 0
    dealer_hand = 0
    card = rng.next_int(13) + 1
    check_card(card)
    #Making sure the value of cards is at most 10
    if card > 10:
        player_hand += 10
    else:
        player_hand += card
    print(f"Your hand is: {player_hand}")
    game_done = False
    while game_done is False:
        print()
        play_menu()
        print()
        option = (input("Choose an option: "))
        #Making sure the user input is flagged when wrong, and it won't exit the program when wrong
        try:
            option = int(option)
            if option > 4 or option < 1:
                print("Invalid input!")
                print("Please enter an integer value between 1 and 4.")
        except:
            print("Invalid input!")
            print("Please enter an integer value")
        if option == 4:
            game_continue = False
            exit(4)
        if option == 1:
            card = rng.next_int(13) + 1
            check_card(card)
            if card > 10:
                player_hand += 10
            else:
                player_hand += card
            print(f"Your hand is: {player_hand}")
            #How to generally win and lose
            if player_hand == 21:
                print("BLACKJACK! You win!\n")
                wins += 1
                game_done = True
                break
            if player_hand > 21:
                print("You exceeded 21! You lose.")
                print()
                losses += 1
                game_done = True
                break
        #Configured how to win, lose, and tie in a game when holding
        if option == 2:
            dealer_card = rng.next_int(11) + 16
            dealer_hand += dealer_card
            print(f"Dealer's hand: {dealer_hand}")
            print(f"Your hand is: {player_hand}")
            if dealer_hand > 21:
                print("You win!\n")
                wins += 1
                game_done = True
                break
            if player_hand == dealer_hand:
                print("It's a tie! No one wins!")
                print()
                ties += 1
                break
            if dealer_hand > player_hand:
                print("Dealer wins!")
                print()
                game_done = True
                losses += 1
            if player_hand > dealer_hand:
                print("You win!\n")
                game_done = True
                wins += 1
        if option == 3:
            game_stats(game_number, wins, losses, ties)



