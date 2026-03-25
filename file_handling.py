def file_validation(file_name : str) -> dict | str:
    """
    Read a file and count the total number of words and non-empty lines.

    Args:
        file_name (str): Name of the file to read.
    Returns:
        dict: Contains total words and number of non-empty lines
        str: Error message if the file is empty or not found
    """
    try:
        with open(file_name,"r") as f:
            count_word = 0
            non_empty_lines = 0
            for line in f:
                if line.strip():
                    non_empty_lines+=1
                    count_word+=len(line.split())
            if count_word == 0 and non_empty_lines == 0:
                return "The file is empty"
            return {
                "total words: ":count_word, "non_empty_lines":non_empty_lines
            }
    except FileNotFoundError:
        return("File not found")
    
if __name__=="__main__":
    print(file_validation("file.txt"))
