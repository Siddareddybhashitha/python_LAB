#declaring the array size
i = int(input("Give array size:"))
print ("Give values:")
a = []
for k in range(0, i):
    value = int(input())
    a.append(value)
for k in range(1,i+1):
    print(list(combinations(a, k)))#printing the subsets in an array