def student_info(name, age, major):
    print(f"{name}, {age} years old, majoring in {major}")

# Positional arguments
student_info("Delta", 20, "Computer Science")

# Keyword arguments
student_info(major="Information Systems", name="Echo", age=21)