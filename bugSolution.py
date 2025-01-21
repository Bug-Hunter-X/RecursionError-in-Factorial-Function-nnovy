def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")
#Test with large number: 
number = 1000
result = factorial(number)
print(f"The factorial of {number} is {result}") 