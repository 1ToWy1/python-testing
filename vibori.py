def can_vote(age, citi, disqualification):
    return age >= 18 and citi and not disqualification


age = int(input("Введите ваш возраст: "))
citizen = input("Вы гражданин страны? (да/нет): ").lower() == "да"
disqualified = input("Вы дисквалифицированы? (да/нет): ").lower() == "да"

if can_vote(age, citizen, disqualified):
    print("Вы можете голосовать!")
else:
    print("Вы не можете голосовать.")
