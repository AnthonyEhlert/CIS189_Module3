"""
Program: coupon_calculations.py
Author: Tony Ehlert
Last date modified: 1/25/2023

The purpose of this program is to calculate a total price of an online purchase after cash and percent discount
coupons have been applied and shipping has been added
The input is the amount of a purchase, the amount of a cash coupon(if present),
and the amount of percent coupon (if present)
The output is the final price after all calculations
"""
# import of Constants.py
from Constants import TAX_RATE, SHIP_RATE_1, SHIP_RATE_2, SHIP_RATE_3, FREE_SHIPPING, CASH_DSC_1, CASH_DSC_2, \
    PERCENT_DSC_1, PERCENT_DSC_3, PERCENT_DSC_2, SHIP_RANGE_1, SHIP_RANGE_2, SHIP_RANGE_3

# creation of global variables
cash_coupon_amt = 0.00
percent_coupon_amt = 0.00
shipping_amt = 0.00

# prompt user for amount of purchase and assign to variable
purchase_price = float(input("Please enter the amount of your purchase: \n"))

# prompt user if a cash coupon is being used and assign to variable
cash_coupon_present = input("Do you have a cash coupon? [Y]es or [N]o\n")

# start of if statements for cash coupon calculations
if (cash_coupon_present == 'y' or cash_coupon_present == 'Y'):

    # prompt user for cash coupon amount and assign to variable
    user_cash_input = input("Do you have a $5 or $10 coupon? [5] or [10]\n")

    # if-elif statements to assign proper cash coupon amount from Constants.py
    if (user_cash_input == '5'):
        cash_coupon_amt = CASH_DSC_1
    elif (user_cash_input == '10'):
        cash_coupon_amt = CASH_DSC_2
    else:
        cash_coupon_amt = 0.00
#print("cash coupon amount = " + str(cash_coupon_amt)) # test print to ensure cash_coupon_amt is correct

# calculate subtotal minus cash off coupon and assign to variable
cash_off_subtotal = purchase_price - cash_coupon_amt
#print("cash off subtotal = " + str(cash_off_subtotal)) # test print to ensure cash_off_subtotal is correct

# prompt user if a percent coupon is being used and assign to variable
percent_coupon_present = input("Do you have a percent coupon? [Y]es or [N]o\n")

# start of if statements for percent coupon calculations
if (percent_coupon_present == 'y' or percent_coupon_present == 'Y'):

    # prompt user for percent coupon amount and assign to variable
    user_percent_input = input("Do you have a 10%, 15%, or 20% coupon? [10], [15], or [20]\n")

    # if-elif statements to assign proper percent coupon amount from Constants.py
    if (user_percent_input == '10'):
        percent_coupon_amt = PERCENT_DSC_1
    elif (user_percent_input == '15'):
        percent_coupon_amt = PERCENT_DSC_2
    elif (user_percent_input == '20'):
        percent_coupon_amt = PERCENT_DSC_3
    else:
        percent_coupon_amt = 0.00
#print("coupon percent = " + str(percent_coupon_amt)) # test print to ensure percent_coupon_amt is correct

# calculate subtotal minus percent coupon
percent_off_subtotal = cash_off_subtotal - (cash_off_subtotal * percent_coupon_amt)
#print("percent off subtotal = " + str(percent_off_subtotal)) # test print to ensure percent_off_subtotal is correct

# calculate calculate total tax amount and assign to variable
tax_total = percent_off_subtotal * TAX_RATE
#print("tax total = " + str(tax_total)) # test print to ensure tax_total is correct

# add tax_total to percent_off_subtotal to get final subtotal before shipping
final_subtotal = percent_off_subtotal + tax_total
#print("final subtotal = " + str(final_subtotal))  # test print to ensure final_subtotal is correct

# start of if-elif statements to determine total shipping
if(SHIP_RANGE_1 <= final_subtotal < SHIP_RANGE_2):
    shipping_amt = SHIP_RATE_2
elif(SHIP_RANGE_2 <= final_subtotal < SHIP_RANGE_3):
    shipping_amt = SHIP_RATE_3
elif( final_subtotal >= 50):
    shipping_amt = FREE_SHIPPING
else:
    shipping_amt = SHIP_RATE_1
#print("shipping amount = " + str(shipping_amt)) # test print to ensure shipping_amt is correct

# calculation of final total
final_total = final_subtotal + shipping_amt

# creation of final output string
final_output_string = f"Your final order total is: ${final_total:6.2f}"

# print out of final output string
print(final_output_string)
