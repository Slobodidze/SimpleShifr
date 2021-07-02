import random
Mode = False

orig = {0:'й', 1:'ц', 2:'у', 3:'к', 4:'е', 5:'н', 6:'г', 7:'ш', 7:'щ', 8:'з', 9:'х', 10:'ъ', 11:'э', 12:'ж', 13:'д', 14:'л', 15:'о', 16:'р', 17:'п', 18:'а', 19:'в', 20:'ы', 21:'ф', 22:'я', 23:'ч', 24:'с', 25:'м', 26:'и', 27:'т', 28:'ь', 29:'б', 30:',', 31:'.', 32:' '}
coded = {0:'q', 1:'w', 2:'e', 3:'r', 4:'t', 5:'y', 6:'u', 7:'i', 7:'o', 8:'p', 9:'-', 10:'=', 11:'*', 12:'/', 13:'l', 14:'k', 15:'j', 16:'h', 17:'g', 18:'f', 19:'d', 20:'s', 21:'a', 22:'z', 23:'x', 24:'c', 25:'v', 26:'b', 27:'n', 28:'m', 29:'e', 30:'t', 31:'-', 32:'*'}
dict = {0:'Q', 1:'W', 2:'R', 3:'Y', 4:'U', 5:'I', 6:'S', 7:'D', 8:'F', 9:'G'}

def code():
    text = input("ВВедите текст для Зашифровки ")
    pre = text.lower()
    mapping = str.maketrans("0123456789", "QWRYUISDFG")    # создаём отображение
    mapping2 = str.maketrans("йцукенгшщзхъ", "qwertyuiop-=")    # создаём отображение
    mapping3 = str.maketrans("эждлорпавыф", "*/lkjhgfdsa")    # создаём отображение
    mapping4 = str.maketrans("ячсмить бю,.", "zxcvbnm_+-*~")    # создаём отображение
    post = pre.translate(mapping)     # преобразуем строку
    post = post.translate(mapping2)     # преобразуем строку
    post = post.translate(mapping3)     # преобразуем строку
    post = post.translate(mapping4)     # преобразуем строку
    print(post)
    return

def decode():
    #print("ВВедите текст для Расшифровки")
    crypt = input("ВВедите текст для Расшифровки")


def exp():
    text = input("ВВедите текст для Зашифровки ")
    pre = text.lower()
    mapping = str.maketrans("0123456789", "QWRYUISDFG")    # создаём отображение
    mapping2 = str.maketrans("йцукенгшщзхъ", "qwertyuiop-=")    # создаём отображение
    mapping3 = str.maketrans("эждлорпавыф", "*/lkjhgfdsa")    # создаём отображение
    mapping4 = str.maketrans("ячсмить бю,.", "zxcvbnm_+-*~")    # создаём отображение
    post = pre.translate(mapping)     # преобразуем строку
    post = post.translate(mapping2)     # преобразуем строку
    post = post.translate(mapping3)     # преобразуем строку
    post = post.translate(mapping4)     # преобразуем строку
    print(post)


while Mode == False:
    print('Программа для Зашифровки и Расшифровки текста.')
    print('Выберите режим: Зашифровать(З) или Расшифровать(Р)')
    mode = input()
    if mode not in ['З', 'Р', 'Э']:
        print('Неправильный ввод!')
        Mode = False
    else:
        Mode = True
if mode == 'З':
    code()
elif mode == 'Э':
    exp()
else:
    decode()

