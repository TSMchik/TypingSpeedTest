from tkinter import *
import ctypes
import random
import tkinter

# Для более резкого окна
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Установка
root = Tk()
root.title('Type Speed Test')

# Устанавливаем разрешение окна
root.geometry('700x700')

# Устанавливаем шрифт для текста в лейблах и кнопках
root.option_add("*Label.Font", "consolas 30")
root.option_add("*Button.Font", "consolas 30")


# генерируют строки для теста
def resetwritinglables():
	startlabel.destroy()
	startbutton.destroy()
	possibletext = [
		'For writers, a random sentence can help them get their creative juices flowing. Since the topic of the '
		'sentence is completely unknown, it forces the writer to be creative when the sentence appears. There are a '
		'number of different ways a writer can use the random sentence for creativity. The most common way to use the '
		'sentence is to begin a story. Another option is to include it somewhere in the story. A much more difficult '
		'challenge is to use it to end a story. In any of these cases, it forces the writer to think creatively since '
		'they have no idea what sentence will appear from the tool.',
		'The goal of Python Code is to provide Python tutorials, recipes, problem fixes and articles to beginner and '
		'intermediate Python programmers, as well as sharing knowledge to the world. Python Code aims for making '
		'everyone in the world be able to learn how to code for free. Python is a high-level, interpreted, '
		'general-purpose programming language. Its design philosophy emphasizes code readability with the use of '
		'significant indentation. Python is dynamically-typed and garbage-collected. It supports multiple programming '
		'paradigms, including structured (particularly procedural), object-oriented and functional programming. It is '
		'often described as a "batteries included" language due to its comprehensive standard library.',
		'As always, we start with the imports. Because we make the UI with tkinter, we need to import it. We also '
		'import the font module from tkinter to change the fonts on our elements later. We continue by getting the '
		'partial function from functools, it is a genius function that excepts another function as a first argument '
		'and some args and kwargs and it will return a reference to this function with those arguments. This is '
		'especially useful when we want to insert one of our functions to a command argument of a button or a key '
		'binding.'
	]
	text = random.choice(possibletext).lower()
	# определение места разделения текста
	splitpoint = 0

	# Здесь уже написан текст
	global labelleft
	labelleft = Label(root, text=text[0:splitpoint], fg='grey')
	labelleft.place(relx=0.5, rely=0.5, anchor=E)

	# Вот текст, который будет написан
	global labelright
	labelright = Label(root, text=text[splitpoint:])
	labelright.place(relx=0.5, rely=0.5, anchor=W)

	# Эта метка показывает пользователю, какую букву нужно нажать.
	global currentletterlabel
	currentletterlabel = Label(root, text=text[splitpoint], fg='grey')
	currentletterlabel.place(relx=0.5, rely=0.6, anchor=N)

	# Эта метка показывает пользователю, сколько времени прошло
	global timeleftlabel
	timeleftlabel = Label(root, text=f'0 Seconds', fg='grey')
	timeleftlabel.place(relx=0.5, rely=0.4, anchor=S)

	global writeable
	writeable = True
	root.bind('<Key>', keypress)

	global passedseconds
	passedseconds = 0

	# Привязка обратных вызовов к функциям через определенное время.
	root.after(60000, stoptest)
	root.after(1000, addsecond)


# фунцкия остановки теста. она будет вызвана корнем через 60сек, затем подсчитает количество строк написанных юзером,
# мы достаем текст из левой метки (лейбл) разбивая его по пустым местам и считаем длину списка, после уничтожаем
# метки из теста
def stoptest():
	global writeAble
	writeAble = False

	# Подсчет количества слов
	amountwords = len(labelleft.cget('text').split(' '))

	# Уничтожает ненужные виджеты.
	timeleftlabel.destroy()
	currentletterlabel.destroy()
	labelright.destroy()
	labelleft.destroy()

	# Отображение результатов теста
	global resultlabel
	resultlabel = Label(root, text=f'Words per Minute: {amountwords}', fg='black')
	resultlabel.place(relx=0.5, rely=0.4, anchor=CENTER)

	# Кнопка перезапуска
	global resultbutton
	resultbutton = Button(root, text=f'Retry', command=restart)
	resultbutton.place(relx=0.5, rely=0.6, anchor=CENTER)


def restart():
	# Очищает экран от лейбла с результатами
	resultlabel.destroy()
	resultbutton.destroy()

	# вызываем фунцкию запуска теста.
	resetwritinglables()


def addsecond():
	global passedseconds
	passedseconds += 1
	timeleftlabel.configure(text=f'{passedseconds} Seconds')

	# вызывает эту функцию еще раз через одну секунду, если время не истекло.
	if writeable:
		root.after(1000, addsecond)


def keypress(event=None):
	try:
		if event.char.lower() == labelright.cget('text')[0].lower():
			# Удаление одного символа с правой стороны.
			labelright.configure(text=labelright.cget('text')[1:])

			# Удаление одного символа с правой стороны..
			labelleft.configure(text=labelleft.cget('text') + event.char.lower())

			# Ставим след букву в лейбл
			currentletterlabel.configure(text=labelright.cget('text')[0])
	except tkinter.TclError:
		pass


def start():
	global startlabel
	startlabel = Label(root, text="Вы готовы?", fg='black')
	startlabel.place(relx=0.5, rely=0.4, anchor=CENTER)

	global startbutton
	startbutton = Button(root, text=f'Начать тест', command=resetwritinglables)
	startbutton.place(relx=0.5, rely=0.6, anchor=CENTER)


start()
root.mainloop()
