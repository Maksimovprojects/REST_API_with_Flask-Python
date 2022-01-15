def divide(dividend, divisor):
    return dividend/divisor


students = [{"name": "Bob", "grades": [75, 90]},
            {"name": "Rolf", "grades": []},
            {"name": "Jen", "grades": [100, 90]},
            ]
try:
    for student in students:
        name = student['name']
        grades = student['grades']
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}.")
except Exception as e:                          # will be printed if error ZeroDivisionError is happened
    print(f"ERROR: {name} has no grades!")
    print(e)
else:
    print("-- All stident average calculated --")   # will be printed if ERROR NOT caused but, try isn't executed
finally:
    print("-- End of student average calculation --")   # will be printed anytime


