from Tree import *

list = []

for i in range(100):
  list.append(-1)
list.pop(0)
insert(list,10)
insert(list,30)
insert(list,40)
insert(list,50)
insert(list,60)
insert(list,80)
insert(list,70)
insert(list,2)
insert(list,1)

print_Tree(list)
print("----------------------")
remove(list,30)
print_Tree(list)
remove(list,10)
print("----------------------")
print_Tree(list)
insert(list, 11)
print("----------------------")
print_Tree(list)
insert(list, 15)
print("----------------------")
print_Tree(list)