import collections
import os

stocks = dict(id=3005, name="神基", price=40.2, target=45)
stocks1 = dict([("id", 1537), ("name", "廣隆"), ("price", 143.5), ("target", 155)])
print(stocks)
print(stocks1)
print(stocks1['name'])
stocks1['price']=55
print(stocks1['price'])
stocks1['profit'] = "{0:.2%}".format(0.05)
stocks1['quantity'] = 2
print(stocks1)
stocks1.pop('quantity')
print(stocks1)
print(len(stocks1))
print(stocks1.items())
print(stocks1.keys())

print(stocks1.popitem())

d = {}.fromkeys("ABCD", 3)
print(d)
s = set("ACX")
print(s)
print(d.keys()-s)

files = {name: os.path.getsize(name) for name in os.listdir(".")}
print(files)
files = {name: os.path.getsize(name) for name in os.listdir(".") if os.path.isfile(name)}
print(files)

d1={}
for i, k in enumerate("ABCDE"):
    d1[k]=d1.get(k, i)
print(d1)
invert_d1 = {v:k for k,v in d1.items()}
print(invert_d1)

d2 = collections.OrderedDict([('z', -5), ('e', 17), ('k', 9)])
print(d2)


d2_list= list(sorted(d2.items(), key=lambda d: d[0]))
print(d2_list)
print(d2.popitem(last=false))
"""
stocks2 = stocks1.fromkeys(["id"])
print(stocks2)
for item in stocks1.items():
    print(item[0], item[1])
for key, value in stocks1.items():
    print(key, value)
for key in stocks1:
    print(key)
for key in stocks1.keys():
    print(key)
for value in stocks1.values():
    print(value)"""