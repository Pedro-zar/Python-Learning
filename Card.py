"""Jogo de cartas War, no final contém o script para saber a probabilidade do jogador 1 ganhar"""
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
    "Valete": 11,
    "Dama": 12,
    "Rei": 13,
    "Ás": 14,
}
suits = ("Ouros", "Espadas", "Copas", "Paus")
ranks = ("Ás", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Valete", "Dama", "Rei")


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return self.rank + " de " + self.suit


class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_one(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def remove_one(self):
        return self.cards.pop()

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)

    def __str__(self):
        return f"O jogador {self.name} tem {len(self.cards)} cartas"


def game():
    game_on = True
    round_num = 0
    cartas = Deck()
    jogador_um = Player("Um")
    jogador_dois = Player("Dois")

    for card in range(26):
        jogador_um.add_cards(cartas.deal_one())
        jogador_dois.add_cards(cartas.deal_one())

    while game_on:
        round_num += 1
        if len(jogador_um.cards) == 0:
            game_on = False
            return (jogador_dois.name, round_num)
        elif len(jogador_dois.cards) == 0:
            game_on = False
            return (jogador_um.name, round_num)
        else:
            jogador_1_cards = []
            jogador_1_cards.append(jogador_um.remove_one())
            jogador_2_cards = []
            jogador_2_cards.append(jogador_dois.remove_one())
        at_war = True
        while at_war:
            if jogador_1_cards[-1].value > jogador_2_cards[-1].value:
                jogador_um.add_cards(jogador_1_cards)
                jogador_um.add_cards(jogador_2_cards)
                at_war = False
            elif jogador_1_cards[-1].value < jogador_2_cards[-1].value:
                jogador_dois.add_cards(jogador_1_cards)
                jogador_dois.add_cards(jogador_2_cards)
                at_war = False
            else:

                if len(jogador_um.cards) < 5:
                    game_on = False
                    return (jogador_dois.name, round_num)
                elif len(jogador_dois.cards) < 5:
                    game_on = False
                    return (jogador_um.name, round_num)
                else:
                    for num in range(5):
                        jogador_1_cards.append(jogador_um.remove_one())
                        jogador_2_cards.append(jogador_dois.remove_one())


estatisticas = []
vencedores = 0
rounds = 0
for num in range(10000):
    estatisticas.append(game())
for jogo in estatisticas:
    if jogo[0] == "Um":
        vencedores += 1
    rounds += jogo[1]
print(f"Média de rounds: {rounds/len(estatisticas)}")
print(f"Chance do jogador 1 ganhar é {vencedores/len(estatisticas)*100}%")
