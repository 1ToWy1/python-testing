def can_vote(age, citizen, disqualified):
    return age >= 18 and citizen and not disqualified


try:
    age = int(input("Введите ваш возраст: "))
except ValueError:
    print("Ошибка: возраст должен быть числом")
    exit()

citizen = input("Вы гражданин страны? (да/нет): ").lower() == "да"
disqualified = input("Вы дисквалифицированы? (да/нет): ").lower() == "да"

if can_vote(age, citizen, disqualified):
    print("Вы можете голосовать!")
else:
    print("Вы не можете голосовать.")
