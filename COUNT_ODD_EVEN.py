# A Python program to count the number of even and odd numbers from a series of numbers.

numbers =(input("Enter a series of numbers separated by spaces: "))
number_list = numbers.split()
even_count = 0
odd_count = 0
for i in number_list:
    num=int(i)
    if num % 2==0:
        even_count +=1
    else:
        odd_count+=1
print("Number of even numbers: ", even_count)
print("Number of odd numbers: ", odd_count)
