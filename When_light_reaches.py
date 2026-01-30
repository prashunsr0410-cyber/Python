#when light reaches on earth from different planets 
#speed = distance / time

AU = 149,597,870 #distance in KM

c = 299792 #speed of light in KM/s

Planet_Name = input("Enter the name of the planet1(Where you want to see the time to reach the light): ")
distance = float(input("Enter the distance in KM: "))
Planet_Name2 = input("Enter the name of the planet2(From where the light is coming): ")

print(f"The time light takes to reach the {Planet_Name.upper()} from {Planet_Name2.upper()} is:")


time = distance / c

print(f"The time Light takes to reach the {Planet_Name.upper()} from {Planet_Name2.upper()} is {format(time, '.2f')} seconds.")
print(f"The time Light takes to reach the {Planet_Name.upper()} from {Planet_Name2.upper()} is {format(time / 60, '.2f')} minutes.") 
print(f"The time Light takes to reach the {Planet_Name.upper()} from {Planet_Name2.upper()} is {format(time / 3600, '.2f')} hours.") 
print(f"The time Light takes to reach the {Planet_Name.upper()} from {Planet_Name2.upper()} is {format(time / 86400, '.2f')} days.") 



#Sample Data to test this code.
"""
These all distances are from EARTH In KM

Planet Name: JUPITER
Distance in KM: 642254075

Planet Name: MARS
Distance in KM: 356279555

Distance of SUN from EARTH:  149597870

"""