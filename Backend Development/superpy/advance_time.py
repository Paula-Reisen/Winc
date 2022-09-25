import datetime
import handle_date

def advanceTime(IntDays):
    advanced_date = datetime.datetime.now() + datetime.timedelta(days=IntDays)
    advanced_date.date()
    #handle_date.handle_date(advanced_date)
    return advanced_date
    
