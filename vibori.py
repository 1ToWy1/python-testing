def check_voting_eligibility(age: int, citizen: bool, disqualified: bool) -> bool:
    return age >= 18 and citizen and not disqualified


def get_yes_no_input(prompt: str) -> bool:
    return input(prompt).strip().lower() == "да"


def main():
    try:
        age = int(input("Введите ваш возраст: "))
        if age < 0:
            print("Ошибка ввода: возраст не может быть отрицательным.")
            return
    except ValueError:
        print("Ошибка ввода: возраст должен быть числом.")
        return

    citizen = get_yes_no_input("Вы гражданин страны? (да/нет): ")
    disqualified = get_yes_no_input("Вы дисквалифицированы? (да/нет): ")

    if check_voting_eligibility(age, citizen, disqualified):
        print("Вы можете голосовать!")
    else:
        print("Вы не можете голосовать.")


if __name__ == "__main__":
    main()
