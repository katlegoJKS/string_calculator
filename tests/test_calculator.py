from string_calculator.calculator import add

def test_add_empty_str():
    assert add("") == 0
    
def test_add_one_number():
    assert add("1") == 1
    assert add("11") == 11
    assert add("111") == 111

def test_adding_two_numbers():
    assert add("1,1") == 2

def test_adding_multiple_numbers():
    assert add("1,1,1") == 3
    assert add("1,1,1,1") == 4
    assert add("1,2,3,4") == 10

def test_adding_new_line_between_integers():
    assert add("1\n2,3") == 6
    assert add("1,2\n3") == 6
    assert add("1\n2\n3") == 6

def test_adding_mixed_numbers_within_delimiters():
    assert add("//;\n1;2") == 3

def test_handling_different_delimiters():
    assert add("//;\n1;2") == 3
    assert add("//4\n142") == 3

def test_handling_negative_numbers():
    with pytest.raises(Exception) as err:
        assert add("//;\n-1;2,-3")
        assert str(err.value) == "Negatives not allowed: -1,-3,"

# def test_more_than_twenty():
#     assert add("//;\n1;2,21") == 3

# def test_delimeter_len():
#     assert add("//[***]\n1***2***3") == 6