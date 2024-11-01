#
#
# numbers = [5,2,1,7,4]
# numbers2 = numbers.copy()
# numbers.append(13)
# numbers.insert(0,10)
# # numbers.remove(5)
# #  numbers.clear()
# # numbers.pop()
# # numbers.index(5)
# print(50 in numbers)
#
# print(numbers.count(2))
# numbers.sort()
# print(numbers)
# print(numbers2)




n = [1,2,3,4,5,6,1,2,3,4,7,8,9,0]
uniques = []
for number in n:
    if number not in uniques:
        uniques.append(n)
print(uniques)



