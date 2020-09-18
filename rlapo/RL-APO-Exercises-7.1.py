"""
(1) Create a class, FirstAvailableFile, that takes a variable number
    of filenames as arguments.  When used as a context manager, the
    class will return a file-like object providing a read-only
    connection to the first of the files that it was able to open
    successfully.

    When exiting from an instance of FirstAvailableFile, the opened
    file is then closed.

    Thus, we can say:

        with FirstAvailableFile('/etc/junkfile', '/etc/alsojunk', '/etc/passwd') as f:
            for one_line in f:
                print(one_line)

    We don't know ahead of time which file 'f' really refers to.  Assuming that the first
    two files don't exist, or that we don't have permission to read them, it's the third
    file that will actually be opened.  It'll also be closed when the "with" block exits.

(2) Implement the above as a decorator function, using contextlib.
"""


class FirstAvailableFile(object):
    def __init__(self, *args):
        self.filenames = args
        self.f = None

    def __enter__(self):
        for one_filename in self.filenames:
            try:
                self.f = open(one_filename, "r")
                return self.f
            except:
                return f"Unable to open {one_filename}"
        else:
            print("No filename was good.")
            return None

    def __exit__(self, *args):
        self.f.close()


def main():
    with FirstAvailableFile("/etc/passwd", "/etc/junkfile", "/etc/alsojunk") as foo:
        for one_line in foo:
            print(one_line)


if __name__ == "__main__":
    main()

