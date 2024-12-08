# 0x04. UTF-8 Validation

## Project Overview

The "0x04. UTF-8 Validation" project focuses on validating whether a given dataset adheres to the UTF-8 encoding scheme. This project requires you to apply bitwise operations, understand the UTF-8 encoding rules, and use Python programming skills to solve the problem.

### Key Concepts

- **Bitwise Operations**:
  - Understanding how to manipulate individual bits in Python, including operations like AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), and bit shifts (`<<`, `>>`).
  - Useful Python resources on bitwise operators: [Python Bitwise Operators](https://docs.python.org/3/library/operator.html#bitwise-operations).

- **UTF-8 Encoding Scheme**:
  - Familiarity with how UTF-8 encodes characters as one or more bytes.
  - Understanding the rules of UTF-8 encoding, such as how to determine the number of bytes for a character, and the specific bit patterns that indicate valid UTF-8 characters.
  - Resources to explore:
    - [UTF-8 Wikipedia](https://en.wikipedia.org/wiki/UTF-8)
    - [The Absolute Minimum Every Software Developer Must Know About Unicode and Character Sets](https://www.joelonsoftware.com/2003/10/01/the-absolute-minimum-every-software-developer-must-know-about-unicode-and-character-sets/)

- **Data Representation**:
  - Learn how to handle data at the byte level and interpret integers as byte sequences.
  - Using bitwise operations to validate the encoding of each byte.

- **List Manipulation in Python**:
  - Iterating over lists, accessing list elements, and understanding Python list comprehensions.
  - Refer to [Python Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) for more.

- **Boolean Logic**:
  - Applying logical operations to make decisions within the program.
  - Understanding how to structure conditionals using boolean expressions.

### Requirements

- **General**:
  - Allowed editors: `vi`, `vim`, `emacs`.
  - All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3.
  - All files should end with a newline.
  - The first line of all files should be exactly `#!/usr/bin/python3`.
  - Follow PEP 8 style guide (version 1.7.x).
  - All files must be executable.
  - A `README.md` file is mandatory at the root of the project folder.

### Tasks

1. Implement a function that validates whether a given dataset represents a valid UTF-8 encoding. Your solution should iterate through the dataset and apply bitwise checks to ensure the dataset matches UTF-8 encoding patterns.
2. Make sure that the function is efficient and handles edge cases, such as invalid byte sequences and incomplete character encodings.
