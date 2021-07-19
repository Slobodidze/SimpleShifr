import# Импортируем все из библиотеки TKinter
from tkinter import *
# Создаем главный объект (по сути окно приложения)
root = Tk()
# Эта функция срабатывает при нажатии на кнопку "Посмотреть погоду"
def Exit():
	exit()
def sbros():
	slovo = vivod.get()
	slovo = ""
	info['text'] = slovo
def shifrovka():
	# Получаем данные от пользователя
	slovo = vivod.get()
	Nomer = len(slovo)
	if Nomer % 2 == 0:
		slovo = slovo[1::2] + slovo[::2]  # это экстромув
		info['text'] = slovo
	else:
		slovo = slovo[1::2] + slovo[::2]  # это экстромув

# Настройки главного окна

# Указываем фоновый цвет
root['bg'] = 'orange'
# Указываем название окна
root.title('Шифровщик')
# Указываем размеры окна
root.geometry('300x250')
# Делаем невозможным менять размеры окна
root.resizable(width=False, height=False)

# Создаем фрейм (область для размещения других объектов)
# Указываем к какому окну он принадлежит, какой у него фон и какая обводка
frame_top = Frame(root, bg='Red', bd=5)
# Также указываем его расположение
frame_top.place(relx=0.16, rely=0.15, relwidth=0.7, relheight=0.25)


frame_exit = Frame(root, bg='orange', bd=5)
# Также указываем его расположение
frame_exit.place(relx=0.40, rely=0.8, relwidth=0.9, relheight=0.43)


frame_set = Frame(root, bg='orange', bd=5)
# Также указываем его расположение
frame_set.place(relx=0.36, rely=0.4, relwidth=0.3, relheight=0.30)

# Все то-же самое, но для второго фрейма
frame_bottom = Frame(root, bg='gray', bd=6)
frame_bottom.place(relx=0.15, rely=0.57, relwidth=0.7, relheight=0.14)
Nazvanie = Label(root, text='Шифровщик Dan4k', bg='orange', font=50)
Nazvanie .pack()
# Создаем текстовое поле для получения данных от пользователя
vivod = Entry(frame_top, bg='orange', font=29)
vivod.pack()  # Размещение этого объекта, всегда нужно прописывать

# Создаем кнопку и при нажатии будет срабатывать метод "shifrovka"
btn = Button(frame_top, text='Зашифровать', command=shifrovka,bg='red')
btn.pack()

# Создаем кнопку и при нажатии будет срабатывать метод "shifrovka"
btn_set = Button(frame_set, text='Reset', command= sbros ,bg='red')
btn_set.pack()



btn_exit = Button(frame_exit, text='Exit', command= Exit ,bg='red')
btn_exit.pack()

# Создаем текстовую надпись, в которую будет выводиться информация о шифре
info = Label(frame_bottom, text='Шифр будет тут', bg='gray', font=50)
info.pack()

# Запускаем постоянный цикл, чтобы программа работала
root.mainloop()
