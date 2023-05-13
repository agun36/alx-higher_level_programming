#!/usr/bin/env python3
def no_c(my_string):
    """
    Removes all chter c and C from a string
    ...
    Parameters
    ----------
    my_string : str
        The stri to remove 'Cc' from
    Return:
        The new string
    """
    return re.sub(r"[cC]", "", my_string)
