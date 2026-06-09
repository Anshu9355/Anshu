from sys import hash_info

print("program to calculate the average of the numbers in a given list")
a=[1,2,3,4,5,6,7,8,9,10,11]
sum=0
count=0
for num in a:
    sum=sum+num
    count=count+1
print(sum)
print("Average of the list is",sum/count)


print("************************************************************************************")

print("read a number n and compute n+nn+nnn")
#a=int(input("enter the number"))
print("the square of number is")
#print(a,"+",a*a,"+",a*a*a)

print("**************************************************************************************")

print("Write a program to reverse the given number")
#b=int(input("enter the number"))

num = 12345
reversed_num = 0

while num > 0:
    digit = num % 10                 # Extracts the last digit (e.g., 5)
    reversed_num = (reversed_num * 10) + digit  # Appends digit to the right
    num = num // 10                  # Drops the last digit from the number

print(reversed_num)  # Output: 54321

print("*******************************************************************************")

print("check the number is positive or negative")
#num=int(input("enter the number"))
if num>0:
    print("number is positive")
elif num<0:
    print("number is negative")
else:
    print("number is Zero")

print("**********************************************************************************************")






