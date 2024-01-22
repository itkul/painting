import turtle as t
import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser

t.speed(100)
t.penup()
t.goto(-300, 200)
t.pendown()
t.circle(20)    #Создаёт иконку круга

t.penup()
t.goto(-270, 200)   #Создаёт иконку квадрата
t.pendown()
for i in range(4):
    t.fd(40)
    t.lt(90)
    
t.penup()
t.goto(-220, 200)   #Создаёт иконку прямоугольника
t.pendown()
for i in range(2):
    t.fd(60)
    t.lt(90)
    t.fd(40)
    t.lt(90)
    
t.penup()
t.goto(-150, 200)   #Создаёт иконку треугольника
t.pendown()
for i in range(3):
    t.fd(40)
    t.lt(120)
    
t.penup()
t.goto(-320, 155)   #Создаёт иконку ломанной
t.pendown()
t.lt(50)
t.fd(30)
t.rt(45)
t.fd(20)
t.rt(80)
t.fd(20)
t.rt(40)
t.fd(10)
t.lt(115)

t.penup()
t.goto(-260, 155)   #Создаёт иконку замкнутой 
t.pendown()
t.lt(50)
t.fd(30)
t.rt(45)
t.fd(20)
t.rt(80)
t.fd(20)
t.rt(40)
t.fd(10)
t.lt(115)
t.goto(-260, 155)

t.penup()
t.goto(250, 200)    #Создаёт иконку ластика
t.pendown()
t.lt(45)
t.fd(56)
t.rt(45)
t.penup()
t.goto(250, 240)
t.rt(45)
t.pendown()
t.fd(56)
t.lt(45)

func_number = ''    #хранит названия функций

first_click_broken = True   #необходимы для функционирования ломаной и замкнутой
first_click_closed = True

color_fill = ''     #хранят цвета
stroke_color = 'black'

size = 1    #толщина пера

s_len = 40      #размеры фигур
c_len = 50
t_len = 40
r_len = 60
r_len1 = 40

x1 = 0  #переменные для возвращения конца замкнутой ломаной в начало
y1 = 0

def mclick(x, y):   
    global func_number
    if -320 <= x <= -280 and 200 <= y <= 240:   #определяет название функции
        func_number = 'circle'
        return
    elif -270 <= x <= -230 and 200 <= y <= 240:
        func_number = 'square'
        return
    elif -220 <= x <= -160 and 200 <= y <= 240:
        func_number = 'rectangle'
        return
    elif -320 <= x <= -270 and 150 <= y <= 190:
        func_number='brokenline'
        return
    elif -260 <= x <= -210 and 150 <= y <= 190:
        func_number = 'closedline'
        return
    elif -150 <= x <= -110 and 200 <= y <= 240:
        func_number = 'triangle'
        return
    elif 250 <= x <= 300 and 200 <= y <= 240:
        func_number ='delete'
        return
    
    if func_number == 'circle':     #активирует функции 
        circle(x, y)
    elif func_number == 'square':
        square(x, y)
    elif func_number == 'rectangle':
        rectangle(x, y)
    elif func_number == 'brokenline':
        brokenline(x, y)
    elif func_number == 'closedline':
        closedline(x, y)
    elif func_number == 'triangle':
        triangle(x, y)
    elif func_number == 'delete':
        delete1(x, y)
 
def select_color_fill():    #определяет цвет заливки
        global color_fill
        result = colorchooser.askcolor(initialcolor = "black")
        color_fill = result[1]
        return color_fill
    
open_button = ttk.Button(text = "Выбрать цвет заливки", command = select_color_fill) #кнопка для выбора цвета заливки
open_button.pack(side = 'left', padx = 10, pady = 10)

def select_stroke_color():      #определяет цвет контура
        global stroke_color
        result = colorchooser.askcolor(initialcolor = "black")
        stroke_color = result[1]
        return stroke_color
    
open_button = ttk.Button(text = "Выбрать цвет контура", command = select_stroke_color) #кнопка для выбора цвета контура
open_button.pack(side = 'left', padx = 10, pady = 10)

def figures(): #создаёт окно для введения размеров фигур
    
    def len_figures():  #определяет размеры фигур
        global s_len, c_len, t_len, r_len, r_len1
        len = square_len.get()
        if len:
            s_len = int(len)
        len = circle_len.get()
        if len:
            c_len = int(len)
        len = triangle_len.get()
        if len:
            t_len = int(len)
        len = rectangle_len.get()
        if len:
            r_len = int(len)
        len = rectangle_len1.get()
        if len:
            r_len1 = int(len)
        win.destroy()
        return s_len, c_len, t_len, r_len, r_len1
    
    win = tk.Tk()
    win.title('Выбор')
    win.geometry('600x150+650+300')
    ttk.Label(win,
              text = 'Укажите размер стороны квадрата:').grid(row = 1, column = 1)
    ttk.Label(win,
              text = 'Укажите размер радиуса круга:').grid(row = 2, column = 1)
    ttk.Label(win,
              text = 'Укажите размер стороны треугольника:').grid(row = 3, column = 1)
    ttk.Label(win,
              text = 'Укажите размер сторон прямоугольника:').grid(row = 4, column = 1)
    
    square_len = ttk.Entry(win)
    square_len.grid(row = 1, column = 2)
    circle_len = ttk.Entry(win)
    circle_len.grid(row = 2, column = 2)
    triangle_len = ttk.Entry(win)
    triangle_len.grid(row = 3, column = 2)
    rectangle_len = ttk.Entry(win)
    rectangle_len.grid(row = 4, column = 2)
    rectangle_len1 = ttk.Entry(win)
    rectangle_len1.grid(row = 4, column = 3)
    
    btn = ttk.Button(win, text = 'Ok',command = len_figures).grid(row = 5, column = 2)

open_button = ttk.Button(text = "Выбрать размер фигуры", command = figures)     #кнопка для выбора размеров фигур
open_button.pack(side = 'left', padx = 10, pady = 10)

def sizes(): #создаёт окно для введения толщины пера
    
    def pen():      #определяет толщину пера
        global size
        size1 = pen_size.get()
        if size1:
            size = int(size1)
        win.destroy()
        
    win = tk.Tk()
    win.title('Выбор')
    win.geometry('400x150+650+300')
    ttk.Label(win, text = '').grid(row = 1, column = 1)
    ttk.Label(win, text = 'Укажите размер пера:').grid(row = 2, column = 1)
    pen_size = ttk.Entry(win)
    pen_size.grid(row = 2, column = 2)
    btn = ttk.Button(win, text = 'Ok', command = pen).grid(row = 3, column = 1)

open_button = ttk.Button(text = "Выбрать размер пера", command = sizes)     #кнопка для выбора толщины пера
open_button.pack(side = 'left', padx = 10, pady = 10)

def circle(x, y):   #рисует круг
    global first_click_broken, first_click_closed
    if -320 <= x <= 300 and 150 <= y <= 240:    #ограничивает зону рисунка
        return
    
    else:
        first_click_broken = True
        first_click_closed = True
        t.pensize(size)
        t.color(stroke_color, color_fill)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.begin_fill()
        t.circle(c_len)
        t.end_fill()
    
def square(x, y):   #рисует квадрат
    global first_click_broken, first_click_closed
    if -320 <= x <= 300 and 150 <= y <= 240:
        return
    
    else:
        first_click_broken = True
        first_click_closed = True
        t.pensize(size)
        t.color(stroke_color, color_fill)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.begin_fill()
        for i in range(4):
            t.fd(s_len)
            t.lt(90)
        t.end_fill()

def rectangle(x, y):    #рисует прямоугольник
    global first_click_broken, first_click_closed
    if -320 <= x <= 300 and 150 <= y <= 240:
        return
    
    else:
        first_click_broken = True
        first_click_closed = True
        t.pensize(size)
        t.color(stroke_color, color_fill)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.begin_fill()
        for i in range(2):
            t.fd(r_len)
            t.lt(90)
            t.fd(r_len1)
            t.lt(90)
        t.end_fill()

def triangle(x, y):     #рисует треугольник
    global first_click_broken, first_click_closed
    if -320 <= x <= 300 and 150 <= y <= 240:
        return
    
    else:
        first_click_broken = True
        first_click_closed = True
        t.pensize(size)
        t.color(stroke_color, color_fill)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.begin_fill()
        for i in range(3):
            t.fd(t_len)
            t.lt(120)
        t.end_fill()

def brokenline(x, y):   #рисует ломаную
    global first_click_broken, first_click_closed
    if -320 <= x <= 300 and 150 <= y <= 240:
        return
    
    else:
        first_click_closed = True
        t.pensize(size)
        t.color(stroke_color)
        if first_click_broken:
            first_click_broken = False
            t.penup()
            t.goto(x, y)
            t.pendown()
        else:
            t.goto(x, y)

def closedline(x, y):   #рисует замкнутую ломаную
    global first_click_closed, first_click_broken, x1, y1
    if -320 <= x <= 300 and 150 <= y <= 240:
        return
    
    else:
        first_click_broken = True
        t.pensize(size)
        t.color(stroke_color)
        if first_click_closed:
            first_click_closed = False
            t.penup()
            t.goto(x, y)
            x1 = t.xcor()
            y1 = t.ycor()
            t.pendown()
            return x1, y1
        else:
            t.goto(x, y)

def closed():   #соединяет начало и конец замкнутой ломаной 
    global x1, y1
    t.goto(x1, y1)

def delete1(x, y):  #ластик 
    global first_click_broken, first_click_closed
    if -320 <= x <= 300 and 150 <= y <= 240:
        return
    
    else:
        first_click_broken = True
        first_click_closed = True
        t.color('white', 'white')
        t.pensize(size)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.begin_fill()
        t.circle(50)
        t.end_fill()

t.onscreenclick(mclick)
t.listen()
t.onkey(closed, ' ')
t.mainloop()
