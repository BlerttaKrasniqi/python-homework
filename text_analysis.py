text = "Python is powerful and python helps build powerful applications"

def word_count(text):
    words = text.lower().split()
    result = {}
    for word in words:
        result[word]=result.get(word,0) + 1
    return result

if __name__ == "__main__":
    print(word_count(text))
