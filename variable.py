#Basic variable
username="Uma_balan"
email="umabalan259@gmail.com"
age=20
is_active=True
print(f"User {username} registered successfully!")
#Multiple data types
city="Bangalore"
temperature = 28.5
humidity = 65
is_raining = False
forecast = "Partly Cloudy"
print(f"Weather in {city} : {temperature}C , Humidity : {humidity}%")
print(f"Forecast : {forecast}")
#Update Data
age=19
city="Coimbatore"
phone="9876543210"
print(f"Before Update age = {age} , city = {city}")
age=20
city = "Chennai"
print(f"After update age = {age} , city = {city}")
#Calculations with variables
product_price = 500
quantity = 3
tax_rate = 0.18
discount = 50
subtotal = product_price*quantity
tax_amount = subtotal*tax_rate
total_with_tax = subtotal + tax_amount
final_total = total_with_tax - discount
print(f"Subtotal : ${subtotal}")
print(f"Tax(18%) : ${tax_amount}")
print(f"Total with tax : ${total_with_tax}")
print(f"Discount : -${discount}")
print(f"Final Total : ${final_total}")
#combining variables
method = "POST"
endpoint = "/api/tasks"
status_code = 201
response_time_ms = 245
log_message = f"[method]{endpoint} --> Status:{status_code} ({response_time_ms})"
print(log_message)
#Reusing variables
entered_username = "uma_balan"
entered_password = "mypassword123"
correct_username = "uma_balan"
correct_password = "mypassword123"
username_match = (entered_username == correct_username)
password_match = (entered_password == correct_password)
is_login_successful = username_match and password_match
print(f"Login_successful: {is_login_successful}")
#Managing state
cart_item1 = "Laptop"
cart_price_1 = 50000
cart_quantity_1 = 1
cart_item2 = "Mouse"
cart_price_2 = 15000
cart_quantity_2 = 2
total_items = cart_quantity_1 + cart_quantity_2
total_price = (cart_price_1 * cart_quantity_1) + (cart_price_2 * cart_quantity_2)
print(f"Items in cart: {total_items}")
print(f"Item 1: {cart_item1} * {cart_quantity_1} = ${cart_price_1 * cart_quantity_1}")
print(f"Item 2: {cart_item2} * {cart_quantity_2} = ${cart_price_2 * cart_quantity_2}")
print(f"Total: ${total_price}")
#challenge 1: Student Grade System
student_name = "Arjun"
math_score = 85
english_score = 92
science_score = 78
average = (math_score + english_score + science_score /3)
print(f"Student: {student_name}")
print(f"Math: {math_score}, English: {english_score}, Science: {science_score}")
print(f"Average: {average}")
print(f"Total Marks: {math_score + english_score + science_score}")
if average>=50:
    print(f"Status:Pass")
#challenge 2: Bank account operations
account_holder = "Priya Sharma"
initial_balance = 50000
deposit_amount = 10000
withdrawal_amount = 5000
total = initial_balance + deposit_amount
after_deposit = initial_balance + deposit_amount
after_withdrawl = after_deposit - withdrawal_amount
final_balance = initial_balance + deposit_amount - withdrawal_amount
print(f"Account: {account_holder}")
print(f"Initial Balance: ${initial_balance}")
print(f"After Deposit (+10000): ${after_deposit}")
print(f"After Withdrawl (-$50000): {after_withdrawl}")
print(f"Final Balance: ${final_balance}")
#Challenge3: Product Inventory Management
product_name = "Laptop"
product_price = 75000
stock_quantity = 15
reorder_level = 5
total_value = product_price * stock_quantity
is_stock_low = stock_quantity <= reorder_level
print(f"Product: {product_name}(${product_price})")
print(f"Stock Quantity: {stock_quantity}units")
print(f"Inventory Value: ${total_value}")
print(f"Status: {'Low Stock' if is_stock_low else 'Available'}")
#Challenge4: User profile display
user_id = 5001
first_name = "Rajesh"
last_name = "Patel"
email = "rajesh@gmail.com"
phone = "9876543210"
is_verified = True
account_age_days = 365
print("- - - USER PROFILE - - -")
print(f"ID: {user_id}")
print(f"Name: {first_name} {last_name}")
print("Email: ",email)
print("Phone: ",phone)
print(f" Verified { "Yes" if is_verified else "No"}")
print(f"Account Age: {account_age_days} days")
#Challenge 5: Order Processing
order_id = 2001
item_1_name = "Keyboard"
item_1_price = 3000
item_1_qty = 2

item_2_name = "Monitor"
item_2_price = 15000
item_2_qty = 1

tax_rate = 0.18
coupon_discount = 500
subtotal_1 = item_1_price * item_1_qty
subtotal_2 = item_2_price * item_2_qty
grandtotal = subtotal_1 + subtotal_2
tax_amount_1 = 0.18 * grandtotal
final_amount = grandtotal + tax_amount_1 - coupon_discount
print("Order #",order_id)
print("- - -Items---")
print(f"{item_1_name} x {item_1_qty} = ${subtotal_1}")
print(f"{item_2_name} x {item_2_qty} = ${subtotal_2}")
print(f"Subtotal: ${grandtotal}")
print(f"Tax (18%): {tax_amount_1}")
print(f"Total with tax: ${tax_amount_1}")
print(f"Coupon Discount: -${coupon_discount}")
print(f"FINAL TOTAL: ${final_amount}")