x = 78
y = "Is an integer"

print(x, end=" ")
print(y)

#Camel Case
firstNumber = 45
#Pascal Case
SecondNumber = 89
#Snake Case
third_number = 56

print("Sum of no. ",(firstNumber+ SecondNumber+third_number))

#Many Values to Multiple Variables
firstnum, secondnum, thirdnum = 45, 89, 56
print(
"FirstNumber: ",firstnum,"\n",
"SecondNumber: ",secondnum,"\n",
"ThirdNumber: ",thirdnum)

print("Sum is: ",(firstnum + secondnum + thirdnum))

#unpacking collection
num_list= [45, 89,56]
num1, num2, num3 = num_list
print("Sum is: ",(num1 + num2 + num3))

print("Sum is"+num1)
