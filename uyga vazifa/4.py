class Employee:
    def __init__ (self, name:str, id:int, salary:int):
        self.name=name
        self.id=id
        self.salary=salary
    def display_info(self):
        return f"""
    id : {self.id}
    ism: {self.name}
    """
class Rahbar(Employee):
    def __init__(self, hourly_rate:int, hourly_worked:int, name:str, id:int):
        super().__init__(name, id, 0)
        self.hourly_rate=hourly_rate
        self.hourly_worked=hourly_worked
    def calculate_salary(self):
        self.salary=self.hourly_rate*self.hourly_worked
    def display_info(self):
        return f"""
    {super().display_info()}rahbar uchun maosh: {self.salary}
    """
class Boshqaruvchi(Employee):
    def __init__(self, hourly_rate:int, hourly_worked:int, name:str, id:int):
        super().__init__(name, id, 0)
        self.hourly_rate=hourly_rate
        self.hourly_worked=hourly_worked
    def calculate_salary(self):
        self.salary=self.hourly_rate*self.hourly_worked
    def display_info(self):
        return f"""
    {super().display_info()}Boshqaruvchi uchun maosh: {self.salary}
    """




A=Rahbar(20,5,"salom",23212)
A.calculate_salary()
print(A.display_info())

B=Boshqaruvchi(20,30,"hayr",32343)
B.calculate_salary()
print(B.display_info())