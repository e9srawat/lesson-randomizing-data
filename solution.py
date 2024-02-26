"""
Randomizing data
"""
from datetime import date, timedelta
import random


def create_assets(p, x):
    """
    Create random asset data
    """
    today = date.today()
    start = today - timedelta(days=x)
    dates = [start + timedelta(days=i) for i in range(x)]
    data = []
    for i in range(1, p + 1):
        data.append(
            {"id": i, "purchase_date": random.choice(dates)},
        )
    return data


def create_rentals(assets, q):
    """
    Create random rental data
    """
    today = date.today()
    rentals = []
    dates = {}
    id_count = 1
    while len(rentals) < q:
        asset = random.choice(assets)
        a_id = asset["id"]
        s_date = asset["purchase_date"]
        if a_id in dates:
            s_date = dates[a_id]
        if s_date > today:
            continue
        e_date = s_date + timedelta(days=random.randint(1,30))
        rentals.append(
            {"id": id_count, "asset_id": a_id, "start_date": s_date, "end_date": e_date}
        )
        dates[a_id] = e_date
        id_count += 1
    return rentals
