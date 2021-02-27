

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say(self):
        return "我叫" + self.name +"；今年" + str(self.age) + "岁了！"