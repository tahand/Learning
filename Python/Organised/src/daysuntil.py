from datetime import date, timedelta

today = date.today()

ls = [
    {"dateVal": date(2026, 1, 5), "description":"Next module"},
    {"dateVal": date(2025, 12, 25), "description":"Chrismas"},
    {"dateVal": date(2025, 11, 22), "description":"Jos birthday"},
    {"dateVal": date(2025, 12, 12), "description":"Mum and Katies birthday"},
    {"dateVal": date(2027, 10, 26), "description":"Move on"}
]

for item in ls:
    future_date = item["dateVal"]
    days_remaining = (future_date - today).days  # Subtract dates
    print(f"{item['description']} is in {days_remaining} days.")

