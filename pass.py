correct_password = "qwerty123"

while True:
    user_password = input("Введите пароль: ")

    if user_password == correct_password:
        print("Пароль верный! Доступ разрешён.")
        break
    else:
        print("Неверный пароль. Попробуйте снова.")
