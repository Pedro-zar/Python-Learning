import random

values = {
    "Dois": 2,
    "Três": 3,
    "Quatro": 4,
    "Cinco": 5,
    "Seis": 6,
    "Sete": 7,
    "Oito": 8,
    "Nove": 9,
    "Dez": 10,
    "Valete": 10,
    "Dama": 10,
    "Rei": 10,
    "Ás": 11,
}
suits = ("Ouros", "Espadas", "Copas", "Paus")
ranks = ("Ás", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Valete", "Dama", "Rei")
playing = True


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + " de " + self.suit


class Deck:
    def __init__(self, shuffle=False):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))
        if shuffle:
            self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Bank:
    def __init__(self, value=500):
        self.value = value
        self.bet = 0

    def winBet(self):
        self.value += self.bet

    def loseBet(self):
        self.value -= self.bet


def take_bet(bank):
    while True:
        try:
            bank.bet = int(input("Qual a sua aposta?"))
        except ValueError:
            print("Por favor, escolha um número inteiro")
        else:
            if bank.bet > bank.value:
                print("Sua aposta excede sua carteira, escolha um valor menor")
            elif bank.bet <= 0:
                print("É necessário apostar algo para jogar")
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Quer continuar ou parar? Enter 'C' or 'P'\n")
        print(playing)
        if x[0].lower() == "c":
            hit(deck, hand)
        elif x[0].lower() == "p":
            print("Jogador para. A casa está jogando.")
            playing = False
        else:
            print("Desculpe, tente novamente.")
            continue
        break


def show_some(player, dealer):
    print("\nMão da casa:")
    print(" <carta virada>")
    print("", dealer.cards[1])
    print("\nMão do jogador:", *player.cards, sep="\n ")


def show_all(player, dealer):
    print("\nMão da casa:", *dealer.cards, sep="\n ")
    print("Mão da casa =", dealer.value)
    print("Mão do jogador:", *player.cards, sep="\n ")
    print("Mão do jogador =", player.value)


def player_busts(bank):
    print("Vitória da casa! Jogador extourou")
    bank.loseBet()


def player_wins(bank):
    print("Vitória do jogador, parabéns!")
    bank.winBet()


def dealer_busts(bank):
    print("Vitória do jogador! A casa extourou")
    bank.winBet()


def dealer_wins(bank):
    print("Vitória da casa!")
    bank.loseBet()


def push():
    print("Empate, apostas de volta pra casa!")


def game():
    global playing
    bank = Bank()
    print("Bem vindo! O jogo da noite é: Blackjack")
    while True:
        deck = Deck(True)
        player = Hand()
        player.add_card(deck.deal())
        player.add_card(deck.deal())
        dealer = Hand()
        dealer.add_card(deck.deal())
        dealer.add_card(deck.deal())
        take_bet(bank)
        show_some(player, dealer)
        while playing:
            hit_or_stand(deck, player)
            show_some(player, dealer)
            if player.value > 21:
                player_busts(bank)
                break

        if player.value <= 21:
            while dealer.value < 17:
                hit(deck, dealer)
            show_all(player, dealer)

            if dealer.value > 21:
                dealer_busts(bank)
            elif player.value > dealer.value:
                player_wins(bank)
            elif player.value < dealer.value:
                dealer_wins(bank)
            else:
                push()

        print("A carteira do jogador tem", bank.value)
        new_game = input("Gostaria de continuar? 'S' ou 'N'")

        if new_game[0].lower() == "s":
            playing = True
            continue
        else:
            print("Obrigado por jogar!")
            break


game()
