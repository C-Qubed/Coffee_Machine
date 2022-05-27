# Blackjack
import random
import art

# Variables
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer = []
player = []
money = 500
play_in = 20


def play():
    global play_in
    global money
    pot = 0
    bet = 0

    print(art.logo)
    print('Welcome to Blackjack!')
    money -= play_in
    print(f'It costs ${play_in} to play, that leaves you with ${money}.')

    # Clear lists from last round
    dealer.clear()
    player.clear()

    # betting addition
    will_bet = input('Would you like to bet additional money? ')
    if will_bet == 'yes':
        bet_amount = int(input('How much would you like to bet? '))
        if bet_amount > money:
            print(f'That\'s more than you have! You can\'t bet that.')
        else:
            bet += bet_amount
    pot = (bet * 2) + (play_in * 2)
    print(f'The pot this round is ${pot}.')

    # Set up starting display
    deal_player()
    deal_dealer()
    display()

    # Player cycle
    done = False
    while not done:
        p_choice = input('Hit or stand? ')
        if p_choice == 'hit':
            player.append(random.choice(cards))
            if sum(player) > 21:
                if 11 in player:
                    player.remove(11)
                    player.append(1)
                done = True
            else:
                display()
        else:
            done = True

    # Dealer cycle
    while sum(dealer) < 16:
        dealer.append(random.choice(cards))
        if sum(dealer) > 21:
            if 11 in dealer:
                dealer.remove(11)
                dealer.append(1)

    # When both cycles are finished
    display()
    if sum(dealer) == sum(player):
        print('It\'s a tie!')
    elif sum(player) > 21:
        print('You lose...')
        money -= bet + play_in
    elif sum(dealer) > 21:
        print('You win!')
        money += pot
    elif sum(dealer) > sum(player):
        print('You lose...')
        money -= bet + play_in
    elif sum(player) > sum(dealer):
        print('You win!')
        money += pot

    print(f'You have ${money}. of the $5000 you need for supplies!')
    if money >= 5000:
        print('You won the money you needed! Thank you for playing blackjack!')
    if money < 0:
        print('You\'re broke!')
        print('We\'ll give you $100 on the house to get you back up and going again.')
        money = 100
        play()
    else:
        play()


def deal_player():
    p_card1 = random.choice(cards)
    player.append(p_card1)
    p_card2 = random.choice(cards)
    player.append(p_card2)


def deal_dealer():
    d_card1 = random.choice(cards)
    dealer.append(d_card1)


def display():
    print(f'Player\'s cards: {player} Total: {sum(player)}')
    print(f'Dealer\'s cards: {dealer} Total: {sum(dealer)}')
