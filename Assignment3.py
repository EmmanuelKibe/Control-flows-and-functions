def calculate_discount(price, discount_percent):
     final_price = price - (discount_percent/100 * price)
     if discount_percent >= 20:
          return final_price
     else:
          return price
     



price = int(input("Enter the price of your item: "))
discount_percent = int(input("Enter the discount percentage of your item: "))

print("The final price of your item is: ", calculate_discount(price, discount_percent))
        
     