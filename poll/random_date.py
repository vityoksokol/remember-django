import datetime
import random
import calendar


def random_date():
    year = random.randint(2000, 2019)
    month = random.randint(1, 13)
    day = random.randint(1, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)
