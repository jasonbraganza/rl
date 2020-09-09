"""

(1) Create a Person class, which has two attributes, first_name and last_name.
    Fill out the methods, so that you can compare two people, and that
    the ordering will be first by last_name and then by first_name.

"""
from functools import total_ordering


@total_ordering
class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __eq__(self, some_person):
        if hasattr(some_person, "last_name") and hasattr(some_person, "first_name"):
            return (self.first_name == some_person.first_name) and (
                self.last_name == some_person.last_name
            )
        else:
            return False

    def __lt__(self, some_person):
        if hasattr(some_person, "last_name") and hasattr(some_person, "first_name"):
            if self.last_name == some_person.last_name:
                return self.first_name < some_person.first_name
            else:
                return self.last_name < some_person.last_name
        else:
            raise TypeError("Sorry, cannot compare these two things")

    def __repr__(self):
        return f"Person, {self.first_name} {self.last_name}"


def main():
    p1 = Person("Mario", "Braganza")
    p2 = Person("Anne", "Frank")
    p3 = Person("Octavia", "Butler")
    p4 = Person("Frida", "Kahlo")

    people = [p1, p2, p3, p4]

    print(p1 == p1)
    print(p2 >= p3)
    print(sorted(people))


if __name__ == "__main__":
    main()
