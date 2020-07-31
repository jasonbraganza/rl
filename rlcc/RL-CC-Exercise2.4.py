# (4) Create, from linux-etc-passwd.txt, a list of tuples
#     in which each tuple is (username, user_id) .
#     username is field index 0, user_id is field index 2


user_id = [tuple(one_line.split(":")[:3 :2])
           for one_line in open("samplefiles/linux-etc-passwd.txt")
           if one_line.strip() and not one_line.startswith("#")]
print(user_id)

‘’