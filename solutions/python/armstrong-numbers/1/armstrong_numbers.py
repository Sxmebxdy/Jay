def is_armstrong_number(number):
    original_number = number  
    result = 0  
    armstrong = 0  
    while number > 0:
        result += 1
        number //= 10 
    number = original_number 
    while number > 0:
        digit = number % 10
        armstrong += digit ** result
        number //= 10  
    return armstrong == original_number 
