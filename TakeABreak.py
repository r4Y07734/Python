import tkinter as tk
import random
import webbrowser
import time
from tkinter import messagebox

a='https://www.youtube.com/watch?v=4C-ifmRfBNA'
b='https://www.youtube.com/watch?v=uHKfrz65KSU'
c='https://www.youtube.com/watch?v=VPFvIauSusY'
d='https://www.youtube.com/watch?v=SB-qEYVdvXA'
e='https://www.youtube.com/watch?v=U--FXc2ox9I'
y='https://www.youtube.com/watch?v=q_7Y24A6oFY'
g='https://www.youtube.com/watch?v=eX2qFMC8cFo'
h='https://www.youtube.com/watch?v=cytJLvf-eVs'
i='https://www.youtube.com/watch?v=XyNlqQId-nk'
j='https://www.youtube.com/watch?v=ucQe-3XLEDE'

x=10

while x == 10:

    f=random.randint(1,10)

    time.sleep(2700)

    result=messagebox.askyesno(title = 'Breaker', message = 'Keep a break', detail = 'Want to keep a break')

    if not result:
        print('nothing')
        
    else:
        if f == 1:
            webbrowser.open(a)
        elif f == 2:
            webbrowser.open(b)
        elif f == 3:
            webbrowser.open(c)
        elif f == 4:
            webbrowser.open(d)
        elif f == 5:
            webbrowser.open(e)
        elif f == 6:
            webbrowser.open(y)
        elif f == 7:
            webbrowser.open(g)
        elif f == 8:
            webbrowser.open(h)
        elif f == 9:
            webbrowser.open(i)
        elif f == 10:
            webbrowser.open(j)

