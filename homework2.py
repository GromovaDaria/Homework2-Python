# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11

#a = input('Input number: ')
#def summ(a):
#    if float(a) < 0:
#        a = float(a) * (-1)
#    number = 0
#    for i in str(a):
#        if i != '.':
#            number += int(i)
#    return number
#print(f'The summ of numbers is {summ(a)}')

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

#N = int(input('Input number: '))
#a = 1
#for i in range(N):
#    i = i + 1
#    a = i * a
#    
#    print(a, end = " ")

# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

#x = int(input('Enter the number of numbers in the list: '))
#def numbers(n):
#    summ = 0
#    for i in range(x):
#        a = int(input(f'Enter number {i + 1}: '))
#        a = (1+1/a)**a
#        summ = a + summ
#        i += 1
#    return summ
#
#print('The summ of numbers is',round((numbers(x)), 2))

# Реализуйте алгоритм перемешивания списка.

#from random import Random, randint
#
#N = int(input('Enter number: '))
#num = []
#for i in range(N):
#    num.append(randint(-N,N+1))
#print('Original list: ', num)
#
#def mix_list(num):
#    list = num[:]
#    list_length = len(list)
#    for i in range(list_length):
#        index = randint(0, list_length - 1)
#        temp = list[i]
#        list[i] = list[index]
#        list[index] = temp
#    return list
#
#print('Mixed list: ', mix_list(num))