"""
Code for below pattern
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 
"""

def pattern_six(rows):
    for i in range(rows, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print("")


if __name__ == "__main__":
    pattern_six(5)
