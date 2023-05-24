def fix_short_time_of_day(time):
    time = str(time)
    if len(time) == 3:
        return '0' + time
    elif len(time) == 2:
        return '00' + time
    elif len(time) == 1:
        return '000' + time
    return time
