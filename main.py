import datetime
from application import salary
from application.db import people



def today_date():
    dt_now = datetime.datetime.now()
    print(dt_now)


if __name__ == '__main__':
    today_date()
    salary.calculate_salary()
    people.get_employees()



