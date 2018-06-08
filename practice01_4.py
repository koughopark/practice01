
def function(*args):
    count = 0
    total = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            if arg%3 == 0:
               count += 1
               total += arg
    return count, total
