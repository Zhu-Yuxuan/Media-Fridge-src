class Tank:

    def __init__(self):
        self.attribute = 'empty'
        self.containing_food_list = []

    def add_food(self, new_food):
        flag = self.check_empty()
        if flag:
            print("创建新仓：{}".format(new_food.attribute))
            self.attribute = new_food.attribute

        if new_food.attribute == self.attribute:
            self.containing_food_list.append(new_food)
            print("食材{}添加成功！".format(new_food.name))
        else:
            print("该食材不应该放置在此箱体！")
    def remove_food(self, food_t):
        for food in self.containing_food_list:
            if food_t.name == food.name:
                self.containing_food_list.remove(food)
                print("食材{}取出成功！".format(food.name))
                break
        if len(self.containing_food_list) == 0:
            self.attribute = 'empty'
            print("箱体清空，已恢复默认模式！")

    def remove_all(self):
        self.attribute = 'empty'
        self.containing_food_list = []
        print("箱体清空，已恢复默认模式！")

    def check_empty(self):
        if len(self.containing_food_list) == 0:
            return True
        else:
            return False

    def print_content(self):
        print("----------")
        for food in self.containing_food_list:
            print(food.name)
        print("舱体类型：{}".format(self.attribute))
        