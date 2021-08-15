
def add_time(start_time, duration, start_day=False):

    # WeekDays Lookup
    days_lst = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']
    days_dict = {days_lst[n].lower(): n for n in range(len(days_lst))}

    # Splitting start_time hours, minutes and AM/PM
    start_time_split = start_time.split()
    nums_start_time = start_time_split[0]
    hours_start_time = int(nums_start_time.split(':')[0])
    minutes_start_time = int(nums_start_time.split(':')[1])
    abb_start_time = start_time_split[1]

    # Stplitting duration HOURS - MINUTOS
    duration_split_lst = duration.split(":")
    hours_duration = int(duration_split_lst[0])
    minutes_duration = int(duration_split_lst[1])
    # Pasar star_time a 24hs format minutes_duration = duration_split(duration)

    if abb_start_time == 'PM':
        hours_start_time = hours_start_time+12

    # Sumar minutos
    minutes_end_time = minutes_start_time + minutes_duration

    # Sumar horas
    hours_end_time = hours_start_time + \
        hours_duration + int(minutes_end_time / 60)

    # Calcular cuantas veces pasamos la hora 24
    hours_forward = hours_end_time % 24
    days_forward = int(hours_end_time / 24)
    minutes_forward = minutes_end_time % 60

    if minutes_forward < 10:
        minutes_forward = '0' + str(minutes_forward)

    # Si vino el parametro r estart_day, calculand_day
    weekDayNum_end = -1
    if start_day is not False:
        weekDayNum_start = days_dict[start_day.lower()]
        weekDayNum_end = (weekDayNum_start+days_forward) % 7
        weekDayName = days_lst[weekDayNum_end]

    # Pasar a formato AM/PM
    if hours_forward > 12 and hours_forward < 24:
        hours_forward = hours_forward-12
        abb_end_time = 'PM'
    elif hours_forward == 12:
        abb_end_time = 'PM'
    elif hours_forward in (24, 0):
        hours_forward = 12
        abb_end_time = 'AM'
    else:
        abb_end_time = 'AM'

    result = f"{str(hours_forward)}:{minutes_forward} {abb_end_time}"
    if weekDayNum_end != -1:
        result += f", {weekDayName}"

    if days_forward > 1:
        result += f" ({days_forward} days later)"
    elif days_forward == 1:
        result += " (next day)"
    print(result)
    return result
