import pytest


class TestInt:

    def test_type_after_division(self):
        """Проверка возвращаемого типа данных при делении целых чисел

        Данные: number_one = 10, number_two = 5

        Ожидаемый результат: type float
        """
        number_one = 10
        number_two = 5
        division_result = number_one / number_two

        assert isinstance(division_result,
                          float), f"Похоже разраб своим фиксом испортил нам все тесты {type(division_result)} не float((("

    def test_bit_left_step(self):
        """Проверка работы оператора '<<' над целым числом

        Данные: целое число = 5, сдвиг = 8

        Ожидаемый результат:
        """
        number = 5
        step = 8
        result = number << step
        expected_result = 1280

        assert result == expected_result, f"битовый оператор '<<' отрабатывает с ошибкой," \
                                          f" результат {result} отличен от ожидаемого {expected_result}"


class TestDict:

    @pytest.mark.parametrize(
        ("key", "expected_result"),
        [(1, {1: "Hello VK"}), ("_", {"_": "Hello VK"}), (("тупля",), {("тупля",): "Hello VK"})],
        ids=["int", "str", "tuple"]
    )
    def test_values_for_key(self, key, expected_result):
        """ Проверка: может ли быть тип данных использован в качестве ключа словаря
        """
        result = {key: "Hello VK"}

        assert result == expected_result

    # негативный тест
    def test_addition(self):
        """ Проверка работы оператора '+' над словарями

        Данные: словарь1 {"name": "Alice"}, словарь2 {"surname": "Brown"}

        Ожидаемый результат: Ошибка TypeError
        """

        first_dict = {"name": "Alice"}
        second_dict = {"surname": "Brown"}

        try:
            first_dict - second_dict
        except TypeError:
            pass


class TestSet:

    def test_set_discard(self):
        """Проверка работы метода discard

        Данные: множество = {1, 2, 3, 4, 5}, удаляемое значение = 5

        Ожидаемый результат: множество = (1, 2, 3, 4)
        """

        test_set = {1, 2, 3, 4, 5}
        test_set.discard(5)
        expected_result = {1, 2, 3, 4}

        assert test_set == expected_result, f"{test_set} не равен {expected_result}"

    def test_intersection(self):
        """Проверка пересечения множеств путем использования оператора &

        Данные: множество1 = {1, 2}, множество2 = {100, 1}

        Ожидаемый результат: {1}
        """

        first_set = {1, 2}
        second_set = {100, 1}
        result = first_set & second_set
        expected_result = {1}

        assert result == expected_result, f"ОШИБКА!!!!342425!!! ПИЛИМ БАГ РЕПОРТ )))) " \
                                          f"ожидаемый результат:{expected_result} не равен текущему {second_set}"
