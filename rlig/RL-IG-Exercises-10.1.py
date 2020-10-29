"""

Write a coroutine that translates English-language sentences into Pig Latin. It can use the following function:

def pl_sentence(s):
    output = []
    for one_word in s.split():
        if one_word[0] in 'aeiou':
            output.append(one_word + 'way')
        else:
            output.append(one_word[1:] + one_word[0] + 'ay')
    return ' '.join(output)

It should be possible to say:

    g = pig_latin()
    next(g)
    g.send('this is a test')  # we get back 'histay isway away esttay'

The coroutine will exit when it gets a EndService exception, which you should write.

"""


def pl_sentence(s):
    output = []
    for one_word in s.split():
        if one_word[0] in "aeiou":
            output.append(one_word + "way")
        else:
            output.append(one_word[1:] + one_word[0] + "ay")
    return " ".join(output)


class EndService(Exception):
    pass


def pig_latin():
    s = "Enter a sentence to translate: "
    while True:
        try:
            s = yield s
            s = pl_sentence(s)
        except EndService as e:
            break


if __name__ == "__main__":
    g = pig_latin()
    next(g)
    print(g.send("this is a test"))
    print(g.send("this is another test"))
    print(g.throw(EndService))
