def StringEquals(x, y):
    assert isinstance(x, str)
    assert isinstance(y, str)
    return x == y


class Fail(Exception):
    def __init__(self, label, message):
        self.label = label
        self.message = message

    def __str__(self):
        return f'{self.label}: {self.message}'


def parallel(*funs):
    return [f() for f in funs]