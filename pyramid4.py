def pattern_four(rows):
    for i in range(rows + 1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print("")


if __name__ == "__main__":
    pattern_four(5)
