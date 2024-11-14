# Fuel Consumption
# Write  program to calculate the fuel efficiency of a car in kilometers per liter
# A car travels 400km using 50 liters of fuel. calculate its fuel efficiency
print ("FUEL EFFICIENCY CALCULATOR")
distance = int(input("Enter distance travelled (km): "))
fuel= int(input("Enter the fuel consumed (L): "))
cal= distance/fuel
liter = 100 /cal
print("The fuel efficiency of your car in kilometers per liter is " + str(cal) + " Km/L")