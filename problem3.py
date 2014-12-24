import math
#This program tackles problem 3 of Project Euler, the objective is to find
#The largest prime factor of the number 600851475143
#Written by Deep Prasad, December 23rd, 2014


n = 600851475143
i = 2
while i * i < n:
    while n % i == 0:
        n = n / i
    i += 1
print n
