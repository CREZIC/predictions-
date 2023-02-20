from tkinter import *
from tkinter import messagebox
import random

answer=['Да', 'Нет', 'Наверное', 'Пока не ясно попробуй снова', '100% да']
def click():
    messagebox.showinfo('Мой ответ', random.choice(answer))
    return
root=Tk()
root.title('Квадрат предсказаний')
root.geometry('300x300')
F = Button(root, text='взмахнуть', width=15, height=2, bg='black', command=click)
root.mainloop()
