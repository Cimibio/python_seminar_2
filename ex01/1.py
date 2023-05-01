#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
#Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
#вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
import random

def fill_array(arg, min_number, max_number):
    for i in range(len(arg)):
        arg[i] = random.randint(min_number, max_number)

def print_array(arg):
    for i in range(len(arg)):
        print(arg[i])

def CountMinCoins(array):
    heads = 0
    tails = 0
    for i in range(len(array)):
        if array[i] == 0:
            heads = heads + 1
        else:
            tails = tails + 1
    if heads >= tails:
        return tails
    else:
        return heads

N = int(input("введите количество монеток: "))

array = list(range(N))

fill_array(array, 0, 1)
print_array(array)
print("минимальное количество монет которые надо перевернуть: ", CountMinCoins(array))