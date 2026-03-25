def log_call(function):
    """
    Decorator that logs the function name, input, arguments, and output result

    Args:   
        function (callable): The function to be wrapped by the decorator
    Returns: 
        callable: Wrapper function that prints input and output
    """
    def wrapper(*args,**kwargs):
        print(f"Calling function: {function.__name__}")
        if args:
            print(f"Input: {args}")
        if kwargs:
            print(f"Input: {kwargs}")
        res = function(*args,**kwargs)
        print(f"Output: {res}")
        return res
    return wrapper

@log_call
def multiply_numbers(a,b):
    return a*b

if __name__ == "__main__":
    multiply_numbers(5,7)