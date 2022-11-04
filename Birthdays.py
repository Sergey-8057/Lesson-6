from datetime import datetime
from calendar import monthrange


days_week =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

users = [{"name": "Mark", "birthday": datetime(year=1952, month=11, day=4)},
         {"name": "Jim", "birthday": datetime(year=1967, month=11, day=4)},
         {"name": "Piter", "birthday": datetime(year=1989, month=11, day=5)},
         {"name": "Maks", "birthday": datetime(year=1973, month=12, day=4)},
         {"name": "Ilon", "birthday": datetime(year=2001, month=11, day=6)},
         {"name": "Sergey", "birthday": datetime(year=1985, month=12, day=31)},
         {"name": "Nata", "birthday": datetime(year=1996, month=10, day=25)},
         {"name": "Karl", "birthday": datetime(year=1973, month=11, day=1)}]

def get_birthdays_per_week(users, days_week):
    current_date = datetime.now() 
    list_day = {}
    for user in users:
        user_date = user.get("birthday") 
        new_data = datetime(
            year=current_date.year,
            month=user.get('birthday').month,
            day=user.get('birthday').day
        )
        day = datetime.weekday(new_data)
        month = current_date.month
        days = monthrange(current_date.year, month)[1]
        name = user.setdefault("name")
        if user_date.month == current_date.month: #сравн мес рожд = текущ мес
            week = current_date.day + 7
            if user_date.day in range(current_date.day, week):
                if day < 5:
                    print_day = days_week[day]
                    if print_day in list_day:
                        val_name = list_day.get(print_day)
                        name = val_name + ', ' + name
                        list_day[print_day] = name
                    else:
                        list_day[print_day] = name
                else:
                    print_day = 'Monday'
                    if print_day in list_day:
                        val_name = list_day.get(print_day)
                        name = val_name + ', ' + name
                        list_day[print_day] = name
                    else:
                        list_day[print_day] = name
        end = current_date.day + 7 - days
        if end > 0:                         #если дни переходят в след месяц
            next_month = current_date.month + 1
            if user_date.month == next_month:
                if user_date.day in range(1, end):
                    if day < 5:
                        print_day = days_week[day]
                        if print_day in list_day:
                            val_name = list_day.get(print_day)
                            name = val_name + ', ' + name
                            list_day[print_day] = name
                        else:
                            list_day[print_day] = name
                    else:
                        print_day = 'Monday'
                        if print_day in list_day:
                            val_name = list_day.get(print_day)
                            name = val_name + ', ' + name
                            list_day[print_day] = name
                        else:
                            list_day[print_day] = name
        if current_date.month == 12 and end > 0:  #если 12 мес и дни переходят в след месяц
            next_month = 1    
            if user_date.month == next_month:
                if user_date.day in range(1, end):
                    if day < 5:
                        print_day = days_week[day]
                        if print_day in list_day:
                            val_name = list_day.get(print_day)
                            name = val_name + ', ' + name
                            list_day[print_day] = name
                        else:
                            list_day[print_day] = name
                    else:
                        print_day = 'Monday'
                        if print_day in list_day:
                            val_name = list_day.get(print_day)
                            name = val_name + ', ' + name
                            list_day[print_day] = name
                        else:
                            list_day[print_day] = name
    for key,value in list_day.items():
        result = key + ': ' + value
        print(result)
                

get_birthdays_per_week(users, days_week)
