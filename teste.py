"""Arquivo de aprendizado em python"""
import string
from random import shuffle


def count_primes(num):
    """Conta o número de primos de 2 até o número passado"""
    if num < 2:
        return 0
    primes = [2]
    actual_number = 3
    while actual_number <= num:
        for prime in primes:
            if actual_number % prime == 0:
                actual_number += 2
                break
        else:
            primes.append(actual_number)
            actual_number += 2
    print(primes)
    return len(primes)


def embaralhar(cups):
    """Embaralha a lista passada"""
    shuffle(cups)
    return cups


def verificar_acerto(escolha):
    """Verifica se a escolha passada é a correta"""
    copos = embaralhar([False, False, True])
    return copos[escolha]


def jogar():
    """Joga o jogo de acertar onde está a bola nos copinhos"""
    if verificar_acerto(int(input("A bola está no copo 1, 2 ou 3?\n"))-1):
        print("Parabéns, você acertou!")
    else:
        print("Que pena, você errou")


def myfunc(phrase):
    """Função para fazer as letras pares maiúsculas e o resto minúscula"""
    lista = []
    count = 0
    for letter in phrase:
        count = count + 1
        if count % 2 == 0:
            lista.append(letter.upper())
        else:
            lista.append(letter.lower())
    result = ''
    for word in lista:
        result = result+word

    return result


def lesser_evens(num1, num2):
    """Verifica dois número, se ambos forem par, pega o menor, se não pega o maior"""
    if num1 % 2 == 0 == num2 % 2:
        return min(num1, num2)
    return max(num1, num2)


def is_equal_words(phrase):
    """Verifica se as palavras 1 e 2 são iguais"""
    palavras = phrase.lower().split()
    return palavras[0][0] == palavras[1][0]


def spy_game(nums):
    """Vê se tem a sequência 007 na lista"""
    code = [0, 0, 7, '']
    for num in nums:
        if num == code[0]:
            code.pop(0)
        print(code)
    return len(code) == 1


def vol(rad):
    """Retorna o volume da Rad passada"""
    return 4/3*3.14*(rad**3)


def ran_check(num, low, high):
    """Retorna se o número 1 está entre o dois e o três"""
    # return num in range(low,high+1)
    return low <= num <= high


def up_low(phrase):
    """Conta quantas letras maiusculas e minusculas tem na frase"""
    lower = 0
    upper = 0
    for letter in phrase:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1
    return (upper, lower)


def unique_list(lst):
    """Retorna uma lista com os items da lista passada, sem duplicatas"""
    return list(set(lst))


def multiply(numbers) -> float:
    """Multiplica os números passados como parâmetros em lista"""
    result = 1
    for num in numbers:
        result *= num
    return result


def palindrome(phrase) -> bool:
    """Verifica se é um caso de palindromo"""
    phrase = phrase.replace(' ', '').lower()
    return phrase == phrase[::-1]


def ispangram(str1, alphabet=string.ascii_lowercase):
    """Verifica se é um caso de pangrama"""
    str1 = str1.lower().replace(' ', '')
    for letter in alphabet:
        if not str1.__contains__(letter):
            return False
    return True


class Line:
    """Linha com dois pontos"""

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        """Verificar distancia entre os dois pontos da linha"""
        x_distance = (self.coor2[0] - self.coor1[0])**2
        y_distance = (self.coor2[1] - self.coor1[1])**2
        return (x_distance + y_distance)**(1/2)

    def slope(self) -> float:
        """verificar a Slope??? da linha"""
        y_slope = self.coor2[1]-self.coor1[1]
        x_slope = self.coor2[0]-self.coor1[0]
        return y_slope/x_slope


class Cylinder:
    """Cilindro"""
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self) -> float:
        """Verifica o volume do cilindro"""
        return self.pi*(self.radius**2)*self.height

    def surface_area(self) -> float:
        """Verifica o tamanho da face do cilindro"""
        return (2*self.pi*self.height*self.radius) + (2*self.pi*(self.radius**2))


class Account:
    """Conta de banco"""

    def __init__(self, owner, balance) -> None:
        self.owner = owner
        self.balance = balance

    def __str__(self) -> str:
        return f"Account owner:   {self.owner}\nAccount balance: ${self.balance}"

    def deposit(self, value) -> None:
        """Faz um deposito na conta"""
        self.balance = self.balance + value
        print("Deposit accepted")

    def withdraw(self, value) -> None:
        """Verifica se é possível, e se sim, faz o saque"""
        if value <= self.balance:
            self.balance = self.balance - value
            print("Withdraw accepted")
        else:
            print("Withdraw rejected, funds unavailable!")


def ask() -> None:
    """Pede um número e diz se o quadrado dele"""
    while True:
        try:
            user_input = int(input("Input an integer: "))
        except:
            print("An error occurred! Please try again!")
        else:
            print(f"Thank you, your number squared is: {user_input**2}")
            break
