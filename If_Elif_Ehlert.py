"""
Program: If_Elif_Ehlert.py
Author: Tony Ehlert
Last date modified: 1/25/2023

The purpose of this program is get input from user that denotes what level of membership they want to subscribe to
and then output their selection along with the cost of the membership
The input is an integer 1-5 which correlates to a subscription level
The output is a print statement containing the user's selection along with the price
"""

# print out describing the Programmer's Toolkit Monthly Subscription Box and membership details
print("Welcome to the Programmer's Toolkit Monthly Subscription Box membership sign up!")
print("After signing up for a membership you will receive a monthly package that could include: ")
print("T-shirts, stickers, figurines, or even programming books.  Each month is something different.")
print("Below are the different membership levels, their prices, and descriptions:")
print("Platinum, $60- Receive five items a month, plus an insider report the newest coding trends.")
print("Gold, $50- Receive at least four items a month.")
print("Silver, $40- Receive at least three items a month.")
print("Bronze, $30- Receive at least two items a month.")
print("Free Trial, FREE!!- Receive one items a month.")

# print out informing user what to enter for their choice & asking user to enter their choice & assign to a variable
print("Please use the following to make a selection")
print("Platinum = 1, Gold = 2, Silver = 3, Bronze = 4, Free Trial = 5")
user_choice = int(input("Please enter your choice: "))

# start of if-elif statements to determine final print out based on user's selection
if (user_choice == 1):
    print("You selected \"Platinum\", that is $60 a month.")
elif (user_choice == 2):
    print("You selected \"Gold\", that is $50 a month.")
elif (user_choice == 3):
    print("You selected \"Silver\", that is $40 a month.")
elif (user_choice == 4):
    print("You selected \"Bronze\", that is $30 a month.")
else:
    print("You selected \"Free Trial\", there is no cost for that.")

# observed outputs after manually running code
"""
# Test 1, Input = 1, Expected ="You selected "Platinum", that is $60 a month."
					Actual = "You selected "Platinum", that is $60 a month."
# Test 2, Input = 5, Expected = "You selected "Gold", that is $50 a month."
					Actual = "You selected "Gold", that is $50 a month."
# Test 3, Input = 5, Expected = "You selected "Silver", that is $40 a month."
					Actual = "You selected "Silver", that is $40 a month."
# Test 4, Input = 5, Expected = "You selected "Bronze", that is $30 a month."
					Actual = "You selected "Bronze", that is $30 a month."
# Test 5, Input = 5, Expected = "You selected "Free Trial", there is no cost for that."
					Actual = "You selected "Free Trial", there is no cost for that."
# Test 6, Input = 10, Expected = "You selected "Free Trial", there is no cost for that."
					Actual = "You selected "Free Trial", there is no cost for that."
"""
