import collections

Tea = collections.namedtuple("Tea", "Id Type size price")
catalog = []
tea1 = Tea(3, "Milk", "Large", 50)
tea2 = Tea(4, "Herb", "Small", 30)
catalog.append(Tea(1, "Red", "Medium", 45))
catalog.append(Tea(2, "Green", "Medium", 40))

for prod in catalog:
    print("Type:{0}, Size:{1}, Price:{2}".format(prod.Type, prod.size, prod.price))

for prod in catalog:
    print("Type:{0.Type}, Size:{0.size}, Price:{0.price}".format(prod))

for prod in catalog:
    print("Type:{Type}, Size:{size}, Price:{price}".format(**prod._asdict()))

print(len(tea1))
print(len(catalog))
