from tkinter import *

root = Tk()
# 生成6个格子
for i in range(6):
    # 设置每个格子的背景颜色和字体属性
    if i % 2 == 0:
        font_color = "white"
        background_color = "#d1d1d1"
    else:
        font_color = "black"
        background_color = "#fafafa"
    # type = Label(root, text="类型：默认\n温度：0°C\n湿度：95%", fg=font_color, bg=background_color, height=17, width=47)
    frame = Frame(root, height=300, width=341)
    frame.grid_propagate(0)
    type = Label(frame, text="类型：默认")
    temp = Label(frame, text="温度：0°C")
    mois = Label(frame, text="湿度：95%")
    type.pack()
    temp.pack()
    mois.pack()

    # temp = Label(root, text="温度：0°C", fg=font_color, bg=background_color, height=5, width=7)
    # mois = Label(root, text="温度：0°C", fg=font_color, bg=background_color, height=5, width=7)

    # 将格子放在合适的位置
    frame.grid(row=i // 3, column=i % 3, sticky='nswe')
    # temp.grid(row=i // 3, column=i % 3)
    # mois.grid(row=i // 3, column=i % 3)

root.mainloop()
