# Lambda functions allow us to declare anonymous functions in a single line of code.
# Example without lambda
def summation(a: int, b: int) -> int:
    return a + b


print(summation(3, 5))

# Lambda function
sumLambda = lambda a, b: a + b
print(sumLambda(2, 4))
