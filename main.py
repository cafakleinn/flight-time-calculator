verify_departing_city = 'N'
verify_departing_time = 'N'

print("Welcome to the Flight Time Calculator. ")

# Departing City
while verify_departing_city != 'Y' or verify_departing_city != 'y':
    departing_city = input("Please enter the departing city you are flying from: ")
    verify_departing_city = input(f"The departing city you inputted is {departing_city}. Is this correct? (Y/N) ")
    
    if verify_departing_city == 'Y' or verify_departing_city == 'y':
        break

# Departure Time
while (verify_departing_time != 'Y' or verify_departing_time != 'y'):
    departure_time = input("Please enter the departure time: ")
    verify_departing_time = input(f"The departure time you inputted is {departure_time}. Is this correct? (Y/N) ")

    if verify_departing_time == 'Y' or verify_departing_time == 'y':
        break

