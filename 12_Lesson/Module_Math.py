import math as m
print(dir(m))

number = int(input("Enter a number: "))
print(f'the sqrt of {number} is {m.sqrt(number):.2f}') #this will give us the square root of the number and the :.2f will round the result to 2 decimal places
print(f'the round of {number} is {m.ceil(number):.2f}') #this will round the number up to the nearest integer
print(f'the square of {number} is {m.pow(number,2):.2f}') #this will give us the number to the power of 2
print(f'the cube of {number} is {m.pow(number,3):.2f}') #this will give us the number to the power of 3
print(f'the ceiling of 3.2 is {m.ceil(3.2):.2f}') #this will round the number up to the nearest integer    
print(f'the floor of 3.8 is {m.floor(3.8):.2f}') #this will round the number down to the nearest integer
print(f'the value of pi is {m.pi}') #this will give us the value of pi
print(f'the value of e is {m.e}') #this will give us the value of e
print(f'the sine of 90 degrees is {m.sin(90)}') #this will give us the sine of 90 degrees
print(f'the cosine of 90 degrees is {m.cos(90)}') #this will give us the cosine of 90 degrees    
print(f'the tangent of 90 degrees is {m.tan(90)}') #this will give us the tangent of 90 degrees
print(f'the natural logarithm of 10 is {m.log(10)}') #this will give us the natural logarithm of 10
print(f'the logarithm of 100 to the base 10 is {m.log10(100)}') #this will give us the logarithm of 100 to the base 10  
print(f'the factorial of 5 is {m.factorial(5)}') #this will give us the factorial of 5
print(f'the greatest common divisor of 48 and 18 is {m.gcd(48,18)}') #this will give us the greatest common divisor of 48 and 18
print(f'the least common multiple of 48 and 18 is {m.lcm(48,18)}') #this will give us the least common multiple of 48 and 18
print(f'90 degrees is equal to {m.radians(90)} radians') #this will convert 90 degrees to radians
print(f'pi/2 radians is equal to {m.degrees(m.pi/2)} degrees') #this will convert pi/2 radians to degrees 
print(f'0.1 + 0.2 is close to 0.3: {m.isclose(0.1 + 0.2, 0.3)}') #this will check if 0.1 + 0.2 is close to 0.3
print(f'10 is a finite number: {m.isfinite(10)}') #this will check if 10 is a finite number
print(f'Infinity is an infinite number: {m.isinf(float("inf"))}') #this will check if infinity is an infinite number
print(f'NaN is a NaN value: {m.isnan(float("nan"))}') #this will check if NaN is a NaN value
print(f'1 with the sign of -5 is: {m.copysign(1, -5)}') #this will return 1 with the sign of -5, which is -1
print(f'the absolute value of -5 is: {m.fabs(-5)}') #this will return the absolute value of -5, which is 5
print(f'the remainder of 10 divided by 3 is: {m.fmod(10, 3)}') #this will return the remainder of 10 divided by 3, which is 1
print(f'the mantissa and exponent of 8 are: {m.frexp(8)}') #this will return the mantissa and exponent of 8
print(f'0.5 multiplied by 2 to the power of 3 is: {m.ldexp(0.5, 3)}') #this will return 0.5 multiplied by 2 to the power of 3, which is 4
print(f'the fractional and integer parts of 3.14 are: {m.modf(3.14)}') #this will return the fractional and integer parts of 3.14
print(f'the integer part of 3.14 is: {m.trunc(3.14)}') #this will return the integer part of 3.14, which is 3
print(f'e to the power of 1 is: {m.exp(1)}') #this will return e to the power of 1, which is e
print(f'e to the power of 1 minus 1 is: {m.expm1(1)}') #this will return e to the power of 1 minus 1, which is e - 1
print(f'the natural logarithm of 1 is: {m.log1p(1)}') #this will return the natural logarithm of 1    
print(f'the logarithm of 8 to the base 2 is: {m.log2(8)}') #this will return the logarithm of 8 to the base 2, which is 3
print(f'the logarithm of 1000 to the base 10 is: {m.log10(1000)}') #this will return the logarithm of 1000 to the base 10, which is 3
print(f'2 to the power of 10 is: {m.pow(2, 10)}') #this will return 2 to the power of 10, which is 1024
print(f'3.7 rounded down to the nearest integer is: {m.floor(3.7)}') #this will round 3.7 down to the nearest integer, which is 3
print(f'3.2 rounded up to the nearest integer is: {m.ceil(3.2)}') #this will round 3.2 up to the nearest integer, which is 4
