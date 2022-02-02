def pattern_seven():
    # N will be the number till where the reverse number to be printed.
    start = 1
    stop = 2
    curr_num = stop
    for row in range(2, 6):
        for i in range(start, stop):
            curr_num -= 1
            print(curr_num, end=" ")
        print("")
        start = stop
        stop += row
        curr_num = stop


if __name__ == "__main__":
    pattern_seven()
