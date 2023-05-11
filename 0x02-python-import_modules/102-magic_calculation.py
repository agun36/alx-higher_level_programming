#!/usr/bin/python3

import importlib.util
def magic_calculation(a, b):
    c = 0
    if a < b:
        spec = importlib.util.find_spec("magic_calculation_102")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        c = module.add(a, b)
        for i in range(4, 7):
            c = module.add(c, i)
        return c
    else:
        return magic_calculation_102.sub(a, b)
