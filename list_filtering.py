numbers = [4,8,12,16,20,24]

def filter_list(numbers):
    return list(filter(lambda x: x%4==0 and x>10, numbers))

if __name__=="__main__":
    print("List with numbers: ",numbers)
    print("Filtered list, containing only numbers divisible by 4 and greater than 10: ",filter_list(numbers))
    