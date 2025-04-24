import pytest
import pandas as pd
from src.reports import spending_by_category, spending_by_weekday, spending_by_workday

@pytest.fixture
def sample_transactions():
    data = {
        "Дата операции": ["2023-10-01", "2023-10-02", "2023-10-03"],
        "Сумма платежа": [100, 200, 300],
        "Категория": ["Супермаркеты", "Кафе", "Супермаркеты"],
        "Описание": ["Описание 1", "Описание 2", "Описание 3"],
        "Номер карты": ["1234", "5678", "9101"],
    }
    return pd.DataFrame(data)

def test_spending_by_category(sample_transactions):
    result = spending_by_category(sample_transactions, "Супермаркеты")
    assert result["category"] == "Супермаркеты"
    assert result["total_spent"] == 400

def test_spending_by_weekday(sample_transactions):
    result = spending_by_weekday(sample_transactions)
    assert "Понедельник" in result
    assert "Вторник" in result

def test_spending_by_workday(sample_transactions):
    result = spending_by_workday(sample_transactions)
    assert "Рабочий день" in result
    assert "Выходной день" in result
