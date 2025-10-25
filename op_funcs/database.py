from datetime import datetime, timezone

import pandas as pd
from tinyflux import Point, TinyFlux

data = pd.read_csv("data/output.csv", usecols=["date", "price"])

db = TinyFlux("db.csv")


def df_to_points(data_frame: pd.DataFrame) -> list[Point]:
    """
    Convert a pandas DataFrame of dates and prices into a list of InfluxDB Point objects.
    Parameters
    ----------
    data_frame : pandas.DataFrame
        DataFrame where each row represents a datapoint. The function expects the first
        two columns (in order) to be: date and price. The date must be a string in
        the '%Y-%m-%d' format (e.g. '2023-01-31'); the price must be numeric or a string
        convertible to float.
    Returns
    -------
    list[Point]
        List of Point objects with:
          - measurement set to "uk oil prices"
          - time set to a timezone-aware UTC datetime parsed from the date string
          - fields containing a single key "price" with a float value
    Raises
    ------
    ValueError
        If a date string cannot be parsed using '%Y-%m-%d' or if a price cannot be
        converted to float.
    """

    data_tuple = list(data_frame.itertuples(index=False))

    point_list = []

    for tup in data_tuple:
        date_, price_ = tup

        date_format = datetime.strptime(date_, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        price_format = float(price_)

        point = Point(
            measurement="uk oil prices",
            time=date_format,
            fields={"price": price_format},
        )

        point_list.append(point)

    return point_list


point_list = df_to_points(data)

db.insert_multiple(point_list, compact_key_prefixes=False, batch_size=1000)
