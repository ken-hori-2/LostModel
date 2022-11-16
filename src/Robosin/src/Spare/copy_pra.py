
import copy

list1 = [[1, 2, 3], [4, 5, 6]]
# list2 = list1.copy()
list2 = copy.copy(list1)
list3 = copy.deepcopy(list1)

# list1の要素の値を変更する
list1[0][0] = 100

# それぞれの変数の内容を表示する
print("list1:", list1)
print("list2:", list2)
print("list3:", list3)