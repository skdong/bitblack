import functools

class Gun(object):
    def __init__(self, before="be", after="af"):
        self.before = before
        self.after = after

    def show_gun(self, f):
        @functools.wraps(f)
        def inner(*args , **kwargs):
            print(self.before)
            f(*args, **kwargs)
            print(self.after)
        return inner


def show_gun(msg):
    def show_message(f):
        def inner(*args, **kwargs):
            print("before "+msg)
            f(*args, **kwargs)
            print("after "+msg)
        return inner
    return show_message
    
gun = Gun()

@show_gun("msg")
def test(message="default"):
    print(message)

test()
print(test.__name__)