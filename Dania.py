import random, sys
slovo = input("Введите слово для зашифровки - ")
print("Вы ввели слово",slovo )
print("шифровка !!!!!!")
Nomer = len(slovo)
if Nomer % 2 == 0:
    slovo = slovo[1::2] + slovo[::2]#это экстромув
else:
    slovo = slovo[1::2] + slovo[::2]#это экстромув
print(slovo)
