verify_departing_city = 'N'

print("Welcome to the Flight Time Calculator. ")

while verify_departing_city != 'Y' or verify_departing_city != 'y':
    departing_city = input("Please enter the departing city you are flying from: ")
    verify_departing_city = input(f"The departing city you inputted is {departing_city}. Is this correct? (Y/N) ")
    
    if verify_departing_city == 'Y' or verify_departing_city == 'y':
        break

# print("Welcome to the Flight Time Calculator. Please enter the departure time:")
# departure_time = input()
# print(f"The departure time you ")