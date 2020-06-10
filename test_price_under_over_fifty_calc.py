#Start Program
"""
Program: test_price_under_between_ten_thirty_cal.py
Author: Paul Thairu
Last date modified: 06/10/2020

The purpose of this program is to calculate discount based on coupons and percentage discount
for item price which is between 10 and 30 dollars.
The program calculates the discount amount
add shipping cost
then calculate tax
then finally give the final sales price
"""
# declaring variables to be used
cash_off_coupon = 0
total_price = 0
SHIPPING_COST = 0
TAX = 0.06
TEN_THIRTY_SHIPPING_COST = 5.95
percentage_discount = 0
price_after_cash_discount = 0
price_after_percentage_disc = 0
price_after_all_discount = 0
add_shipping_cost = 0
cal_tax = 0


def calculate_price(total_price, price_after_cash_discount, price_after_percentage_disc):
    return total_price + TAX + SHIPPING_COST


if __name__ == '__main__':
    """
price: more than 50, 5 cash, 10%
price: more than 50, 5 cash, 15%
price: more than 50, 5 cash, 20%
price: more than 50, 10cash, 10%
price: more than 50,  10 cash, 15%
price: more than 50, 10 cash, 20%
"""
purchase_price = float(input("Please enter the purchase price: "))
# Condition to check if the price is below 10 dollars
if purchase_price < 50:
    print("BECAUSE YOUR PURCHASE PRICE IS LESS '$50' YOU GET NO DISCOUNTS. 'SORRY'!!!")
    tax = purchase_price * TAX
    total_price = purchase_price + tax
    total_price = calculate_price(purchase_price, price_after_cash_discount, price_after_percentage_disc)
    print("Tax (6%)" + str(tax))
    print("Sales Price is : $" + str(total_price))

# calculating sales price, shipping cost and discounts if the price is more than 10
# and less than 30 dollars
# purchase_price = float(input("Please enter the purchase price: "))
else:
    if purchase_price >= 50:
        cash_off_coupon = float(input("Please enter your cash coupon with $5 or $10: "))
        percentage_discount = float(input("Please enter your % discount with %10, %15, %20 or 30%: "))

    if cash_off_coupon == 5.00:
        if percentage_discount == 10:
            price_after_cash_discount = purchase_price - cash_off_coupon
            total_price = purchase_price - price_after_cash_discount
            price_after_percentage_disc = (percentage_discount / 100) * price_after_cash_discount
            price_after_all_discount = price_after_cash_discount - price_after_percentage_disc
            add_shipping_cost = price_after_all_discount + SHIPPING_COST
            cal_tax = add_shipping_cost * TAX
            total_price = add_shipping_cost + cal_tax
            total_price = calculate_price(purchase_price, price_after_cash_discount, price_after_percentage_disc)

        elif percentage_discount == 15:
            price_after_cash_discount = purchase_price - cash_off_coupon
            total_price = purchase_price - price_after_cash_discount
            price_after_percentage_disc = (percentage_discount / 100) * price_after_cash_discount
            price_after_all_discount = price_after_cash_discount - price_after_percentage_disc
            add_shipping_cost = price_after_all_discount + SHIPPING_COST
            cal_tax = add_shipping_cost * TAX
            total_price = add_shipping_cost + cal_tax
            total_price = calculate_price(purchase_price, price_after_cash_discount, price_after_percentage_disc)
        elif percentage_discount == 20:
            price_after_cash_discount = purchase_price - cash_off_coupon
            total_price = purchase_price - price_after_cash_discount
            price_after_percentage_disc = (percentage_discount / 100) * price_after_cash_discount
            price_after_all_discount = price_after_cash_discount - price_after_percentage_disc
            add_shipping_cost = price_after_all_discount + SHIPPING_COST
            cal_tax = add_shipping_cost * TAX
            total_price = add_shipping_cost + cal_tax
        elif percentage_discount == 30:
            price_after_cash_discount = purchase_price - cash_off_coupon
            total_price = purchase_price - price_after_cash_discount
            price_after_percentage_disc = (percentage_discount / 100) * price_after_cash_discount
            price_after_all_discount = price_after_cash_discount - price_after_percentage_disc
            add_shipping_cost = price_after_all_discount + SHIPPING_COST
            cal_tax = add_shipping_cost * TAX
            total_price = add_shipping_cost + cal_tax
            total_price = calculate_price(purchase_price, price_after_cash_discount, price_after_percentage_disc)

    if cash_off_coupon == 10.00:
        if percentage_discount == 10:
            price_after_cash_discount = purchase_price - cash_off_coupon
            total_price = purchase_price - price_after_cash_discount
            price_after_percentage_disc = (percentage_discount / 100) * price_after_cash_discount
            price_after_all_discount = price_after_cash_discount - price_after_percentage_disc
            add_shipping_cost = price_after_all_discount + SHIPPING_COST
            cal_tax = add_shipping_cost * TAX
            total_price = add_shipping_cost + cal_tax
            total_price = calculate_price(purchase_price, price_after_cash_discount, price_after_percentage_disc)

        elif percentage_discount == 15:
            price_after_cash_discount = purchase_price - cash_off_coupon
            total_price = purchase_price - price_after_cash_discount
            price_after_percentage_disc = (percentage_discount / 100) * price_after_cash_discount
            price_after_all_discount = price_after_cash_discount - price_after_percentage_disc
            add_shipping_cost = price_after_all_discount + SHIPPING_COST
            cal_tax = add_shipping_cost * TAX
            total_price = add_shipping_cost + cal_tax
            total_price = calculate_price(purchase_price, price_after_cash_discount, price_after_percentage_disc)

        elif percentage_discount == 20:
            price_after_cash_discount = purchase_price - cash_off_coupon
            total_price = purchase_price - price_after_cash_discount
            price_after_percentage_disc = (percentage_discount / 100) * price_after_cash_discount
            price_after_all_discount = price_after_cash_discount - price_after_percentage_disc
            add_shipping_cost = price_after_all_discount + SHIPPING_COST
            cal_tax = add_shipping_cost * TAX
            total_price = add_shipping_cost + cal_tax
            total_price = calculate_price(purchase_price, price_after_cash_discount, price_after_percentage_disc)

        elif percentage_discount == 30:
            price_after_cash_discount = purchase_price - cash_off_coupon
            total_price = purchase_price - price_after_cash_discount
            price_after_percentage_disc = (percentage_discount / 100) * price_after_cash_discount
            price_after_all_discount = price_after_cash_discount - price_after_percentage_disc
            add_shipping_cost = price_after_all_discount + SHIPPING_COST
            cal_tax = add_shipping_cost * TAX

            total_price = calculate_price(purchase_price, price_after_cash_discount, price_after_percentage_disc)
            total_price = add_shipping_cost + cal_tax
print("Purchase price is: $" + str(purchase_price))
print("Coupon discount applied: $" + str(cash_off_coupon))
print("Price after cash coupon: $" + str(price_after_cash_discount))
print("% discount: $" + str(price_after_percentage_disc))
print("Price after % discount: $" + str(price_after_all_discount))
print("SHIPPING COST IS FREE : $" + str(add_shipping_cost))
print("Tax (6%): $" + str(cal_tax))
print("Sales Price is : $" + str(total_price))


#End program
