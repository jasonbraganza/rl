"""

(1) Create a StateMachine descriptor class, which takes any number of
    unique string arguments, representing unique, ordered states.

    Retrieving the descriptor's value will return the current state.
    (The descriptor will start in the initial state.)

    Setting it (with any value at all) with bump it toward the next
    state -- unless you're already at the final state, in which case
    you'll get a ReachedFinalStateError exception.

"""


from collections import defaultdict


class ReachedFinalStateError(Exception):
    pass


class StateMachine(object):
    def __init__(self, *args):
        self.states = args
        self.index = defaultdict(int)

    def __get__(self, host_instance, host_class):
        if host_instance:
            return self.states[self.index[host_instance]]
        else:
            raise TypeError("You must use an instance")

    def __set__(self, host_instance, new_value):
        self.index[host_instance] += 1

        if self.index[host_instance] >= len(self.states):
            raise ReachedFinalStateError("You reached the end")


class CompanyTask(object):
    state = StateMachine("dev", "qa", "production")


def main():
    ct = CompanyTask()
    print(ct.state)
    ct.state = 2
    print(ct.state)
    ct.state = 1
    print(ct.state)
    ct.state = 1
    print(ct.state)


if __name__ == "__main__":
    main()
