import re

def validate():
    while True:
        password = input("Введите ваш пароль: ")
        if len(password) < 8:
            print("Напишите 8 символов в вашем пароле")
        elif re.search('[0-9]',password) is None:
            print("Напишите хотя бы одну цфиру в вашем пароле")
        elif re.search('[A-Z]',password) is None: 
            print("Напишите хотя бы одну большую букву в вашем пароле")
        elif re.search('[a-z]',password) is None: 
            print("Напишите хотя бы одну маленькую букву в вашем пароле в вашем пароле")
        else:
            print("ваш пароль надёжный")
            break

validate()
    










	

