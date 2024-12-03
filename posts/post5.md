I often run into a scenario when writing unit tests and mocking up code where I need to convert a block of text data into Python format. Whether it's data from a CSV file, an email, or even a simple copy-paste from a spreadsheet, manually converting text data to make it play nice with Python can be a tedious and error-prone task.

Now of course in some cases, we can dump the data into Excel and use CONCAT to convert to Python syntax, but this becomes untenable once the number of fields goes beyond 3 or 4.

This is a handy dandy function that will do the conversion for you. You can simply take the plain text data, say from a csv file, paste into a block comment, and hit Run!

```
import pandas as pd
from io import StringIO

def text_to_dict(text, delimiter=','):
    # Read the text data
    data = StringIO(text)
    df = pd.read_csv(data, delimiter=delimiter)
    
    # Generate the DataFrame definition
    dataframe_definition = "data = {\n"
    
    for column in df.columns:
        dataframe_definition += f"    '{column}': {df[column].tolist()},\n"
    
    dataframe_definition += "}\n"
    
    return dataframe_definition
```

So here's what you'd do. Dump your text into a block comment as shown with **text_data**.

```
# EXAMPLE 1
# Provided text data

text_data = """
Name,Age,Occupation
Alice,25,Software Engineer
Bob,30,Data Scientist
Carol,28,Product Manager
"""

# Generate the DataFrame definition
output = text_to_dict(text_data)

# Print the DataFrame definition
print(output)
```

The code above will convert your plain, comma delimited text to a Python dictionary with correct syntax that is ready to go! And of course, it's trivial to go from dict to DataFrame should you need to.

```
# OUTPUT
# This is the exact format that is returned by the function, which you can see 
# is immediately compatible with Python
data = {
    'Name': ['Alice', 'Bob', 'Carol'],
    'Age': [25, 30, 28],
    'Occupation': ['Software Engineer', 'Data Scientist', 'Product Manager'],
}
```

One more example with a different delimiter, and the function still works like a charm.

```
# EXAMPLE 2
# Provided text data
text_data = """
Name;Age;Occupation
Alice;25;Software Engineer
Bob;30;Data Scientist
Carol;28;Product Manager
"""

# Generate the DataFrame definition
output = text_to_dict(text_data, delimiter=";")

# Print the DataFrame definition
print(output)
```
```
# OUTPUT
# This is the exact format that is returned by the function, which you can see 
# is immediately compatible with Python
data = {
    'Name': ['Alice', 'Bob', 'Carol'],
    'Age': [25, 30, 28],
    'Occupation': ['Software Engineer', 'Data Scientist', 'Product Manager'],
}
```
We could certainly think of ways to break this function by inserting whitespace and using whitespace delimiters, but this will convert many cases as is. The biggest pain point from my experience is going from Excel/csv to Python syntax.