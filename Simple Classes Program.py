#2018 Aymaan Shaikh
#
class One:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)

P1 = One("Tom", "red", 30)
P2 = One("Jerry", "blue", 40)

P1.introduce_self()
P2.introduce_self()
