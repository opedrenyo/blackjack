import random
import os

############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
blackjack = 21
computer_sum_new_card = 17
game_continue = True

def ace_change_value(hand):
    ace_index = hand.index(11)
    hand[ace_index] = 1
    return hand


def player_new_card(player_hand):
        new_card = input("Type 'y' to get another card, type 'n' to pass: ")

        if new_card == 'y':
            player_hand.append(random.choice(cards))
            if sum(player_hand) <= blackjack:
                print(f"Your cards are {player_hand}, current score: {sum(player_hand)}\n")
                player_middle_hand = player_hand
                player_new_card(player_middle_hand)

            elif sum(player_hand) > blackjack and player_hand.count(11) > 0:
                if player_hand.count(11) > 0:
                    ace_change_value(player_hand)
                    print(f"Your cards are {player_hand}, current score: {sum(player_hand)}\n")
                    player_hand_ace = player_hand
                    player_new_card(player_hand_ace)

            else:
                print(f"Your cards are {player_hand}, current score: {sum(player_hand)}. You went over. You lose\n")
                should_continue = input("Do you want to play a game of Blackjack? Type 'y', or 'n': ")
                if should_continue == 'y':
                    continue_game() 
                else:
                    quit()

        return player_hand



def computer_new_card(computer_hand):
    while sum(computer_hand) <= blackjack:
        while sum(computer_hand) < computer_sum_new_card:
                computer_hand.append(random.choice(cards))
                if sum(computer_hand) > blackjack and computer_hand.count(11) > 0:
                    ace_change_value(computer_hand)
        return computer_hand




def who_wins(player_final_hand, computer_final_hand):
        if sum(player_final_hand) > sum(computer_final_hand):
            return "You win! CONGRATS!"
        elif sum(computer_final_hand) > sum(player_final_hand):
            return "You lose..."
        elif sum(player_final_hand) == sum(computer_final_hand):
            return "You draw. Try Again!"

# Program

def continue_game():
    os.system('cls')
    player_hand = []
    computer_hand = []
    
    # We give the first cards to player and computer.
    player_hand.extend([random.choice(cards),random.choice(cards)])
    computer_hand.append(random.choice(cards))

    print(f"Your cards are {player_hand}, current score: {sum(player_hand)}")
    print(f"Computer's first card: {computer_hand[0]}")

    # We ask the player if he wants more cards while he's under 21.
    player_final_hand = player_new_card(player_hand)

    print(f"Player's final hand: {player_final_hand}, final score: {sum(player_final_hand)}.")

    # We give new cards to the computer
    computer_final_hand = computer_new_card(computer_hand)

    
    if sum(computer_final_hand) > blackjack:
        print(f"Computer's final hand: {computer_final_hand}, final score: {sum(computer_final_hand)}.")
        print("Computer went over. You win! CONGRATS!")
    elif sum(computer_final_hand) <= blackjack:
        print(f"Computer's final hand: {computer_final_hand}, final score: {sum(computer_final_hand)}.")
        winner = who_wins(player_final_hand, computer_final_hand)
        print(winner)


## ASK TO PLAY AGAIN.
    should_continue = input("Do you want to play a game of Blackjack? Type 'y', or 'n': ")
    if should_continue == 'y':
        continue_game() 
    else:
        return "Goodbye! See you soon!"


continue_game()




