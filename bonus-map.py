def convert_numbers_to_strings(numbers : list[int]) -> list[str]:
    """
    Convert numeric values to string using map().
    
    Args: 
        numbers (list): List of numeric values

    Returns:
        list: List containing the numbers converted to strings
    """
    return list(map(lambda x: str(x),numbers))

if __name__=="__main__":
    numbers = [1,2,3,4,5,6,7,8,9,10]
    print(convert_numbers_to_strings(numbers))