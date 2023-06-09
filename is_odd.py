def is_odd(x):
    """
    Checks if input is an odd integer

    Returns True if input is an odd integer
    Returns False if input is not an odd integer
    Raises Error if input is not an integer
    """
    if not isinstance(x, int):
        raise TypeError('x must be an integer')



    return (x % 2) != 0









assert is_odd.__doc__ is not None

has_failed = False
try:
    is_odd('bla')
except TypeError:
    has_failed = True
assert has_failed
assert is_odd(1) is not None
assert is_odd(2) is False
