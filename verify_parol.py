import random

parol = input("Введите ваш пароль : ")

try: 
    div = random.random()/len(parol) 
    t_num = int(parol) 
    print("Ваш пароль состоит только из цифр.")
except ZeroDivisionError: 
    print("Вы ввели пароль пустой.")
except: 
    print("Требования к паролю соблюдены.")