"""
Code for below pattern:
1 1 1 1 1  
2 2 2 2  
3 3 3  
4 4  
5 
"""


def pattern_two(rows):
    b = 0
    for i in range(rows, 0, -1):
        b += 1
        for j in range(1, i + 1):
            print(b, end=" ")
        print(" ")


if __name__ == "__main__":
    pattern_two(5)
