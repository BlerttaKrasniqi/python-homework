values = ["50","75","NaN","100","error","25"]

cleaned_values = []
for v in values:
    if v.isdigit():
        cleaned_values.append(int(v))  
print(cleaned_values)


