from food import Food
from tank import Tank
# -*- coding: utf-8 -*
import serial
import time

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

fruit_list = ['fruit','apple', 'banana', 'orange']
meat_list = ['meat','beef', 'pork', 'fish']
drinking_list = ['drinking', 'milk', 'yogurt', 'coke']

food_database = [fruit_list, meat_list, drinking_list]

for list in food_database:
    if detection_result in list:
        detection_attribute = list[0]
        new_food = Food(detection_result, detection_attribute)
        break

fridge = []
for i in range(6):
    tank = Tank()
    fridge.append(tank)

new_food_2 = Food('orange', 'fruit')
fridge[0].add_food(new_food)
fridge[0].add_food(new_food_2)

for tank in fridge:
    tank.print_content()


