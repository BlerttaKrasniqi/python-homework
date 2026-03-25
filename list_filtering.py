numbers = [4,8,12,16,20,24]

def filter_list(numbers : list[int]) -> list[int]:
    """
    Filter numbers that are divisible by 4 and greater than 10.
    Args:
        numbers (list): List of integer values
    Returns:
        list: List containing integer numbers divisible by 4 and greater than 10
    """
    
    return list(filter(lambda x: x%4==0 and x>10, numbers))

if __name__=="__main__":
    print("List with numbers: ",numbers)
    print("Filtered list, containing only numbers divisible by 4 and greater than 10: ",filter_list(numbers))
    