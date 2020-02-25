import sys

def lst_find(lst, target):
    try:
        index = lst.index(target)
    except ValueError:
        index = -1
    return index

def read_data(filename):
    lines = []
    fh = None
    try:
        fh = open(filename, encoding="utf8")
        for line in fh:
            if line.rstrip():
                lines.append(line)
    except (IOError, OSError) as err:
    #except EnvironmentError as err   //EnvironmentError is base class of IOError and OSError
        print(err)
        return []
    finally:
        if fh is not None:
            fh.close()
    return lines

cars = "benz"
index = lst_find(cars, "x")
print(index)


