import datetime
import handle_date

def advanceTime(IntDays):
    advanced_date = datetime.datetime.now() + datetime.timedelta(days=IntDays)
    advanced_date.date()
    return advanced_date
    
