import time

from bst import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

search_tree = BinarySearchTree(None)

for name in names_1:
    if search_tree.value == None:
        search_tree.value = name
    else:
        search_tree.insert(name)


for name in names_2:
    if search_tree.contains(name):
        duplicates.append(name)



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"Mvp runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


duplicates2 = set(names_1).intersection(names_2)

end_time = time.time()
print (f"{len(duplicates2)} duplicates:\n\n{', '.join(duplicates2)}\n\n")
print (f"Stretch runtime: {end_time - start_time} seconds")