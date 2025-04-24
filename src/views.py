
from datetime import datetime
from src.utils import get_currency_rates, get_stock_prices


def homepage(current_time, transactions):
    return {
        "greeting": "Добро пожаловать!",
        "cards": list(transactions["Номер карты"].unique()) if "Номер карты" in transactions else [],
        "top_transactions": transactions.sort_values(by="Сумма платежа", ascending=False).head(3).to_dict("records")
        if "Сумма платежа" in transactions else [],
        "currency_rates": get_currency_rates(["USD", "EUR"]),
        "stock_prices": get_stock_prices(["AAPL", "GOOGL"]),
    }


def events(date_str, transactions):
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return {}

    filtered = transactions.copy()
    filtered["Дата операции"] = pd.to_datetime(filtered["Дата операции"], errors="coerce")
    filtered = filtered[filtered["Дата операции"].dt.date == date_obj.date()]

    expenses = filtered[filtered["Сумма платежа"] < 0].to_dict("records")
    income = filtered[filtered["Сумма платежа"] > 0].to_dict("records")

    return {
        "expenses": expenses,
        "income": income,
        "currency_rates": get_currency_rates(["USD", "EUR"]),
        "stock_prices": get_stock_prices(["AAPL", "GOOGL"]),
    }
