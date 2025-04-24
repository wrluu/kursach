import pytest
from src.services import profitable_categories, investment_bank, simple_search, search_phone_numbers, search_individual_transfers

@pytest.fixture
def sample_transactions():
    return [
        {"Дата операции": "2023-10-01 12:00:00", "Сумма операции": 100, "Категория": "Супермаркеты", "Описание": "Описание 1", "Номер карты": "1234"},
        {"Дата операции": "2023-10-02 12:00:00", "Сумма операции": 200, "Категория": "Кафе", "Описание": "Описание 2", "Номер карты": "5678"},
    ]

def test_profitable_categories(sample_transactions):
    result = profitable_categories(2023, 10, sample_transactions)
    assert "Супермаркеты" in result
    assert "Кафе" in result

def test_investment_bank(sample_transactions):
    result = investment_bank("2023-10", sample_transactions, 50)
    assert result == 300  # Пример значения

def test_simple_search(sample_transactions):
    result = simple_search("Описание 1", sample_transactions)
    assert len(result) == 1
    assert result[0]["Описание"] == "Описание 1"

def test_search_phone_numbers(sample_transactions):
    sample_transactions.append({"Дата операции": "2023-10-03 12:00:00", "Сумма операции": 300, "Категория": "Мобильные", "Описание": "Тинькофф Мобайл +7 995 555-55-55", "Номер карты": "9101"})
    result = search_phone_numbers(sample_transactions)
    assert len(result) == 1
    assert result[0]["Описание"] == "Тинькофф Мобайл +7 995 555-55-55"

def test_search_individual_transfers(sample_transactions):
    sample_transactions.append({"Дата операции": "2023-10-04 12:00:00", "Сумма операции": 400, "Категория": "Переводы", "Описание": "Валерий А.", "Номер карты": "1121"})
    result = search_individual_transfers(sample_transactions)
    assert len(result) == 1
    assert result[0]["Описание"] == "Валерий А."
