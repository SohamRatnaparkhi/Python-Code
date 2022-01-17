def pyramid_height():
    h = input('Height [1 - 8] : ')
    return int(h)

def main():
    height = pyramid_height()
    while (height <= 1 or height >= 8):
        height = pyramid_height()

    a = height - 1
    for row in range(0, height, 1):
        print (" " * (height - row) + '#' * (row + 1) + "  " + '#' * (row + 1))

main()