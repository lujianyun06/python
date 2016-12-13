
def find_lines_func2(filename):
    file = open(filename)
    lines = file.readlines()
    return len(lines)
    pass