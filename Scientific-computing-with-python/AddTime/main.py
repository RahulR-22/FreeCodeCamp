#
# author: Rahul R
#

days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


def add_time(start: str, duration: str, day: str = None):
    time = start[:-3]
    isAM = True if start[-2:] == "AM" else False
    start_time_hr, start_time_min = [int(x) for x in time.split(":")]
    add_time_hr, add_time_min = [int(x) for x in duration.split(":")]
    start_time_hr = start_time_hr if isAM else start_time_hr + 12
    day = day.lower() if day is not None else None
    new_time_min = start_time_min + add_time_min
    new_time_hr = (start_time_hr + add_time_hr) + (new_time_min // 60)
    new_time_min %= 60
    next_days = new_time_hr // 24
    print_time = ""
    new_time_hr %= 24
    if new_time_hr >= 12:
        new_time_hr %= 12
        if new_time_hr == 0:
            new_time_hr = 12
        print_time = "PM"
    elif new_time_hr == 0:
        new_time_hr = 12
        print_time = "AM"
    else:
        print_time = "AM"
    print_days = None
    if next_days == 1:
        print_days = "(next day)"
    elif next_days > 1:
        print_days = f"({next_days} days later)"
    if day is not None:
        ind = days.index(day)
        print_days_word = days[(ind + next_days) % 7]
        print_days_word = print_days_word.capitalize()
    if day is None:
        if print_days is None:
            return f"{new_time_hr}:{new_time_min:02} {print_time}"
        return f"{new_time_hr}:{new_time_min:02} {print_time} {print_days}"
    else:
        if print_days is None:
            return f"{new_time_hr}:{new_time_min:02} {print_time}, {print_days_word}"
        return f"{new_time_hr}:{new_time_min:02} {print_time}, {print_days_word} {print_days}"
