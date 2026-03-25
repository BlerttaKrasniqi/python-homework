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



