import sys

def find_target(table, target):
    found = False
    for row, record in enumerate(table):
        for column, field in enumerate(record):
            for index, item in enumerate(column):
                if item == target:
                    found = True
                    break
            if found:
                break
        if found:
            break
    if found:
        print("found at {0} {1} {2}".format(row, column,index))
    else:
        print("not found")


def find_target(table, target):
    class FoundException(Exception): pass
    try:
        for row, record in enumerate(table):
            for column, field in enumerate(record):
                for index, item in enumerate(column):
                    if item == target
                        raise FoundException
    except FoundException:
        print("found at {0} {1} {2}".format(row, column, index))
    else:
        print("not found")

