class User:

    def __init__(self,user_name,user_pass):
        self.name=user_name
        self.__pss=user_pass
    def reset_pass(self):
        return self.__pss

user=User("Faysal","123sasd123")
print(user.reset_pass())
        
