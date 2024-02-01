class Vehicle:
    def __init__(self, type:str, model:str):
        self.type=type
        self.model=model
    def diplay_info(self):
        return f"""
    tip : {self.type}
    model : {self.model}
    """
class Car (Vehicle):
    def __init__ (self, type:str, model:str):
        super().__init__(type, model) 
    def display_info(self):
        return f"""
        {super().diplay_info()}num vehicle : 4
    num doors   : 4
        """
class Helicopter (Vehicle):
    def __init__ (self, type:str, model:str):
        super().__init__(type, model) 
    def display_info(self):
        return f"""
        {super().diplay_info()}num vehicle : 4
    num doors   : 4
        """
class Motorsikl (Vehicle):
    def __init__ (self, type:str, model:str):
        super().__init__(type, model) 
    def display_info(self):
        return f"""
        {super().diplay_info()}num vehicle : 2
    num doors   : 0
        """
class Plane (Vehicle):
    def __init__ (self, type:str, model:str):
        super().__init__(type, model) 
    def display_info(self):
        return f"""
        {super().diplay_info()}num vehicle : 8
    num doors   : 6
        """
moshina=Car("car", "Bugatti")
print(moshina.display_info())
helikopter=Helicopter("vertalyot", "Black Shark")
print(helikopter.display_info())
plane=Plane("samalyot", "F 32")
print(plane.display_info())
motorsikl=Motorsikl("motorsikl", "Yamaha")
print(motorsikl.display_info())