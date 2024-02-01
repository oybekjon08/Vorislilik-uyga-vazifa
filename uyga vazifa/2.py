class Uy:
    def __init__ (self, type:str, sum_rum:int, area:int, price:int):
        self.type=type
        self.rooms=sum_rum
        self.area=area
        self.price=price
    def get_price(self):
        return self.price
    def get_info(self):
        return f"""
    tipi : {self.type}
    xonalar soni : {self.rooms}
    maydoni : {self.area}
    narhi : {self.price}
    """
class Flat(Uy):
    def __init__ (self, location:str, condition:str,type:str, sum_rum:int, area:int, price:int):
        super().__init__(type, sum_rum, area, price)
        self.location=location
        self.coondition=condition
    def get_price(self):
        return f"""
    {self.get_info()}
    """
    def set_price(self, newPrice:int):
        self.price=newPrice
    
    def __str__(self):
        return  super().get_info()

class House(Uy):
    def __init__ (self, location:str, condition:str,type:str, sum_rum:int, area:int, price:int):
        super().__init__(type, sum_rum, area, price)
        self.location=location
        self.coondition=condition
    def get_price(self):
        return f"""
    {self.get_info()}
    """
    def set_price(self, newPrice:int):
        self.price=newPrice
    
    def __str__(self):
        return  super().get_info()    



f=Flat("toshkent", "the  beast", "Flat", 20, 133, 121200)
f.set_price(390)

g=Flat("Qo'qon", "The beast", "Flat", 25, 122, 2032)
g.set_price(900)

d=Flat("Fergana", "The beast", "Flat", 21, 2332, 2123)
d.set_price(400)

h=House("Andijon", "The beast", "House", 12, 42, 12)
h.set_price(200)

j=House("Navoiy", "Good", "House", 21, 32, 43)
j.set_price(123)
 
l=House("Jizzax", "Not Bad", "House", 21, 32, 43)
l.set_price(953)

flatlar=[f,g,d]
uylar=[l,j,h]

print(max(flatlar, key=lambda f: f.price))
print(max(uylar, key=lambda uy: uy.price))


        