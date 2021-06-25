import time
alpha = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
print(f'Эт0 пр0грамwa дл9 шифр08ки Т%;№:ста.')
message = input("Впиши сл0в0, к0т99ро3 над0 3ашифр08ать :" )
kluch = int(input("П0жалуйста введит3 клю4 (цифру от 1 до 33) : "))
print('-_-')
message = message.lower()
translated = ""
i = len (message) - 1
print(f'П0д0ждит3.... 8ыполня3тс9 шифр0вка...')
time.sleep(4)

while i>=0:
    i = i -1
    for letter in message:
        tochka = alpha.find(letter) #find вроде как обращается переменной алфавита для поиска совпадения
    newtochka = tochka + kluch
    if letter in alpha : #проверка
        translated = translated + alpha[newtochka]
    else:
        translated = translated + letter
    print("3ашифр0ва2ный тЕкст : ", translated)
