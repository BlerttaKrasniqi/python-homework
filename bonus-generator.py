def divisible_by_four(n: int):
    """
    Generator that yields nummbers divisible by 4 up to N

    Args:
        n (int): Upper limit of the range
    Yields:
        int: Numbers divisible by 4 from 1 to n
    """
    for number in range(1,n+1):
        if number %4 == 0:
            yield number

if __name__ == "__main__":
   
    for i in divisible_by_four(30):
        print(i)





        