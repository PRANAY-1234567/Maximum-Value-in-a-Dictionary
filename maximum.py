marks = {"Ram": 80, "Shyam": 90, "Geeta": 85}

topper = max(marks, key=marks.get)
print(topper)
