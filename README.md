🏆 Find the Key with Maximum Value in a Dictionary (Python)


📌 Description

This program finds the student with the highest marks from a dictionary.
The dictionary contains student names as keys and their marks as values.

🧩 Problem Statement

Given a dictionary:

{"Ram": 80, "Shyam": 90, "Geeta": 85}


Find the student who scored the highest marks.

✅ Code
marks = {"Ram": 80, "Shyam": 90, "Geeta": 85}

topper = max(marks, key=marks.get)
print(topper)

🧠 Explanation

marks is a dictionary where:

Key → Student name

Value → Marks

max() finds the key with the maximum value

key=marks.get tells Python to compare dictionary values instead of keys

So, the student with the highest marks is returned.

🖨 Example Output
Shyam

🛠 Concepts Used

Dictionaries

max() function

key parameter

.get() method

🎯 Use Cases

Finding top scorer in a class

Ranking systems

Interview preparation

Dictionary value analysis

🚀 Possible Improvements

Print both name and marks

Handle ties (multiple toppers)

Take input from user

Find minimum marks student

👨‍💻 Author

Pranay Jadhao

<img width="532" height="647" alt="image" src="https://github.com/user-attachments/assets/ea994e90-8c0f-4be7-a53a-030c75891ee6" />
