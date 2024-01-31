class Animal:
    def  __init__(self, animal_type:str, color:str, long_age:int):
        self.animal_type=animal_type
        self.color=color
        self.age=long_age
    def info(self):
        return f"""
    animal tipi  : {self.animal_type}
    animal rangi : {self.color}
    animal yoshi : {self.age}
    """
    
class Dog (Animal):
    def __init__(self, animal_type:str, color:str, long_age:int, speed:int, sum_teeth):
        super().__init__(animal_type, color, long_age)
        self.speed=speed
        self.sum_teeth=sum_teeth
    def __str__(self):
        return f"""
    {super().info()}animal tezligi: {self.speed}
    animal tishlari soni {self.sum_teeth}
    """

class Horse (Animal):
    def __init__(self, animal_type:str, color:str, long_age:int, speed:int, sum_teeth):
        super().__init__(animal_type, color, long_age)
        self.speed=speed
        self.sum_teeth=sum_teeth
    def __str__(self):
        return f"""
    {super().info()}animal tezligi: {self.speed}
    animal tishlari soni {self.sum_teeth}
    """


class Cat (Animal):
    def __init__(self, animal_type:str, color:str, long_age:int, speed:int, sum_teeth):
        super().__init__(animal_type, color, long_age)
        self.speed=speed
        self.sum_teeth=sum_teeth
    def __str__(self):
        return f"""
    {super().info()}animal tezligi: {self.speed}
    animal tishlari soni {self.sum_teeth}
    """


a=Dog("It", "qora", 3, 30, 35)
b=Horse("Ot", "orange", 5, 100, 30)
c=Cat("Mushuk", "black", 4, 21, 30)
hayvonlar=[a,b,c]
print(max(hayvonlar, key=lambda a: a.speed))
print(max(hayvonlar, key=lambda a: a.sum_teeth))