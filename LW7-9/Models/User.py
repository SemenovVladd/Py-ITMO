
class User():
    def __init__(self, name: str, group: str, mail : str, phone: str):
        self.__name: str = name
        self.__group: str = group
        self.__mail: str = mail
        self.__phone: str = phone




    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name:str):
        if type (name) is str and len(name)>=2:
            self.__name==name
        else:
            raise ValueError('Ошибка при задании имени пользователя')


    @property
    def group(self):
        return self.__group
    @group.setter
    def group(self, group:str):
        if type (group) is str and len(group)>=3:
            self.__group==group
        else:
            raise ValueError('Ошибка при задании группы пользователя')

    @property
    def mail(self):
            return self.__mail
    @mail.setter
    def mail(self,mail:str):
        if type (mail) is str and len(mail)>=5:
            self.__mail = mail
        else:
            raise ValueError('Ошибка при задании почты пользователя')

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone:str):
        if type (phone) is str and len(phone)>=8:
            self.__phone==phone
        else:
            raise ValueError('Ошибка при задании номера пользователя')