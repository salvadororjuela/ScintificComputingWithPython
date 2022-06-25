# Returns the correct day
def DaysOfTheWeek(day, daysLater):
    day = day.title()
    daysLater = str(daysLater)
    daysLater = daysLater.split(".")
    daysLater = int(daysLater[0])
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    dayIndex = week.index(day)
    # Variable to determine if the next time is a monday.
    mondays = (daysLater + dayIndex) % 7
    
    if (dayIndex + daysLater) < 7:
        day = week[dayIndex + daysLater]
    elif mondays == 0:
        day = week[0]
        print("'%' aplicado")
    else:
        daysModulo = (daysLater + dayIndex) % 7
        day = week[daysModulo]
        print(day)
        print(f"daysLater = {daysLater}, dayIndex = {dayIndex}, daysModulo = {daysModulo}")
        print(week.index(day))

    return day

print(DaysOfTheWeek("tuesday", 20))