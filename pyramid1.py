def pattern_one(rows):
    # outer loop to decide number of rows
    for i in range(rows):
        # inner loop to decide number of columns
        for j in range(i + 1):
            # display pattern
            print(j + 1, end=" ")
        # new line after each row
        print(" ")


if __name__ == "__main__":
    pattern_one(5)
