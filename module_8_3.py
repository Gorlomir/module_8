class IncorrectVinNumber(Exception):
    def __init__(self, message="Некорректный VIN номер"):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message="Некорректные номера автомобиля"):
        self.message = message


class Car:
    def __init__(self, model, vin_number, numbers):
        self.model = model
        self.__vin = vin_number
        self.__numbers = numbers

        self.__is_valid_vin(vin_number)
        self.__is_valid_numbers(numbers)

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Некорректный тип vin номер")
        if not 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber("Неверный диапазон для vin номера")

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        if len(numbers) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")

    def get_model(self):
        return self.model

    def get_vin(self):
        return self.__vin

    def get_numbers(self):
        return self.__numbers

    def __str__(self):
        return f"Car(model={self.model}, vin={self.__vin}, numbers={self.__numbers})"


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
