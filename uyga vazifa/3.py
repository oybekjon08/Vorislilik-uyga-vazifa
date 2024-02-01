class Shaxs:
    def __init__(self, ism:str, familiya:str, yosh:int, oylik_daromad:int):
        self.ism=ism
        self.familiya=familiya
        self.yosh=yosh
        self.maosh=oylik_daromad
    def info(self):
        return f"""
    ism : {self.ism}
    familiya : {self.familiya}
    yosh :     {self.yosh}
    oylik maosh: {self.maosh}
    """

class Talaba(Shaxs):
    def __init__ (self, ism:str, familiya:str, yosh:int, oylik_daromad:int, soliq:int):
        super().__init__(ism, familiya, yosh, oylik_daromad)
        self.daromad=0
        self.soliq=soliq
    
    def set_daromad(self):
        self.daromad=self.maosh-self.soliq
    
    def get_daromad(self):
        return self.daromad
    
    def get_more_info(self):
        return f"""
    {super().info()}To'liq daromad : {self.daromad}
    """

class Pensioner(Shaxs):
    def __init__ (self, ism:str, familiya:str, yosh:int, oylik_daromad:int, soliq:int):
        super().__init__(ism, familiya, yosh, oylik_daromad)
        self.daromad=0
        self.soliq=soliq
    
    def set_daromad(self):
        self.daromad=self.maosh-self.soliq
    
    def get_daromad(self):
        return self.daromad
    
    def get_more_info(self):
        return f"""
    {super().info()}To'liq daromad : {self.daromad}
    """

class Ishchi(Shaxs):
    def __init__ (self, ism:str, familiya:str, yosh:int, oylik_daromad:int, soliq:int):
        super().__init__(ism, familiya, yosh, oylik_daromad)
        self.daromad=0
        self.soliq=soliq
    
    def set_daromad(self):
        self.daromad=self.maosh-self.soliq
    
    def get_daromad(self):
        return self.daromad
    
    def get_more_info(self):
        return f"""
    {super().info()}To'liq daromad : {self.daromad}
    """

A=Talaba("eshmat", "toshmatov", 23, 300, 20)
A.set_daromad()
print(A.get_more_info())

B=Talaba("toshmat", "eshmatov", 24, 320, 20)
B.set_daromad()
print(B.get_more_info())

C=Pensioner("Tolaboy", "Mirzayev", 65, 0,5)
C.set_daromad()
print(C.get_more_info())


V=Pensioner("alomat", "Qovunov", 76, 20,2)
V.set_daromad()
print(V.get_more_info())

G=Ishchi("Tolaboy", "Mirzayev", 40, 1000,20)
G.set_daromad()
print(G.get_more_info())


H=Ishchi("Anorboy", "Tarbuzov", 40, 1000,20)
H.set_daromad()
print(H.get_more_info())
