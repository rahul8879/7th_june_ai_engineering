# Python Assignment

This assignment is based on the topics covered in the `01_PYTHON` folder.

## Instructions

1. Create one Python file for each question or solve all questions in a single file.
2. Use clear variable names.
3. Add comments where needed.
4. Print the final output for each question.
5. Do not use advanced libraries unless the question explicitly allows it.

## Part 1: Variables, Data Types, and Type Casting

1. Create variables for `name`, `age`, `salary`, and `is_student`. Print the value and data type of each variable.
2. Take a number as input from the user and print its square, cube, and data type after converting it to `int`.
3. Create a float variable called `invoice_amount` and print it rounded to 2 decimal places.
4. Store a numeric value as a string and convert it into `int` and `float`. Print all three versions.

## Part 2: Conditions and Loops

5. Take an SSN number as input and print `Valid SSN` if its length is 9, otherwise print `Invalid SSN`.
6. Take a number as input and print whether it is even or odd.
7. Create a list of 8 sales values. Use a `for` loop to calculate the total sales and average sales.
8. Search for a course name inside a list of courses. If found, print `Course available`; otherwise print `Course not available`.

## Part 3: Lists and Tuples

9. Create a list of 10 numbers. Replace the value at index 4 with `100` and print the updated list.
10. Create two lists of daily sales. First use `append()` to combine them and observe the output. Then use `extend()` and compare the result.
11. From a list of numbers, print:
   - the first 3 elements
   - the last 3 elements
   - every second element
12. Create a tuple with 5 values. Try to change one value and write in a comment what error you get and why.

## Part 4: Strings

13. Create a string and print it in:
   - uppercase
   - lowercase
   - title case
14. Write a program that replaces harmful words such as `hack`, `destroy`, and `attack` with `#` symbols of the same length.
15. Given a sentence, count how many words it contains.
16. Convert the following output strings into tuples:

```text
Category : SPAM | Confidence : 0.9
Category : BILLING | Confidence : 0.8
Category : TECHNICAL | Confidence : 0.4
```

Expected format:

```python
[('SPAM', '0.9'), ('BILLING', '0.8'), ('TECHNICAL', '0.4')]
```

## Part 5: Dictionaries and Sets

17. Create a dictionary where keys are day names and values are lists of sales numbers. Find the average sales for each day and store the result in a new dictionary.
18. Create a nested dictionary for 3 products with keys `name`, `price`, and `category`. Print the total cost of all products.
19. Given a list of words, create a dictionary where each word is the key and its length is the value.
20. Create two sets:
   - `city_a = {'id1', 'id2', 'id3'}`
   - `city_b = {'id2', 'id3', 'id4'}`

Print:
   - union
   - intersection
   - difference of `city_a` from `city_b`

## Part 6: Mini Practice Tasks

21. Build a simple prompt using an f-string for this task:
   - role: email classifier
   - email: `"Payment failed but money was deducted"`
   - ask the model to classify the email into `Billing`, `Technical`, `Spam`, or `Personal`

22. Create a list of 5 email texts and write a loop that builds one prompt for each email using `f-string` or `format()`.

23. Write a small content-moderation script that checks if a sentence contains any harmful words from a predefined list.

24. Write a program that removes duplicate IDs from a list using `set`, then prints the unique IDs as a list again.

## Bonus

25. Build a menu-driven program where the user can choose:
   - calculate average sales
   - search course name
   - censor harmful words
   - remove duplicate IDs

## Submission

- Save your code inside the `01_PYTHON/Assignment` folder.
- Prefer meaningful file names such as `question_01.py`, `question_02.py`, or `python_assignment_solution.py`.
