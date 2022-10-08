import datetime
import pandas as pd


def advanceTime(IntDays):
    advanced_date = datetime.datetime.now() + datetime.timedelta(days=IntDays)
    advanced_date = advanced_date.date()
    # saving new date in csv
    advanced_date_save = pd.DataFrame(
        columns=[
            "date"
        ]
    )
    row = {"date": advanced_date}
    advanced_date_save = advanced_date_save.append(row, ignore_index=True)
    return advanced_date_save.to_csv("advanced_date_save.csv", index=False)
