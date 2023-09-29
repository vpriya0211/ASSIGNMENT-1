# A Python program to get the Fibonacci series between 0 to 50.

limit = int(input("Enter an upper limit for the Fibonacci series: "))
a=0
b=1
if a <= limit:
    print(a)
while b <= limit:
    print(b)
    a, b = b, a + b