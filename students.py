students = [
    {"name": "Harry", "grades": [80, 90, 78]},
    {"name": "Hermione", "grades": [95, 90, 97]},
    {"name": "Ron", "grades": [60, 70, 64]},
    {"name": "Draco", "grades": [60, 75, 70]},
]


def calculate_average(grades):
    if not grades:
        return 0.0
    return sum(grades) / len(grades)


def calculate_overall_average(students_list):
    if not students_list:
        return 0.0

    total_sum = 0
    total_count = 0
    for student in students_list:
        total_sum += sum(student["grades"])
        total_count += len(student["grades"])

    return total_sum / total_count if total_count > 0 else 0.0


def analyze_students(students_list):
    print("--- АНАЛИЗ УСПЕВАЕМОСТИ СТУДЕНТОВ ---")

    for student in students_list:
        avg = calculate_average(student["grades"])
        status = "Успешен" if avg >= 75 else "Отстающий"

        print(f"Студент: {student['name']}")
        print(f"Средний балл: {avg:.2f}")
        print(f"Статус: {status}\n")

    overall_avg = calculate_overall_average(students_list)
    print(f"Общий средний балл по всем студентам: {overall_avg:.2f}")
    print("=" * 40 + "\n")


analyze_students(students)

new_student = {"name": "Neville", "grades": [70, 80, 85]}
students.append(new_student)
print(f"Добавлен новый студент: {new_student['name']}\n")

if students:
    lowest_student = min(
        students, key=lambda student: calculate_average(student["grades"])
    )
    students.remove(lowest_student)
    print(
        f"Удален студент с наименьшим средним баллом: {lowest_student['name']}\n"
    )

print("--- ОБНОВЛЕННЫЕ ДАННЫЕ ПОСЛЕ ИЗМЕНЕНИЙ ---")
analyze_students(students)
