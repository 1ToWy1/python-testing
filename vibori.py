def check_voting_eligibility(age: int, citizen: bool, disqualified: bool) -> bool:
    return age >= 18 and citizen and not disqualified


def get_age_input() -> int:
    try:
        age = int(input("Введите ваш возраст: "))
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        return age
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
        exit()


def get_yes_no_input(prompt: str) -> bool:
    answer = input(prompt).strip().lower()
    return answer == "да"


def display_result(can_vote: bool) -> None:
    if can_vote:
        print("Вы можете голосовать!")
    else:
        print("Вы не можете голосовать.")


def main():
    age = get_age_input()
    citizen = get_yes_no_input("Вы гражданин страны? (да/нет): ")
    disqualified = get_yes_no_input("Вы дисквалифицированы? (да/нет): ")

    eligible = check_voting_eligibility(age, citizen, disqualified)
    display_result(eligible)


if __name__ == "__main__":
    main()
