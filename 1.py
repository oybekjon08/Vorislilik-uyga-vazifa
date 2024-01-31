class Texnika:
    def __init__ (self, brand:str, model:str, tip:str):
        self.brand=brand
        self.model=model
        self.tip=tip
    def info(self):
        return f"""
    brand : {self.brand}
    model : {self.model}
    tip   : {self.tip}
    """
        
class Notebooks (Texnika):
    def __init__ (self, brand:str, model:str, tip:str, vidio_card:str, display:str, ram:int):
        super().__init__(brand, model, tip)
        self.vidio_card=vidio_card
        self.display=display
        self.ram=ram
    def __str__(self):
        return f"""
    {super().info()}vidio carta : {self.vidio_card}
    display     : {self.display}
    ram :       : {self.ram}    
    """

class Televisions (Texnika):
    def __init__(self,brand:str, model:str, tip:str, display:str, size:int):
        super().__init__(brand, model, tip)
        self.display=display
        self.size=size
    def __str__(self):
        return f"""
    {super().info()}display     : {self.display}
    size        : {self.size}    
    """
    
class Smartphones (Texnika):
    def __init__ (self, brand:str, model:str, tip:str, size:int, sim_count:int):
        super().__init__(brand, model, tip)
        self.size=size
        self.sim_count=sim_count
    def __str__(self):
        return f"""
    {super().info()}size:{self.size}
    sim_coount={self.sim_count}
    
    """


a=Notebooks("hp", "victus", "notebook", "rtx 4090", "oled", 1080)
b=Televisions("Samsung", "G'v.1896", "Televizor", "Q-led", 1080)
s=Smartphones("Iphone", "18 pro max", "smartphone", 10, 2)

print(a)
print(b)
print(s)