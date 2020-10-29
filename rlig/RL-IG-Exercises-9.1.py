class ComputerInventory:
    def __init__(self):
        self.data = []
        self.index = 0

    def add_computers(self, *args):
        for one_computer in args:
            self.data.append(one_computer)

    def __iter(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

    def names(self):
        for one_computer in self.data:
            yield one_computer[0]

    def ip_addresses(self):
        for one_computer in self.data:
            yield one_computer[1]

    def by_os(self, os):
        if os not in ["Windows", "Mac", "Linux"]:
            raise ValueError(f"Bad OS, {os}")
        for one_computer in self.data:
            if one_computer[2] == os:
                yield one_computer


if __name__ == "__main__":
    ci = ComputerInventory()
    # fmt: off
    ci.add_computers(('server1', '1.1.1.1', 'Linux'),
                     ('server2', '2.2.2.2', 'Windows'),
                     ('server3', '3.3.3.3', 'Linux'),
                     ('laptop1', '4.4.4.4', 'Windows'),
                     ('laptop2', '5.5.5.5', 'Mac'))
    # fmt: on
    for one_name in ci.names():
        print(one_name)
    print(list(ci.by_os("Linux")))

