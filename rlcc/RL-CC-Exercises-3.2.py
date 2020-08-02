"""
Problems

(2) From the file nums.txt, sum all of the distinct numbers
    there.
"""

# with open("samplefiles/nums.txt") as numberlist:
#     listofnums = []
#     for each_line in numberlist:
#         each_line = each_line.strip()
#         if each_line:
#             listofnums.append(int(each_line))
#     print(sum(set(listofnums)))

with open("samplefiles/nums.txt") as numberlist:
    print(
        sum(
            set(
                int(unique_num)
                for unique_num in [
                    each_line.strip() for each_line in numberlist if each_line.strip()
                ]
            )
        )
    )

