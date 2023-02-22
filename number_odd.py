#A four-digit integer is given. Find the number of odd digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var_int = 9856
#Print the number of odd digits in the variable "var_int".

x1 = var_int%10
x2 = var_int//10%10
x3 = var_int//10//10%10
x4 = var_int//10//10//10%10
print(x4%2 + x3%2 + x2%2 + x1%2 )

