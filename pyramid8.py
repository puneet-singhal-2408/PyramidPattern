"""
Code for below pattern
        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5 
"""

def pattern_eight(rows):
    for i in range(1, rows + 1):
        num = 1
        for j in range(rows, 0, -1):
            if j > i:
                print(" ", end=" ")
            else:
                print(num, end=" ")
                num += 1
        print("")


if __name__ == "__main__":
    pattern_eight(5)
