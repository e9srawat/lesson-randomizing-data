"""
Randomizing data
"""
from datetime import datetime, timedelta
import random


def create_assets(p, x):
    """
    Create random asset data
    """
    today = datetime.today()
    start = today - timedelta(days=x)
    data = []
    for i in range(1, p + 1):
        year = random.choice(range(start.date().year, today.date().year + 1))
        if year == today.date().year:
            day = random.choice(range(1, today.date().day + 1))
            month = random.choice(range(1, today.date().month + 1))
        elif year == today.date().year:
            day = random.choice(range(1, 29))
            month = random.choice(range(start.date().month, 13))
        else:
            day = random.choice(range(1, 29))
            month = random.choice(range(1, 13))

        data.append(
            {"id": i, "purchase_date": datetime(year, month, day).date()},
        )
    return data


def create_rentals(assets, q):
    """
    Create random rental data
    """
    rentals = []
    dates = {}
    for i in range(1, q + 1):
        asset = random.choice(assets)
        a_id = asset["id"]
        s_date = asset["purchase_date"]
        if a_id in dates:
            s_date = datetime(
                dates[a_id].year, dates[a_id].month, dates[a_id].day
            ).date()
        if s_date.month < 12:
            e_date = datetime(s_date.year, s_date.month + 1, s_date.day).date()
        else:
            e_date = datetime(s_date.year+1, 1, s_date.day).date()
        rentals.append(
            {"id": i, "asset_id": a_id, "start_date": s_date, "end_date": e_date}
        )
        dates[a_id] = e_date
    return rentals
