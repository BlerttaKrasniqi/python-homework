text = "Python is powerful and python helps build powerful applications"

def word_count(text : str) -> dict[str, int]:
    """
    Count how many times each word appears in the text.
    Args:
        text (str): Input text to analyze
    Returns:
        result (dict): Dictionary where keys are words and values are the number of occurences. 
    """
    words = text.lower().split()
    result = {}
    for word in words:
        result[word]=result.get(word,0) + 1
    return result

if __name__ == "__main__":
    print(word_count(text))
