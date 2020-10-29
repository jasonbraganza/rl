def words(length, letters):
    letters_set = set(letters)
    # fmt: off
    return (
        one_word.strip()
        for one_word in open("words.txt")
        if len(one_word.strip()) == length 
        if set(one_word.strip()) <= letters_set
    )
    # fmt: on


# fmt: off
agen = (one_word
    for one_line in open('alice-in-wonderland.txt')
    for one_word in one_line.split()
    if len(one_word)>=6)
# fmt: on

if __name__ == "__main__":
    # w = words(4, "alice")
    # print(next(w))
    # print(next(w))
    # print(next(w))
    # print(next(w))
    # print(next(w))
    # print(next(w))
    print(next(agen))
    print(next(agen))
    print(next(agen))
    print(next(agen))

