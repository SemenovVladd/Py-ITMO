#from Currency import get_currencies
def User_cur(user_val, val):
    u_v=[]
    u_v.append(user_val.split(','))
    #создаем массив и записываем в него названия валют пользователя
    valut_u=[]
    #итоговый массив для хронения названий валют пользователя
    # и их значений
    for i in range(len(u_v[0])):
        valut_u.append((u_v[0][i], val[u_v[0][i]]))
        #проходимся по всем названиям валют пользователя
        # и записываем в итоговый массив название валюты и её значение
    return valut_u
#d=get_currencies()
#print(User_cur('USD,AUD,DZD',d))