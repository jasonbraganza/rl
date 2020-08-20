"""
Problem

(1) Assume that we can calculate a word's "score" by
    adding the scores of each letter -- where a=1, b=2,
    c=3, and so forth (ignoring case).  Ask the user for
    a sentence, and then create a dict based on that
    sentence, in which the keys are the words and the
    values are the "scores" for the words.

    bad cab   # output will be {'bad':4, 'cab':6} 

    ord('a') # 97 == ASCII value
"""


def word_score(word):
    score = sum([ord(letter) for letter in word]) - 96
    return score


def main():
    get_a_line = input("Enter a phrase: ").lower().split()
    word_score(get_a_line[0])


if __name__ == "__main__":
    main()

