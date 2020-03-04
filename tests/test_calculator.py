from string_calculator.calculator import String_cal

add = String_cal()

def test_calculate_sum():
    assert add.calculate_sum("10","200") == 210