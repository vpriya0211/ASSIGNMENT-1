# A Python program that accepts a word from the user and reverse it.

word = input("Enter a word : ")
reverse= ""
for i in word:
    reverse = i + reverse
print("Reversed word:", reverse)

# A Python program to get the Fibonacci series between 0 to 50.

limit = int(input("Enter an upper limit for the Fibonacci series: "))
a=0
b=1
if a <= limit:
    print(a)
while b <= limit:
    print(b)
    a, b = b, a + b

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
