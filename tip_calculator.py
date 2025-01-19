# Display a welcome message
print("Welcome to the tip calculator!")

# Ask the user for the total bill amount and convert it to a float
bill = float(input("What was the total bill? $"))

# Ask the user for the percentage of tip they want to give and convert it to an integer
tip = int(input("What percentage tip would you like to give? 10 12 15 "))

# Ask the user how many people to split the bill with and convert it to an integer
people = int(input("How many people to split the bill? "))

# Convert the tip percentage to a decimal (e.g., 15% becomes 0.15)
tip_as_percent = tip / 100

# Calculate the total tip amount by multiplying the bill by the tip percentage
total_tip_amount = bill * tip_as_percent

# Calculate the total bill by adding the tip amount to the original bill
total_bill = bill + total_tip_amount

# Calculate how much each person should pay by dividing the total bill by the number of people
bill_per_person = total_bill / people

# Round the result to two decimal places to avoid fractions of a cent
final_amount = round(bill_per_person, 2)

# Print the final amount each person needs to pay
print(f"Each person should pay: ${final_amount}")