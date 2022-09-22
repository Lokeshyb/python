from collections import defaultdict
test_list = []
a=int(input("No of elements in the list"))
for i in range(a):
    b=input()
    test_list.append(b)
print("The original list : " + str(test_list))
temp = defaultdict(list)
for ele in test_list:
    temp[str(sorted(ele))].append(ele)
res = list(temp.values())

# print result
print("The grouped Anagrams : " + str(res))
