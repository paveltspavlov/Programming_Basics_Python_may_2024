hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())

buff_exam = (hour_of_exam * 60) + minutes_of_exam
buff_arriaval = (hour_of_arrival * 60) + minutes_of_arrival

if buff_arriaval > buff_exam:
    print("Late")
    buff_diff = buff_arriaval - buff_exam
    if buff_diff < 60:
        print(f"{buff_diff} minutes after the start")
    elif buff_diff >= 60:
        buff_hours = buff_diff // 60
        buff_minutes = buff_diff % 60
        print(f"{buff_hours}:{buff_minutes:02d} hours after the start")
elif buff_arriaval <= buff_exam:
    buff_diff = buff_exam - buff_arriaval
    if buff_diff <= 30:
        print("On time")
        if buff_diff > 0:
            print(f"{buff_diff} minutes before the start")
    else:
        print("Early")
        if buff_diff < 60:
            print(f"{buff_diff} minutes before the start")
        elif buff_diff >= 60:
            buff_hours = buff_diff // 60
            buff_minutes = buff_diff % 60
            print(f"{buff_hours}:{buff_minutes:02d} hours before the start")