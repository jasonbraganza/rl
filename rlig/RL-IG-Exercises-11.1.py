"""
We're going to create a simple hashing service using two modules in
the Python standard library, "hashlib" and "base64".

From hashlib, we'll use the "md5" system for one-way hashing.  The way
it works is as follows:

    from hashlib import md5
    m = md5()
    m.update('this is a test'.encode())
    m.digest()

The base64 module works differently:

    from base64 import b64encode
    b64encode('this is a test'.encode())

Create two coroutines, "md5_service" and "b64_service". Each expects to be sent
a bytestring, and yields a bytestring -- the result of invoking the appropriate
code on its input.  When it receives a EndService exception, the coroutine should
exit.

Then create a "hash_service" coroutine. It expects to be sent either "md5" or "b64" (as strings).  It then connects us to that hash service, which takes any number of inputs (via send) until it gets an EndService exception.
"""

from hashlib import md5
from base64 import b64encode

# fmt: off
class EndService(BaseException):
    pass
# fmt: on


def md5_service():
    b = "Send a bytestring to digest: "
    while True:
        try:
            b = yield b
            m = md5()
            m.update(b)
            b = m.digest()
        except EndService as e:
            break


def b64_service():
    b = "Send a bytestring to digest: "
    while True:
        try:
            b = yield b
            b = b64encode(b)
        except EndService as e:
            break


def hash_service():
    s = "Send md5 or b64 to choose a service: "
    while True:
        s = yield s
        if s == "md5":
            yield from md5_service()
        elif s == "b64":
            yield from b64_service()
        else:
            break


if __name__ == "__main__":
    # m = md5_service()
    # next(m)
    # print(m.send(b"hello"))
    # print(m.throw(EndService))

    # b = b64_service()
    # next(b)
    # print(b.send(b"hello!"))
    # b.throw(EndService)

    h = hash_service()
    next(h)
    h.send("md5")
    print(h.send(b"hello"))
    h.throw(EndService)
    h.send("b64")
    print(h.send(b"hello"))
    h.throw(EndService)
