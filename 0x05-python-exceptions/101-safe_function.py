#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        solution = fct(*args)
        return solution
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return None
