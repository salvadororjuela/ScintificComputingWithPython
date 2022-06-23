def add_time(start, duration, day=None):
    # Split the components of the start and duration time.
    start = start.split()
    duration = duration.split(":")
    # Split the hours, minutes, and meridiem of start and duration times to store them into variables
    hourstart = start[0].split(":")
    hour = int(hourstart[0])
    minutes = int(hourstart[1])
    meridiem = start[1]
    hourduration = int(duration[0])
    minuteduration = int(duration[1])

    # Do the addition of time and minutes
    # This also calculates when the new hour is the am on the same day
    hour = hour + hourduration
    minutes = minutes + minuteduration

    # If the minutes addition is greater than 59, it adds one hour to hour and calculate the remainig 
    # minutes to display the correct hour and minutes
    if minutes > 59:
        minutes = 0 + (minutes - 60)
        hour = hour + 1

    # Format the minutes to add a 0 before the number if the minutes variable is <= 9
    if len(str(minutes)) < 2:
        minutes = f"0{minutes}"
    
    # Determines the meridiem for the same day and up to the next day. 48 hours maximum
    if hour < 12 or hour >= 24 and hour < 36:
        meridiem = "AM"
    if hour >= 12 and hour < 24 or hour >= 36 and hour < 48:
        meridiem = "PM"
    
    # Subtract the number of hours if hours to get the meridiem AM or PM up to the next day.
    if hour > 12 and hour < 24:
        hour = hour - 12
    if hour >= 24 and hour <= 36:
        hour = hour - 24
    if hour > 36 and hour < 48:
        hour = hour -36
    # Determine the meridiem when the new time of two or more days ahead.
    if hour >= 48:
        # Variable to calculate the number of days later after the time
        # It uses the round method to determine the am pm meridien.
        daysLater = round((hour / 24), 2)
        # Calculate when the new hour is in am or in pm.
        dayMeridiem = str(daysLater)
        dayMeridiem = dayMeridiem.split(".")

        # Evaluate if dayMeridiam is starts with a 0 as a string. If so, the meridiem is am
        if dayMeridiem[1].startswith("0"):
            meridiem = "AM"
        # If not, turn dayMeridiem into an integer and determine if the meridiem is am or pm by turning dayMeridiem
        # into an integer, and if the result is less than 5 then the meridiem is am and viceversa
        else:
            dayMeridiem = int(dayMeridiem[1])

            if dayMeridiem < 50:
                meridiem = "MANANA"
            else:
                meridiem = "TARDE"
    
    new_time = f"{hour}:{minutes} {meridiem}, {day}, Days Later: {daysLater}, dayMeridiem: {dayMeridiem}"
    return new_time
    # Calculate when the new hour is in am or in pm.
    
print(add_time("00:00 AM", "466:00", "TUESDAY"))