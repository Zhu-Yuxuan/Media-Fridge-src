import threading
from tkinter import *
from tank import Tank
from food import Food
import serial
import time
import tkinter.font as tkFont
# import RPi.GPIO as GPIO

name = ["保鲜室1", "保鲜室2", "保鲜室3", "保鲜室4", "保鲜室5", "保鲜室6"]
temp = [0, 0, 0, 0, 0, 0]
mois = [80, 80, 80, 80, 80, 80]
type = ["默认", "默认", "默认", "默认", "默认", "默认"]
info = ["箱体清空，已恢复默认模式！", "箱体清空，已恢复默认模式！", "箱体清空，已恢复默认模式！", "箱体清空，已恢复默认模式！", "箱体清空，已恢复默认模式！", "箱体清空，已恢复默认模式！"]
colo = ["white", "white", "white", "white", "white", "white"]
fruit_list = ['fruit', 'apple', 'banana', 'orange', 'peach', 'pear', 'berry', 'pineapple', 'melon', 'radish', 'tomato', 'cucumber', 'pumpkin']
vegetable_list = ['vegetable', 'mushroom', 'spinach', 'celery', 'caraway', 'lettuce', 'agaric', 'lotus root', 'water shield', 'arrowhead', 'cress']
meat_list = ['meat', 'beef', 'pork', 'fish', 'egg', 'mutton', 'chicken', 'duck']
drinking_list = ['drinking', 'milk', 'yogurt', 'coke', 'beer', 'vodka']
food_database = [fruit_list, vegetable_list, meat_list, drinking_list]
temperature_reco = [10, 3, 0, 5]
moisture_reco = [95, 95, 85, 90]
typename = ["水果与喜温蔬菜", "喜凉蔬菜", "禽畜肉与蛋", "甜点，饮品"]

class GUI():
    def __init__(self, root):
        self.initGUI(root)
    def Update(self):
        global temp, mois, type
        for i in range(6):
            self.content[2][i].config(text=type[i])
            self.content[3][i].config(text=temp[i])
            self.content[4][i].config(text=mois[i])
            self.content[6][i].config(text=info[i])
            self.framelist[i].config(bg=colo[i])
        self.root.after(1000, self.Update)
    def initGUI(self, root):
        global temp, mois, type
        self.root = root
        self.root.geometry("1024x600")
        self.root.title("Frodge UI")
        self.framelist = []
        self.content = [[], [], [], [], [], [], []]
        # init list
        for i in range(6):
            self.framelist.append(Frame())
            self.content[0].append(Label()) # name
            self.content[1].append([Label(), Label(), Label()])  # fix
            self.content[2].append(Label())  # type
            self.content[3].append(Label())  # tempture
            self.content[4].append(Label())  # moisture
            self.content[5].append([Label(), Label()])  # unit
            self.content[6].append(Label()) # information
        # init frame
        for i in range(6):
            self.framelist[i] = Frame(self.root, height=300, width=341, bg=colo[i])
            self.framelist[i].grid_propagate(0)
            self.content[0][i] = Label(self.framelist[i], text=name[i], bg=colo[i], font="Fixdsys 15 bold") # name
            self.content[1][i][0] = Label(self.framelist[i], text="类型：", bg=colo[i], font="Fixdsys 12") # fixed properties
            self.content[1][i][1] = Label(self.framelist[i], text="温度：", bg=colo[i], font="Fixdsys 12")
            self.content[1][i][2] = Label(self.framelist[i], text="湿度：", bg=colo[i], font="Fixdsys 12")
            self.content[2][i] = Label(self.framelist[i], text=type[i], bg=colo[i],font="Fixdsys 12") # type
            self.content[3][i] = Label(self.framelist[i], text=temp[i], bg=colo[i],font="Fixdsys 12") # temperature
            self.content[4][i] = Label(self.framelist[i], text=mois[i], bg=colo[i],font="Fixdsys 12") # moisture
            self.content[5][i][0] = Label(self.framelist[i], text="°C", bg=colo[i],font="Fixdsys 12") # unit
            self.content[5][i][1] = Label(self.framelist[i], text="%", bg=colo[i],font="Fixdsys 12")
            self.content[6][i] = Label(self.framelist[i], text=info[i], bg=colo[i],font="Fixdsys 12") # information: warning, reminding
            self.content[0][i].grid(row=0, column=1, columnspan=3)
            self.content[1][i][0].grid(row=1, column=1)
            self.content[1][i][1].grid(row=2, column=1)
            self.content[1][i][2].grid(row=3, column=1)
            self.content[2][i].grid(row=1, column=2)
            self.content[3][i].grid(row=2, column=2)
            self.content[4][i].grid(row=3, column=2)
            self.content[5][i][0].grid(row=2 ,column=3)
            self.content[5][i][1].grid(row=3, column=3)
            self.content[6][i].grid(row=4, column=1, columnspan=3, pady = 15)
            self.framelist[i].grid(row=i // 3, column=i % 3)
        self.root.after(1000, self.Update)
        self.root.mainloop()
def image_detect():
    result_str = ""
    ser = serial.Serial('/dev/ttyAMA0', 9600) # 9600为波特率，通信双方要保持一致
    if ser.isOpen == False:
        ser.open() # 打开串口
    #ser.write(b"Raspberry pi is ready")
    try:
        while True:
            size = ser.inWaiting()               # 获得缓冲区字符
            if size != 0:
                response = ser.read(size)        # 读取内容并显示
                try:
                    result_str = response.decode()
                    if result_str[0] == '/':
                        result_str = result_str[1:-4]
                        # print(result_str)
                        break
                except:
                    pass
                ser.flushInput()                 # 清空接收缓存区
                time.sleep(0.1)                  # 软件延时
    except KeyboardInterrupt:
        pass
    ser.close()
    return result_str
def fridgeUI():
    root = Tk()
    fUI = GUI(root)
def fetch_w():
    result_str = ""
    ser = serial.Serial('/dev/ttyAMA1', 9600)  # 9600为波特率，通信双方要保持一致
    if ser.isOpen == False:
        ser.open()  # 打开串口
    # ser.write(b"Raspberry pi is ready")
    try:
        while True:
            try:
                size = ser.inWaiting()  # 获得缓冲区字符
                if size != 0:
                    response = ser.read(size)  # 读取内容并显示
                    try:
                        result_str = response.decode().strip()
                    except:
                        pass
                    ser.flushInput()  # 清空接收缓存区
                result_float = float(result_str)
                print(result_float)
            except:
                pass
    except KeyboardInterrupt:
        pass
    ser.close()
    return result_float
    return 10.0
def logic(fridge):
    global temp, mois, type
    w_threshold = 1000.0
    w_cur = fetch_w()
    while True:
        w_pre = w_cur
        w_cur = fetch_w()
        if w_cur - w_pre > 5000:
            foodname = image_detect()
            food = find_food(foodname)
            if food.attribute == fridge[0].attribute or fridge[0].attribute == 'empty':
                temp[0] = temperature_reco[food.num]
                mois[0] = moisture_reco[food.num]
                type[0] = typename[food.num]
                fridge[0].add_food(food)
                if foodname not in fridge[0].containing_food_list:
                    info[0] = "食材{}添加成功！".format(foodname)
                    colo[0] = "green"
                time.sleep(2)
                info[0] = ""
            else:
                info[0] = "该食材不应该放置在此箱体！"
                colo[0] = "red"
        elif w_cur < w_threshold:
            fridge[0].remove_all()
            temp[0] = 0
            mois[0] = 80
            type[0] = "默认"
            info[0] = "箱体清空，已恢复默认模式！"
            colo[0] = ""


def find_food(foodname):
    if foodname in fruit_list:
        return Food(foodname, fruit_list[0], 0)
    elif foodname in vegetable_list:
        return Food(foodname, vegetable_list[0], 1)
    elif foodname in meat_list:
        return Food(foodname, meat_list[0], 2)
    elif foodname in drinking_list:
        return Food(foodname, drinking_list[0], 3)
    else:
        print("请选择食材类型:\n")
        print("1. 水果、根茎菜、瓜果菜、豆\n")
        print("2. 叶菜、菌菇、水生蔬菜\n")
        print("3. 禽肉、畜肉、蛋、鱼\n")
        print("4. 饮料、奶制品、酒类、甜点\n")
        str = input()
        food_database[int(str)-1].append(foodname)
        return Food(foodname, food_database[int(str)-1][0], int(str)-1)

def terminal_simu(fridge):
    while True:
        str = input ("命令：")
        if str[0] in ['1', '2', '3', '4', '5', '6']:
            if str[1] == '+':
                food = find_food(str[2:])
                if food.attribute == fridge[int(str[0])-1].attribute or fridge[int(str[0])-1].attribute == 'empty':
                    temp[int(str[0])-1] = temperature_reco[food.num]
                    mois[int(str[0])-1] = moisture_reco[food.num]
                    type[int(str[0])-1] = typename[food.num]
                    fridge[int(str[0])-1].add_food(food)
                else:
                    print("该食材不应该放置在此箱体！")
            elif str[1] == '-':
                fridge[int(str[0])-1].remove_food(find_food(str[2:]))
                if len(fridge[int(str[0])-1].containing_food_list) == 0:
                    temp[int(str[0])-1] = 0
                    mois[int(str[0])-1] = 80
                    type[int(str[0])-1] = "默认"
            elif str[1:] == "check":
                for n in fridge[int(str[0])-1].containing_food_list:
                    print(n.name, " ")
            else:
                print("无效命令，请重新输入！")
        elif str == "quit":
            break
        else:
            print("无效命令，请重新输入！")

if __name__ == "__main__":
    fridge = [Tank(), Tank(), Tank(), Tank(), Tank(), Tank()]

    t1 = threading.Thread(target=fridgeUI)
    t2 = threading.Thread(target=logic, args=(fridge,))
    t1.start()
    t2.start()
