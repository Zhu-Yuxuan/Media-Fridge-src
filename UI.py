#!/usr/bin/python
# -*- coding: UTF-8 -*-

from tkinter import *
def say_hi():
    print("hello ~ !")
root = Tk()
frame = Frame(root, height = 600, width = 1024)
frame.pack()
frame1 = Frame(frame, height= 300, width=341)
frame2 = Frame(frame, height= 300, width=341)
frame3 = Frame(frame, height= 300, width=341)
frame4 = Frame(frame, height= 300, width=341)
frame5 = Frame(frame, height= 300, width=341)
frame6 = Frame(frame, height= 300, width=341)
frame1.grid_propagate(0)
frame2.grid_propagate(0)
frame3.grid_propagate(0)
frame4.grid_propagate(0)
frame5.grid_propagate(0)
frame6.grid_propagate(0)

root.title("tkinter frame")

type1 = Label(frame1, text="类型：默认", width=47)
temp1 = Label(frame1, text="温度：0°C")
mois1 = Label(frame1, text="湿度：95%")
type1.grid(row=1, column=1)
temp1.grid(row=2, column=1)
mois1.grid(row=3, column=1)

type2 = Label(frame2, text="类型：默认", width=47)
temp2 = Label(frame2, text="温度：0°C")
mois2 = Label(frame2, text="湿度：95%")
type2.grid(row=1, column=1)
temp2.grid(row=2, column=1)
mois2.grid(row=3, column=1)

type3 = Label(frame3, text="类型：默认", width=47)
temp3 = Label(frame3, text="温度：0°C")
mois3 = Label(frame3, text="湿度：95%")
type3.grid(row=1, column=1)
temp3.grid(row=2, column=1)
mois3.grid(row=3, column=1)

type4 = Label(frame4, text="类型：默认", width=47)
temp4 = Label(frame4, text="温度：0°C")
mois4 = Label(frame4, text="湿度：95%")
type4.grid(row=1, column=1)
temp4.grid(row=2, column=1)
mois4.grid(row=3, column=1)

type5 = Label(frame5, text="类型：默认", width=47)
temp5 = Label(frame5, text="温度：0°C")
mois5 = Label(frame5, text="湿度：95%")
type5.grid(row=1, column=1)
temp5.grid(row=2, column=1)
mois5.grid(row=3, column=1)

type6 = Label(frame6, text="类型：默认", width=47)
temp6 = Label(frame6, text="温度：0°C")
mois6 = Label(frame6, text="湿度：95%")
type6.grid(row=1, column=1)
temp6.grid(row=2, column=1)
mois6.grid(row=3, column=1)

frame1.grid(row=1, column=1)
frame2.grid(row=1, column=2)
frame3.grid(row=1, column=3)
frame4.grid(row=2, column=1)
frame5.grid(row=2, column=2)
frame6.grid(row=2, column=3)
frame1.update()
print("frame size: ", frame1.winfo_width(), frame1.winfo_height())
root.mainloop()