
fruits=["apple", "orange", "guava", "Melon", "apple", "lichi"]
test=set("apple")
test1=set("aple")
fruits_set=set(fruits)

winter_fruits= fruits_set - {"guava", "Melon", "lichi"}
winter_fruits.discard("Jujube")

codes = { sex + size + color for sex in "MF" for size in "SMLX" for color in "BGW" if not (sex == "F" and size in "LX")}

print(codes)
print(type(codes))