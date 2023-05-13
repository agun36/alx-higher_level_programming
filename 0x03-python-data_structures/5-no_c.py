#!/usr/bin/env python3
def no_c(mystr):
    mystr_2 = mystr.translate({ord("c"):None})
    mystr_2 = mystr_2.translate({ord("c"):None})
    return mystr_2
