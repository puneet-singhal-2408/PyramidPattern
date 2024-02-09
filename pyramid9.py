"""
Code for below pattern
        1 
      2 1 2 
    3 2 1 2 3 
  4 3 2 1 2 3 4 
5 4 3 2 1 2 3 4 5
"""

def pattern_nine(rows):
    for i in range(1, rows + 1):
        for j in range(rows, 0, -1):
            if j > i:
                print(" ", end=" ")
            else:
                print(j, end=" ")
        k = 2
        while i >= k:
            print(k, end=" ")
            k += 1
        print("")


if __name__ == "__main__":
    pattern_nine(5)
