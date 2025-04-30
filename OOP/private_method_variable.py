class User:
    __name="anonymus"

    def __see_name(self):
        return self.__name
    def see_function(self):
        return self.__see_name()
    

user=User()
print(user.see_function())
        
