def divisible_by_four(n):
    for number in range(1,n+1):
        if number %4 == 0:
            yield number

if __name__ == "__main__":
   
    for i in divisible_by_four(30):
        print(i)