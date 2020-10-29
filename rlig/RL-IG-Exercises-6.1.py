def read_n(fname, n):
    f = open(fname)
    while True:
        output = ""
        for i in range(n):
            output += f.readline()
        if output:
            yield output
            print("-" * 30)
        else:
            break


def now_read():
    for one_chunk in read_n("/home/jess/code/rl/README.md", 2):
        print(one_chunk)


if __name__ == "__main__":
    now_read()
