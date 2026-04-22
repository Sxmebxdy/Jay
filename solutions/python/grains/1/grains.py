def square(number):
    if 64 < number or number <= 0:
        raise ValueError("square must be between 1 and 64")
    result = 1
    for num in range(number-1):
        result *= 2
    return result
      
def total():
    result = 1
    for num in range(0, 64):
        result *= 2
    return result - 1
        
