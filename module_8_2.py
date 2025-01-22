def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for num in numbers:
        try:
            if isinstance(num, (int, float)):
                result += num
            else:
                raise TypeError(f"Некорректный тип данных: {type(num)}")
        except TypeError as exc:
            incorrect_data += 1
            print(f"Ошибка: {exc}")

    return result, incorrect_data


def calculate_average(numbers):
    try:
        if not isinstance(numbers, (list, tuple)):
            raise TypeError("numbers должен быть списком или кортежем")

        total_sum, incorrect_count = personal_sum(numbers)

        if incorrect_count > 0:
            print(f"Некорректный тип данных для подсчёта суммы - {' '.join(map(str, numbers))}")
            return 0

        if len(numbers) == 0:
            return 0

        average = total_sum / len(numbers)
        return average

    except ZeroDivisionError:
        print("Деление на ноль!")
        return 0

    except TypeError as exc:
        print(f"В numbers записан некорректный тип данных: {exc}")
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
