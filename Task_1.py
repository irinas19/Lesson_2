#Напишите программу, которая принимает на вход строку и выводит на
# экран все слова, которые начинаются с заглавной буквы.

def find_title(a):
    words = []
    for i in a.split(' '):
        if i.istitle():
            words.append(i)
    return words

a = input('Введите строку: ')
print(find_title(a))