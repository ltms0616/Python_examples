
"""unpack test of list, tuple and set"""
def caculate_sum(*args):
    sum = 0
    try:
        for i in args:
            sum += i
        return sum
    except ValueError:
        print("wrong input")
        return 0

nums1 = [5, 6, 7, 8, 9]
sum = caculate_sum(*nums1)
print("the sum of nums1 is {0:d}".format(sum))

nums2 = (10, 11, 12, 13, 14)
sum = caculate_sum(*nums2)
print("the sum of nums2 is {0:d}".format(sum))

num3 = {15, 16, 17, 18, 19}
sum = caculate_sum(*num3)
print("the sum of num3 is {0:d}".format(sum))

"""unpack test of dict"""

def updateEmployeeStatus(**args):
    if 'name' in args.keys():
        print("The employee name is {0}". format(args['name']))
    if 'age' in args.keys():
        print("Age is {0}".format(args['age']))
    if 'addr' in args.keys():
        print("Address is {0}". format(args['addr']))

data = {'name':'Moore', 'age':18, 'addr':'taipe'}
updateEmployeeStatus(**data)