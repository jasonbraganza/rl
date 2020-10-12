""" 
Write an iterator, ByWord, which takes both a string and an optional
integer argument. The iterator should return each word from the
string (separated by whitespace).

However, if the optional integer argument is provided, then the
next word should only be returned if it's longer than the argument.

(Don't worry about memory usage in your solution; we will assume that
the string can safely exist in memory.)

Use a helper class in implementing your solution.

bw = ByWord('This is a test of my system', 3)

for one_word in bw:
    print(one_word)

This
test
system
"""


class ByWord:
    def __init__(self, s, min_length=0):
        self.s = s.split()
        self.min_length = min_length
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.index >= len(self.s):
                raise StopIteration
            value = self.s[self.index]
            self.index += 1
            if len(value) >= self.min_length:
                break
        return value


if __name__ == "__main__":
    bw = ByWord("This is a test of my system")

    for one_word in bw:
        print(one_word)
