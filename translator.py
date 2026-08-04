number = int(input("Введите число от 1 до 5: "))

if number == 1:
    word = "One"
elif number == 2:
    word = "Two"
elif number == 3:
    word = "Three"
elif number == 4:
    word = "Four"
elif number == 5:
    word = "Five"
else:
    word = "Число должно быть от 1 до 5"

print("Соответствующее слово:", word)