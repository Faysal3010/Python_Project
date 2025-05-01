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


car1=ToyotaCar("Tesla")
car2=ToyotaCar("GLS")

print(car1.start())
print(car2.stop())
