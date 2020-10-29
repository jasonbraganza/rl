"""
Define a generator function, by_chunk, that takes two arguments:

    - filename, the name of a text file
    - when_to_stop, a sequence of strings

The generator will return the contents of the text file, one chunk at
a time, where "chunk" is defined as text that ends with one of the
elements of when_to_stop.  (when_to_stop can be a string, but if you
want to have a multi-character stop, you'll need to use a tuple of
strings.)

So if you want to get the contents of a text file, one sentence at a
time, you could say:

    by_chunk('myfile.txt', '.?!')
"""


def by_chunk(filename, when_to_stop):
    text = open(filename).read()
    while True:

        indexes = [
            text.find(one_string) for one_string in when_to_stop if one_string in text
        ]

        if not indexes:
            yield text
            return

        index = min(indexes) + 1

        output = text[:index]
        text = text[index:]
        yield output


if __name__ == "__main__":
    for one_chunk in by_chunk("test.txt", "!.?"):
        print(one_chunk, end="*")
