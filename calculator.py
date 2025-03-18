num1 = float(input("Enter the first number: "))
oper=input('*-+/')
num2 = float(input("Enter the second number: "))
if oper=='+':
    sum_result = num1 + num2
if oper=='-':
    difference_result = num1 - num2
if oper=='*':
    product_result = num1 * num2
if oper=='/' and num2>0:
    quotient_result = num1 / num2
else:
    print('Second number cannot be zero or lesser')
print(f"Results of your two numbers:")
print(f"Sum: {sum_result}")  # ➕
print(f"Difference: {difference_result}")  
print(f"Product: {product_result}")  
print(f"Quotient: {quotient_result}") 
