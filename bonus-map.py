def convert_numbers_to_strings(numbers):
    return list(map(lambda x: str(x),numbers))

if __name__=="__main__":
    numbers = [1,2,3,4,5,6,7,8,9,10]
    print(convert_numbers_to_strings(numbers))