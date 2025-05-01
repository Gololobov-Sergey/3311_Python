import random
list_1 = []
for i in range(10):
    list_1.append(random.randint(0, 10))

print(list_1)

# count = 0
# for el in list_1:
#     if el == 0:
#         count = count + 1
#
# print(count)
# print(list_1.count(0))

max_el = list_1[0]
min_el = list_1[0]

for i in range(int(len(list_1)/2)):
    if list_1[i] > max_el:
        max_el = list_1[i]
    if list_1[i] < min_el:
        min_el = list_1[i]

print(max_el, min_el)
print(max(list_1))
print(min(list_1))