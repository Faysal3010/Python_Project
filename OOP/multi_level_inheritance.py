class Car:
    @staticmethod
    def start():
        return "Car started.."
    @staticmethod
    def stop():
        return "Car stopped.."

    
class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name 

class Model(ToyotaCar):
    def __init__(self, model):
        self.model=model
car1=Model("Prado")
car2=Model("Cround")

print(car1.start())
print(car2.stop())
