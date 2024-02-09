"""
Code for below pattern
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 
"""

def pattern_five(rows):
    for i in range(rows, 0, -1):
        for j in range(i, 0, -1):
            print(i, end=" ")
        print("")


if __name__ == "__main__":
    pattern_five(10)
