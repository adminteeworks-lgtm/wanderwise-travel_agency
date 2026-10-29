print("Welcome to WanderWise Travel Agency!")
print("-------------------------------------")
print("Explore the World with Us!")
print()
print("1. Pakistan Tour - Rs. 15000")
print("2. Dubai Tour - Rs. 85000")
print("3. Turkey Tour - Rs. 120000")
print()
destination = input("Enter your destination (Pakistan/Dubai/Turkey): ")

if destination.lower() == "pakistan":
    print("Your Pakistan tour package is Rs. 15000.")
elif destination.lower() == "dubai":
    print("Your Dubai tour package is Rs. 85000.")
elif destination.lower() == "turkey":
    print("Your Turkey tour package is Rs. 120000.")
else:
    print("Sorry, this destination is not available.")

print("Thank you for choosing WanderWise!")
