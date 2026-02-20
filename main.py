a=float(input("Enter number\n"))
b=float(input("Enter number\n"))
sum_result=a+b
diff_result=a-b
mult_result=a*b
if b>0:
   div_result=a/b
else:
   div_result="Cannot divide by zero"
print(f"Sum: {sum_result}")
print(f"Difference: {diff_result}")
print(f"Multiplication: {mult_result}")
print(f"Division: {div_result}")