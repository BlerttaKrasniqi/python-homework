## 1. Delivery Records Processing

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

## 5. List Filtering

This example filters numbers from a list using the `filter()` function.

The program keeps only numbers that:
- are divisible by 4
- are greater than 10

The filtering is done using a lambda function.

### Implementation
<img width="1109" height="424" alt="image" src="https://github.com/user-attachments/assets/35940213-ff72-4906-9183-7b71ff2c420a" />

### Output
<img width="850" height="57" alt="image" src="https://github.com/user-attachments/assets/5a0c4e59-ef87-43de-8b7d-55698c1acba9" />

## 6. File Handling with Validation

This example reads a file and analyzes its content.

The program calculates:
- total number of words
- number of non-empty lines

It also handles error cases:
- file not found
- empty file

Exception handling is used to prevent the program from crashing.

### Implementation

<img width="863" height="704" alt="image" src="https://github.com/user-attachments/assets/c15f3c7b-1f5d-4399-8e35-751ecaee8b9d" />

### Output
<img width="542" height="91" alt="image" src="https://github.com/user-attachments/assets/2b0eb07c-5f1d-45af-aff3-c775aadff92e" />

## 7. Data Integrity Check

This example validates account records and identifies invalid data.

Each account is checked based on the following rules:

- `account_id` must not be `None`
- `owner` must not be empty
- `balance` must be positive

If an account contains invalid data, the program stores the full record together with a list of issues.

### Implementation
<img width="855" height="881" alt="image" src="https://github.com/user-attachments/assets/20b6a6e7-5caf-4954-9fcc-2c9ef2d96a4d" />

### Output
<img width="965" height="101" alt="image" src="https://github.com/user-attachments/assets/d7b093f8-e235-40f9-b580-e44b79438eb5" />

## Bonus – Decorator for Logging Function Calls

This example demonstrates how to create a decorator that logs the function name, input arguments, and output result.

The decorator wraps another function and prints information every time the function is called.

This allows adding extra behavior without modifying the original function.

### Decorator
<img width="787" height="642" alt="image" src="https://github.com/user-attachments/assets/fb113948-ccce-48cb-8441-8187a2919bcb" />

### Output
<img width="468" height="117" alt="image" src="https://github.com/user-attachments/assets/7f65e785-2c5d-4f7b-9446-c3bcf9453e0b" />


## Bonus – Generator

This example demonstrates how to use a generator to produce numbers divisible by 4 up to a given limit.

A generator uses the `yield` keyword to return values one at a time instead of returning the whole list at once.

This is more memory efficient and useful for large ranges of data.

### Generator function
<img width="646" height="440" alt="image" src="https://github.com/user-attachments/assets/5c6cd34c-dcd7-44d2-85aa-d886ef1e0bb6" />

### Output
<img width="520" height="200" alt="image" src="https://github.com/user-attachments/assets/e6c98e4c-352d-440d-b5cb-a30c1b91c0c5" />

## Bonus – map()

This example demonstrates how to use the `map()` function to convert numeric values to strings.

The `map()` function applies a function to every element in a list and returns the result as an iterable.  
In this case, each number is converted to a string using `str()`.

### Function
<img width="689" height="378" alt="image" src="https://github.com/user-attachments/assets/1ecb7377-5779-41c3-ab16-3a46b2a4c1a9" />

### Output
<img width="703" height="81" alt="image" src="https://github.com/user-attachments/assets/bb0dc860-9f55-4317-a388-ac4b123bc3b3" />



















