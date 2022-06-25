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
    # Variable to calculate AM or PM in TwoOrMoreDays()
    hourstart = int(hourstart[0])

    # Do the addition of time and minutes
    # This also calculates when the new hour is the am on the same day
    hour = hour + hourduration
    minutes = minutes + minuteduration

    # Variable to calculate the number of days later after the time
    # It uses the round method to determine the am pm meridien.
    daysLater = round((hour / 24), 2)

    # If the minutes addition is greater than 59, it adds one hour to hour and calculate the remainig 
    # minutes to display the correct hour and minutes
    if minutes > 59:
        minutes = 0 + (minutes - 60)
        hour = hour + 1

    # Format the minutes to add a 0 before the number if the minutes variable is <= 9
    if len(str(minutes)) < 2:
        minutes = f"0{minutes}"
    
    # Determines the meridiem for the same day and up to the next day. 48 hours maximum
    if meridiem == "PM" and hour > 12 and hour < 24: # Necesary if the start variable is > 12 and meridiem is PM
        hour = hour - 12
        meridiem = "AM"
        new_time = NextDay(hour, minutes, meridiem, day, daysLater)
        return new_time
    if meridiem == "PM" and hour < 12: # Necesary if the start variable is < 12 and meridiem is PM
        hour = hour + 12
        meridiem = "PM"
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
                meridiem = "AM"
            else:
                meridiem = "PM"
 
    # Return the result for the same day
    if daysLater < 1:
        new_time = SameDay(hour, minutes, meridiem, day)
        return new_time

    # Return the result when the meridiem is PM and the second or more days start after 35.59 hours
    if meridiem == "PM" and hour >= 12 and hour < 24:
        meridiem = "AM"
        daysLater = str(daysLater)
        daysLater = daysLater.split(".")
        daysLater = int(daysLater[0])
        daysLater = daysLater + 1
        new_time = TwoOrMoreDays(dayMeridiem, minutes, meridiem, day, daysLater, hourstart, hourduration)
        return new_time

    if meridiem == "PM" and hour >= 24 and hour < 36:
        meridiem = "PM"
        new_time = TwoOrMoreDays(dayMeridiem, minutes, meridiem, day, daysLater, hourstart, hourduration)
        return new_time

    # Return the result if the new time is in the next day
    if daysLater >= 1 and daysLater < 2:
        new_time = NextDay(hour, minutes, meridiem, day, daysLater)
        return new_time
    
    # It is necesary to add 1 to daysLater to get the correct count of days that
    # includes the day in progress. Only necesary for two or more days ahead
    daysLater = daysLater + 1

    # Call the function to return the result if the new time is more than one day later
    if daysLater >= 2:
        new_time = TwoOrMoreDays(dayMeridiem, minutes, meridiem, day, daysLater, hourstart, hourduration)
        return new_time


def SameDay(hour, minutes, meridiem, day):
    # Return the new hour without the day and viceversa
    if day == None:
        new_time = f"{hour}:{minutes} {meridiem}"
    else:
        new_time = f"{hour}:{minutes} {meridiem}, {day}"

    return new_time


def NextDay(hour, minutes, meridiem, day, daysLater):
    # Return the new hour without the day and viceversa
    if day == None:
        new_time = f"{hour}:{minutes} {meridiem} (next day)"
    else:
        newDay = DaysOfTheWeek(day, daysLater)
        new_time = f"{hour}:{minutes} {meridiem}, {newDay} (next day)"
    return new_time


def TwoOrMoreDays(dayMeridiem, minutes, meridiem, day, daysLater, hourstart, hourduration):
    # Calculate the hour in the future
    hourToCalculate = hourduration % 24
    newHour = hourToCalculate + hourstart - 12
    
    # Used to convert the hour when the result is < 0. That means that the meridiem is in the AM frame
    if newHour <= 0:
        # + 13 Necesary to include the hour 0, or the newHour will be - 1 hour instead of the real hour
        newHour = newHour + 13
    if newHour >= 12:
        newHour = newHour - 13
    
    # Determine the meridiem
    # If not, turn dayMeridiem into an integer and determine if the meridiem is am or pm by turning dayMeridiem
    # into an integer, and if the result is less than 5 then the meridiem is am and viceversa. Also determines
    # the meridiem when the time is PM
    if meridiem == "PM" and dayMeridiem >= 50:
        meridiem = "AM"
    elif meridiem == "PM" and dayMeridiem < 50:
        meridiem = "PM"
    elif dayMeridiem <= 1:
        meridiem = "AM"
    elif dayMeridiem < 50:
        meridiem = "AM"
    else:
        meridiem = "PM"

    # Get only the int number for daysLater to calculate the index to search
    daysLater = str(daysLater)
    daysLater = daysLater.split(".")
    daysLater = int(daysLater[0])

    # Return the new hour without the day and viceversa
    if day == None:
        new_time = f"{newHour}:{minutes} {meridiem} ({daysLater} days later)"
    else:
        newDay = DaysOfTheWeek(day, daysLater)
        new_time = f"{newHour}:{minutes} {meridiem}, {newDay} ({daysLater} days later)"

    return new_time


# Returns the correct day
def DaysOfTheWeek(day, daysLater):
    # Convert the day into camelcase when the new time is one day or more later
    day = day.title()
    # Get only the int number for daysLater to calculate the index to search
    daysLater = str(daysLater)
    daysLater = daysLater.split(".")
    daysLater = int(daysLater[0])
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    # Index for the present day
    dayIndex = week.index(day)
    # Variable to determine if the next time is a Monday.
    mondays = (daysLater + dayIndex) % 7
    
    # When the next time is in the same week
    if (dayIndex + daysLater) < 7:
        day = week[dayIndex + daysLater]
    # When the next time is exactly a Monday
    elif mondays == 0:
        day = week[0]
    # When the next time is greater than 7 days and it is a day different from Monday
    else:
        daysModulo = (daysLater + dayIndex) % 7
        day = week[daysModulo]
        
    return day


# print(add_time("3:30 PM", "2:12")) # expected = "5:42 PM"
# print(add_time("11:55 AM", "3:12")) # expected = "3:07 PM"
# print(add_time("9:15 PM", "5:30")) # expected = "2:45 AM (next day)"
# print(add_time("11:40 AM", "0:25")) # expected = "12:05 PM"
# print(add_time("2:59 AM", "24:00")) # expected = "2:59 AM (next day)"
# print(add_time("11:59 PM", "24:05")) # expected = "12:04 AM (2 days later)"  ##########################################
# print(add_time("8:16 PM", "466:02"))  # expected = "6:18 AM (20 days later)" 
# print(add_time("5:01 AM", "0:00")) # expected = "5:01 AM"
# print(add_time("3:30 PM", "2:12", "Monday")) # expected = "5:42 PM, Monday"
# print(add_time("2:59 AM", "24:00", "saturDay")) # expected = "2:59 AM, Sunday (next day)"
print(add_time("11:59 PM", "24:05", "Wednesday")) # expected = "12:04 AM, Friday (2 days later)" ####################################
# print(add_time("9:16 PM", "466:02", "tuesday")) # expected = "7:18 AM, Monday (20 days later)"


# print(add_time("0:00 AM", "49:02"))