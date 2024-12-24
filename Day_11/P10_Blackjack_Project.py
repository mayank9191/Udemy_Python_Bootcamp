import random

logo = '''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      '------'                           |__/ 
'''


def sum(list):
    count = 0
    for i in list:
        count += i

    return count


def check_player(player, computer, sump, sumc):
    if (sump > 21):
        print(f'''Your final hand: {player}, Final score: {
            sump}\nComputer's final hand: {computer}, final score: {sumc}
            ''')
        print("You went over. You lose 😭")
        return True

    elif (sump == sumc):
        print(f'''Your final hand: {player}, Final score: {
            sump}\nComputer's final hand: {computer}, final score: {sumc}
            ''')

        print("Draw 🙃")
        return True


def check_computer(player, computer, sump, sumc):

    if (sumc > 21):
        print(f'''Your final hand: {player}, Final score: {
            sump}\nComputer's final hand: {computer}, final score: {sumc}
            ''')
        print("Opponent went over. You win 😁")
        return True

    elif (sumc < sump):
        print(f'''Your final hand: {player}, Final score: {
            sump}\nComputer's final hand: {computer}, final score: {sumc}
                ''')
        print("You win 😃")
        return True

    elif (sump == sumc):
        print(f'''Your final hand: {player}, Final score: {
            sump}\nComputer's final hand: {computer}, final score: {sumc}
            ''')
        print("Draw 🙃")
        return True

    else:
        print(f'''Your final hand: {player}, Final score: {
            sump}\nComputer's final hand: {computer}, final score: {sumc}
            ''')

        print("You lose 😤")
        return True


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


while (True):

    select = input(
        " Do you want to play a game of Blackjack? Type \"y\" or \"n\": ").lower()

    if (select == "n"):
        break

    print(logo)
    player = random.choices(cards, k=2)
    computer = random.choices(cards)

    print(f'''Your cards: {player}, current score: {
        sum(player)}\nComputer's first card {computer[0]}''')

    while (True):

        futher = input(
            "Type 'y' to get another card, type 'n' to pass: ").lower()

        if (futher == "y"):
            player.append(random.choice(cards))
            if (11 in player):
                if (sum(player) > 21):
                    player[player.index(11)] = 1

            sump = sum(player)
            sumc = sum(computer)

            print(f'''Your cards: {player}, current score: {
                sum(player)}\nComputer's card {computer[0]}
                ''')

            if check_player(player, computer, sump, sumc):
                player = []
                computer = []
                print("\n" * 0)
                break

        else:
            computer.append(random.choice(cards))
            if (11 in player):
                if (sum(player) > 21):
                    player[player.index(11)] = 1

            while True:
                if (sum(computer) < 17):
                    computer.append(random.choice(cards))
                    if (11 in player):
                        player[player.index(11)] = 1

                else:
                    break
            sump = sum(player)
            sumc = sum(computer)

            if check_computer(player, computer, sump, sumc):
                player = []
                computer = []
                print("\n" * 20)
                break

            print(f'''Your cards: {player}, current score: {
                sum(player)}\nComputer's cards {computer}
                ''')
