"""
Problems

(3) From linux-etc-passwd.txt, show all of the different
    shells.
"""

# with open("samplefiles/linux-etc-passwd.txt") as shell_source:
#     shells = []
#     for each_line in shell_source:
#         each_line = each_line.strip()
#         if each_line and not each_line.startswith("#"):
#             split_line = each_line.split(sep=":")
#             shells.append(split_line[-1])
#     print(set(shells))

# with open("samplefiles/linux-etc-passwd.txt") as shell_source:
#     print(
#         set(
#             [
#                 last_item[-1]
#                 for last_item in [
#                     each_line.strip().split(":")
#                     for each_line in shell_source
#                     if each_line.strip() and not each_line.startswith("#")
#                 ]
#             ]
#         )
#     )

with open("samplefiles/linux-etc-passwd.txt") as shell_source:
    print(
        {
            each_line.strip().split(":")[-1]
            for each_line in shell_source
            if each_line.strip() and not each_line.startswith("#")
        }
    )
