list = [1,1,2,3,4,4,5,1,3,4,5,3,1]
newlist = []
start = 0

for i, val in enumerate(list):
    if val == 3:
        newlist.append(list[start:i+1])
        start = i + 1

print(newlist)


# list = [1,1,2,3,4,4,5,1]
# newlist = []
# a = list.index(3)
# newlist = list[:a]
# newlist.append(list[a:])
# print(newlist)

a = 5
b = 10
a, b = b, a 
print("a =", a)
print("b =", b)
