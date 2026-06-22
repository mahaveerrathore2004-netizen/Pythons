#dictionary iteration
"""
dict = {
    "name": "Mahaveer Singh",
    "age": 21,
    "city": "Sirohi"
}
print(dict["name"])
print(dict["age"])
print(dict)
"""

#nested dictionary
"""
info = {
    "name": "Mahaveer Singh",
    "age": 21,
    "address": {
        "city": "Sirohi",
        "state": "Rajassthan"
    }
}
print(info)
print(info["name"])
print(info["address"]["city"])

print(info.keys())
print(info.values())
print(info.items())
print(list(info.keys()))
print(len(list(info.keys()))) 
print(info.get("key"))
info.update({"name": "Mahi"})
print(info)
"""

#set in python
"""
nums = {1, 2, 3, 4, 5}
print(nums)

set = {1, 2, 2, 2}
print(set)
"""

#methods in set
"""
collection = set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(4)
print(collection)
collection.clear()
print(collection)

#collection.pop()
#print(collection)

collection1 = {"a", "b", "c"}
print(collection1.pop())
print(collection1.pop())
print(collection1.pop())
"""

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))