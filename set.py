#inputs = user inputs
#variables = num1, num2,num3, var1, var2, , A ,B
#process = create 2 sets, then perform set intersection
#output = A & B
num = input("Enter your first three no.s separated by spaces: ").split()
num1, num2, num3 = map (int, num)
var = input("Enter your three numbers separated by spaces: ").split()
var1, var2, var3 = map(int, var)

A = {num1, num2, num3}
B = {var1, var2, var3}

#their intersection
C = A & B
print(C)