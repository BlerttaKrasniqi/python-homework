values = ["50","75","NaN","100","error","25"]



def get_clean_values(values):
    cleaned_values = []
    for value in values:
        try:
            cleaned_values.append(int(value))
        except ValueError:
            continue
    return cleaned_values

if __name__ == "__main__":
    print("Values before cleaning the list: ")
    print(values)
    print("Cleaned values: ")
    print(get_clean_values(values))
