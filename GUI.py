import threading
from tkinter import *
from tank import Tank
from food import Food
# import RPi.GPIO as GPIO

temp = [0, 0, 0, 0, 0, 0]
mois = [80, 80, 80, 80, 80, 80]
type = ["默认", "默认", "默认", "默认", "默认", "默认"]
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
            self.content[1][i].config(text=type[i])
            self.content[2][i].config(text=temp[i])
            self.content[3][i].config(text=mois[i])
        self.root.after(1000, self.Update)
    def initGUI(self, root):
        global temp, mois, type
        self.root = root
        self.root.geometry("1024x600")
        self.root.title("Frodge UI")
        self.framelist = []
        self.content = [[], [], [], [], []]
        # init list
        for i in range(6):
            self.framelist.append(Frame())
            self.content[0].append([Label(), Label(), Label()])  # fix
            self.content[1].append(Label())  # type
            self.content[2].append(Label())  # tempture
            self.content[3].append(Label())  # moisture
            self.content[4].append([Label(), Label()])  # unit
        # init frame
        for i in range(6):
            self.framelist[i] = Frame(self.root, height=300, width=341)
            self.framelist[i].grid_propagate(0)
            self.content[0][i][0] = Label(self.framelist[i], text="类型：").grid(row=1, column=1)
            self.content[0][i][1] = Label(self.framelist[i], text="温度：").grid(row=2, column=1)
            self.content[0][i][2] = Label(self.framelist[i], text="湿度：").grid(row=3, column=1)
            self.content[1][i] = Label(self.framelist[i], text=type)
            self.content[2][i] = Label(self.framelist[i], text=temp)
            self.content[3][i] = Label(self.framelist[i], text=mois)
            self.content[4][i][0] = Label(self.framelist[i], text="°C").grid(row=2, column=3)
            self.content[4][i][1] = Label(self.framelist[i], text="%").grid(row=3, column=3)
            self.content[1][i].grid(row=1, column=2)
            self.content[2][i].grid(row=2, column=2)
            self.content[3][i].grid(row=3, column=2)
            self.framelist[i].grid(row=i // 3, column=i % 3)
        self.root.after(1000, self.Update)
        self.root.mainloop()
def fridgeUI():
    root = Tk()
    fUI = GUI(root)
def logic():
    global temp, mois, type
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
    t2 = threading.Thread(target=terminal_simu, args=(fridge,))
    t1.start()
    t2.start()
