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
    
    # If the time is on the pm meridiem and the duration time makes to pass to a new day
    if meridiem == "PM" and hour >= 12 and hour < 12:
        
        print("FRANJA PM Y HASTA 24 HORAS PARA NEXT DAY")
        # Return new time with or without day
        if day == None:
            new_time = f"{hour - 12}:{minutes} AM (next day)"
            return new_time
        else:
            pass

    # elif meridiem == "AM" and hour > 24 and hour < 36:
    #     print("TEST")
    
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

        if dayMeridiem <= 5:
            meridiem = "AM"
        else:
            meridiem = "PM"

    ########################################################### FOR LATER DELETION #####################################################    
    print(hour, minutes, meridiem, daysLater, dayMeridiem)
    ########################################################### FOR LATER DELETION #####################################################

    # Return the result for the same day
    if daysLater < 1:

        # Subtract 12 if the hour is greater than 12
        if hour > 12:
            hour = hour - 12

        # Return the new hour without the day and viceversa
        if day == None:
            new_time = f"{hour}:{minutes} {meridiem}"
        else:
            new_time = f"{hour}:{minutes} {meridiem}, {day}"
        
        return new_time

    # Return the result if the new time is in the next day
    if daysLater >= 1 and daysLater < 2:
        
        print("OPCION 2")
        
        # Subtract 24 if the hour is greater than 24 to get the am pm merediem
        hour = hour - 24
        print(hour)
        # Subtract 12 hours if the meridiem is pm
        if hour > 12:
            hour = hour - 12

        # Return the new hour without the day and viceversa
        if day == None:
            new_time = f"{hour}:{minutes} {meridiem} (next day)"
        else:
            new_time = f"{hour}:{minutes} {meridiem}, {day} (next day)"
        return new_time

    # Call the function to return the result if the new time is more than one day later
    if daysLater >= 2:
        print ("THIS")
    

print(add_time("00:00 AM", "03:00"))