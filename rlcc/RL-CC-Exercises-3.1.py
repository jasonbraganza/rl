"""
Problems

(1) Ask the user to enter some integers, separated by
    spaces.  Sum the different numbers they enter.

    1 2 3   #  6
    1 2 3 1 2 3 # 6
"""

some_numbers = (input("Enter some numbers, seperated by spaces: ")).split()

print(sum(set([int(each_item) for each_item in some_numbers])))

