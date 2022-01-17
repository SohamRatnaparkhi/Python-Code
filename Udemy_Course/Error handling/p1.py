try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("** operator cant be used in case of a string")