def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first integer.
        b (int or float): The second integer. Defaults to 98.


    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer.

    """

   def add_integer(a, b):
    """Return the addition of two numbers."""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
