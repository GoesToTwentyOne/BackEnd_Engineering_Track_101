def external(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} called")
        return result
    return wrapper


@external
def sum_values(*args, **kwargs):
    total = sum(args)
    return total


def callback_even(func):
    def wrapper(*args, **kwargs):
        even_numbers = [num for num in args if num % 2 == 0]
        return func(*even_numbers, **kwargs)
    return wrapper


def callback_odd(func):
    def wrapper(*args, **kwargs):
        odd_numbers = [num for num in args if num % 2 != 0]
        return func(*odd_numbers, **kwargs)
    return wrapper


nslice = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s1 = sum_values(*nslice)
print("Total sum:", s1)

s2 = callback_even(sum_values)(*nslice)
print("Even sum:", s2)

s3 = callback_odd(sum_values)(*nslice)
print("Odd sum:", s3)
