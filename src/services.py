
from typing import List, Dict, Any
import pandas as pd


def get_profitable_cashback_categories(transactions: List[Dict[str, Any]], year: int, month: int) -> Dict[str, float]:
    """
    Анализирует выгодность категорий повышенного кешбэка.
    """
    df = pd.DataFrame(transactions)
    if df.empty or "Дата операции" not in df.columns:
        return {}

    df["Дата операции"] = pd.to_datetime(df["Дата операции"], errors="coerce")
    df = df[df["Дата операции"].notna()]
    filtered_df = df[(df["Дата операции"].dt.year == year) & (df["Дата операции"].dt.month == month)]

    category_cashback = {}
    for category, group in filtered_df.groupby("Категория"):
        total_spent = group["Сумма платежа"].sum()
        cashback = total_spent * 0.01  # 1% кешбэк
        category_cashback[category] = cashback

    return category_cashback
