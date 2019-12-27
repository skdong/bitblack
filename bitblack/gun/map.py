import contextlib
import six

a = [i for i in range(10)]
print(a)
b = map(lambda i: i+1, a)
print(list(b))

c = filter(lambda i: i>5, a)

@contextlib.contextmanager
def test():
    print("before")
    yield
    print("after")


with test():
    print("cc")
