<img width="902" height="103" alt="image" src="https://github.com/user-attachments/assets/8517860f-3728-42f1-b167-bcbd304d3bc8" />## 1. Delivery Records Processing

This example processes a list of delivery records and filters only the valid ones.

Each delivery record is stored as a dictionary with the following fields:

- delivery_id
- distance
- status

The program returns only deliveries that:
- have a positive distance
- have status equal to "completed"

This is implemented using list comprehension.

### Implementation:
<img width="1160" height="690" alt="image" src="https://github.com/user-attachments/assets/09150f05-c70d-4363-8b07-d2157a80f62f" />


### Output

<img width="592" height="158" alt="image" src="https://github.com/user-attachments/assets/239523af-e98f-4230-90ce-a3c3b3ab1489" />


## 2. Clean Numeric Data

This example processes a list of string values and keeps only valid numeric values.

Some elements in the list may contain invalid data such as text or non-numeric values.  
The program converts valid values to integers and ignores invalid ones using exception handling.

### Implementation
<img width="935" height="632" alt="image" src="https://github.com/user-attachments/assets/5ddaf92e-6b10-4416-b23b-d4897f4b3b87" />

### Output

<img width="527" height="158" alt="image" src="https://github.com/user-attachments/assets/3db8d6ad-3a5e-4b79-9482-2bc09070e3e8" />

## 3. Custom Validation Exception

This example demonstrates how to create and use a custom exception in Python.

A custom exception `InvalidDistanceError` is defined and raised when the distance value is not within the allowed range.

Conditions:
- Distance must be greater than 0
- Distance must not exceed 1000

If the value is invalid, the program raises an exception and prints an error message.

### Implementation
<img width="842" height="745" alt="image" src="https://github.com/user-attachments/assets/1ece17bf-cce4-45c3-bef5-2736a438720b" />

### Output 
<img width="493" height="136" alt="image" src="https://github.com/user-attachments/assets/18de386e-a911-4d6e-b81f-863b8889d44a" />

## 4. Text Analysis

This example analyzes a text and counts how many times each word appears.

The text is converted to lowercase so that words like "Python" and "python" are treated as the same word.  
The result is stored in a dictionary where:

- key = word
- value = number of occurrences

### Implementation
<img width="960" height="463" alt="image" src="https://github.com/user-attachments/assets/ef416b35-b960-4167-a380-3cb6d0747757" />

### Output
<img width="902" height="103" alt="image" src="https://github.com/user-attachments/assets/c3148f49-0573-40a5-8f02-0e7cf3ff1f90" />









