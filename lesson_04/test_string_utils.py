import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст Пример: `capitilize("skypro") -> "Skypro"
@pytest.mark.positive
@pytest.mark.parametrize("input_str, out_str", [
    ("lesson", "Lesson"),
    ("culture park", "Culture park"),
    ("04 апреля 2023", "04 апреля 2023")
])
def test_capitalize_positive(input_str, out_str):
    assert string_utils.capitalize(input_str) == out_str

@pytest.mark.negative
@pytest.mark.parametrize("input_str, out_str", [
    ("", ""),
    ("123hello", "123hello")
])
def test_capitalize_negative(input_str, out_str):
    assert string_utils.capitalize(input_str) == out_str

@pytest.mark.negative
def test_capitalize_not_str():
    with pytest.raises(AttributeError):
        string_utils.capitalize(123)


# Принимает на вход текст и удаляет пробелы в начале, если они есть Пример: `trim("   skypro") -> "skypro"
@pytest.mark.positive
@pytest.mark.parametrize("input_str, out_str", [
    ("  lesson", "lesson"),
    (" culture park", "culture park"),
    ("   123   ", "123   ")
])
def test_trim_positive(input_str, out_str):
    assert string_utils.trim(input_str) == out_str

@pytest.mark.negative
@pytest.mark.parametrize("input_str, out_str", [
    ("", ""),
    ("   ", "")
])
def test_trim_negative(input_str, out_str):
    assert string_utils.trim(input_str) == out_str

@pytest.mark.negative
def test_trim_not_str():
    with pytest.raises(AttributeError):
        string_utils.trim(123)


# Возвращает `True`, если строка содержит искомый символ и
# `False` - если нет Параметры: `string` - строка для обработки, `symbol` - искомый символ
# Пример 1: `contains("SkyPro", "S") -> True, Пример 2: `contains("SkyPro", "U") -> False
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, out_bool", [
    ("SkyPro", "k", True),
    ("SkyPro", "Sky", True),
    ("SkyPro", "Pro", True),
    ("123", "2", True)
])
def test_contains_positive(input_str, symbol, out_bool):
    assert string_utils.contains(input_str, symbol) == out_bool

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, out_bool", [
    ("", "P", False),
    ("SkyPro", "U", False),
    ("SkyPro", "sky", False)
])
def test_contains_negative(input_str, symbol, out_bool):
    assert string_utils.contains(input_str, symbol) == out_bool

@pytest.mark.negative
def test_contains_not_str():
    with pytest.raises(TypeError):
        string_utils.contains("apple", None)


# Удаляет все подстроки из переданной строки
# Параметры: `string` - строка для обработки, `symbol` - искомый символ для удаления.
# Пример 1: `delete_symbol("SkyPro", "k") -> "SyPro", Пример 2: `delete_symbol("SkyPro", "Pro") -> "Sky"`
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, out_str", [
    ("Python", "t", "Pyhon"),
    ("Яблоко", "Я", "блоко"),
    ("Sky@Pro", "@", "SkyPro")
])
def test_delete_symbol_positive(input_str, symbol, out_str):
    assert string_utils.delete_symbol(input_str, symbol) == out_str

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, out_str", [
    ("   ", "o", "   "),
    ("", "a", "")
])
def test_delete_symbol_negative(input_str, symbol, out_str):
    assert string_utils.delete_symbol(input_str, symbol) == out_str

@pytest.mark.negative
def test_delete_symbol_symbol_not_str():
    with pytest.raises(TypeError):
        string_utils.delete_symbol("Python", 1)