# fmt:off
my_gen = (one_line.split(" -")[0] 
         for one_line in open("mini-access-log.txt")
         if 'yahoo' in one_line.split()[-1] or 'google' in one_line.split()[-1])
# fmt:on
if __name__ == "__main__":
    print(next(my_gen))
    print(next(my_gen))
    print(next(my_gen))
    print(next(my_gen))
    print(next(my_gen))
    print(next(my_gen))
    print(next(my_gen))
