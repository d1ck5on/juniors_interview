from functools import wraps
from inspect import getfullargspec


def strict(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        fspec = getfullargspec(func)
        fargs = fspec.args
        fannotations = fspec.annotations
        for i, farg in enumerate(fargs):
            if i < len(args):
                received_arg = args[i]
            else:
                received_arg = kwargs[farg]
            if not isinstance(received_arg, fannotations[farg]):
                raise TypeError
        return func(*args, **kwargs)
    return wrapper
