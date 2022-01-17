try:
    x = 5
    y = 0

    z = x/y
except ZeroDivisionError:
    print("Division by a zero is not allowed")

finally:
    print("Done")