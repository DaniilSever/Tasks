from main import all_divisors

set_values = [23436, 190187200, 380457890232]


def test_all_divisors_return_list():
    for value in set_values:
        assert all_divisors(value) == list


def test_all_divisors_correct_division_first_number():
    divisors_list = all_divisors(set_values[0])
    for value in divisors_list:
        assert set_values % value == 0


def test_all_divisors_correct_division_second_number():
    divisors_list = all_divisors(set_values[1])
    for value in divisors_list:
        assert set_values % value == 0


def test_all_divisors_correct_division_third_number():
    divisors_list = all_divisors(set_values[2])
    for value in divisors_list:
        assert set_values % value == 0
