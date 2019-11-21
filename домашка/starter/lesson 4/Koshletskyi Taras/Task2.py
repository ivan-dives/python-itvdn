
def factorial_for(number=5):
    result = 1
    for i in range(1, number+1):
        result *= i
    return result

def factorial_while(number=5):
    result = 1
    iter = 1
    while iter <= number:
        result *= iter
        iter += 1
    return result

print(factorial_for(4))
print(factorial_while(4))
