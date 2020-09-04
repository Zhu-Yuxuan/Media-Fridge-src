from tkinter import *
import threading
import time

def detect():
    global temp
    while True:
        temp -= 1
        time.sleep(1)
        print(temp)
    # functions

def update(root):
    root.update()
    root.after(1000, update(root))

def gui():
    global temp
    root = Tk()
    root.geometry("1024x600")
    root.title("Frodge UI")

    framelist = []
    content = [[], [], [], [], []]
    # init list
    for i in range(6):
        framelist.append(Frame())
        content[0].append([Label(), Label(), Label()])  # fix
        content[1].append(Label())  # type
        content[2].append(Label())  # tempture
        content[3].append(Label())  # moisture
        content[4].append([Label(), Label()])  # unit
    # init frame
    for i in range(6):
        framelist[i] = Frame(root, height=300, width=341)
        framelist[i].grid_propagate(0)
        content[0][i][0] = Label(framelist[i], text="类型：")
        content[0][i][1] = Label(framelist[i], text="温度：")
        content[0][i][2] = Label(framelist[i], text="湿度：")
        content[1][i] = Label(framelist[i], text=type)
        content[2][i] = Label(framelist[i], text="0")
        content[3][i] = Label(framelist[i], text=temp)
        content[4][i][0] = Label(framelist[i], text="°C")
        content[4][i][1] = Label(framelist[i], text="%")
        content[0][i][0].grid(row=1, column=1)
        content[0][i][1].grid(row=2, column=1)
        content[0][i][2].grid(row=3, column=1)
        content[1][i].grid(row=1, column=2)
        content[2][i].grid(row=2, column=2)
        content[3][i].grid(row=3, column=2)
        content[4][i][0].grid(row=2, column=3)
        content[4][i][1].grid(row=3, column=3)
        framelist[i].grid(row=i // 3, column=i % 3)

    root.after(1000, update(root))
    root.mainloop()

if __name__ =='__main__':
    global temp
    temp = 95
    t1 = threading.Thread(target=gui)
    t2 = threading.Thread(target=detect)
    t1.start()
    t2.start()