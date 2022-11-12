import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix


# l = [[0, 1, 2, 0],
#      [0, 0, 0, 1],
#      [3, 0, 0, 3],
#      [0, 0, 0, 0]]



# a = np.array(l)

# print("----- 有向グラフ -----")
# print(shortest_path(a))

# print("----- 疎行列 -----")
# csr = csr_matrix(l)
# print(csr)

# print("----- 有向グラフ -----")
# print(shortest_path(csr))

# print("----- 始点が決まっている時は指定可能 -----")
# print(shortest_path(csr, indices=[0,1,2,3]))

# print("----- 始点 = 0の場合 -----")
# print(shortest_path(csr, indices=0))

# print("----- 無向グラフ -----")
# print(shortest_path(a, directed=False))


# print("----- 無向グラフ 他手法 -----")
# l_ud = [[0, 1, 2, 0],
#         [1, 0, 0, 1],
#         [2, 0, 0, 3],
#         [0, 1, 3, 0]]

# print(shortest_path(np.array(l_ud)))
# print(shortest_path(csr_matrix(l_ud)))



"----- parameter-default -----"
# indices = All          # 始点の指定
# method = 'auto'        # アルゴリズムの選択   
# directed = True        # 有向 or 無向
# unweighted = False     # 変の重みを加味するか



# print("----- data 1 -----")
# print("   0,  1,  2,  3,  4,  5")
# l_test = [[0, 0, 6, 0, 0, 0],
#           [0, 0, 2, 0, 0, 0],
#           [6, 2, 0, 5, 0, 0],
#           [0, 0, 5, 0, 0, 7],
#           [0, 0, 0, 0, 0, 5],
#           [0, 0, 0, 7, 5, 0]]


# print(shortest_path(np.array(l_test)))

# print("----- 始点 = 5 の場合 -----")
# print("    0,  1,  2,  3,  4,  5")
# print(f"5:{shortest_path(np.array(l_test), indices=5)}")



# print("----- data 2 -----")
# print("   0,  1,  2,  3,  4,  5")
# l_test_2 = [[0, 0, 6, 0, 0, 0],
#             [0, 0, 2, 0, 0, 0],
#             [0, 0, 0, 5, 0, 0],
#             [0, 0, 0, 0, 0, 7],
#             [0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 5, 0]]

# #    s  A  B  C  D  E
# # s [0, 0, 6, 0, 0, 0]
# # A [0, 0, 2, 0, 0, 0]
# # B [0, 0, 0, 5, 0, 0]
# # C [0, 0, 0, 0, 0, 7]
# # D [0, 0, 0, 0, 0, 0]
# # E [0, 0, 0, 0, 5, 0]

# # s(0) - B(2) : 6
# # A(1) - B(2) : 2
# # B(2) - C(3) : 5
# # C(3) - E(5) : 7
# # E(5) - D(4) : 5
# print("----- 疎行列 -----")
# csr = csr_matrix(l_test_2)
# print(csr)


# print("----- 有向グラフ -----")
# print(shortest_path(np.array(l_test_2)))
# print("----- 無向グラフ -----")
# print(shortest_path(np.array(l_test_2), directed=False))

# print("----- 始点 = 5 の場合 -----")
# print("    0,  1,  2,  3,  4,  5")
# print(f"5:{shortest_path(np.array(l_test_2), indices=5, directed=False)}")




print("===== data 3 =====")



# l = [[0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0]]

l = [[0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0]]

l = np.array(l)

print(l)

# # s(0)-B(2) : 6
# # if l[row][column] == 0 or data <= l[row][column]: lが0または、新しい距離が以前のものより小さい場合格納する
# l[0][2] = 6
# l[1][2] = 2
# l[2][3] = 5
# l[3][5] = 7
# l[5][4] = 5

# print(l)


# # for row, column in zip(Node, NextNode):
# #     data = [row, column]
# #     if l[row][column] == 0 or data < l[row][column]:

Node_l = ["s", "A", "B", "C", "D", "E", "F", "O", "g"]

old = "s"
new = "B"
Node = Node_l.index(old)
NextNode = Node_l.index(new)
Arc = 6
# for row, column in zip(Node, NextNode):
row = Node
column = NextNode

if l[row][column] == 0 or Arc < l[row][column]:

    l[row][column] = Arc

print(l)
print("----------")

old = "A"
new = "B"
Node = Node_l.index(old)
NextNode = Node_l.index(new)
Arc = 2
# for row, column in zip(Node, NextNode):
row = Node
column = NextNode

if l[row][column] == 0 or Arc < l[row][column]:

    l[row][column] = Arc

print(l)
print("----------")

old = "B"
new = "C"
Node = Node_l.index(old)
NextNode = Node_l.index(new)
Arc = 5
# for row, column in zip(Node, NextNode):
row = Node
column = NextNode

if l[row][column] == 0 or Arc < l[row][column]:

    l[row][column] = Arc

print(l)
print("----------")



old = "C"
new = "E"
Node = Node_l.index(old)
NextNode = Node_l.index(new)
Arc = 7
# for row, column in zip(Node, NextNode):
row = Node
column = NextNode

if l[row][column] == 0 or Arc < l[row][column]:

    l[row][column] = Arc

print(l)
print("----------")


old = "E"
new = "D"
Node = Node_l.index(old)
NextNode = Node_l.index(new)
Arc = 5
# for row, column in zip(Node, NextNode):
row = Node
column = NextNode

if l[row][column] == 0 or Arc < l[row][column]:

    l[row][column] = Arc

print(l)

print("----- 無向グラフ -----")
# print(shortest_path(np.array(l), directed=False))
print(shortest_path(l, directed=False))

print("----- 始点 = 5 の場合 -----")
print("    0,  1,  2,  3,  4,  5")
print(f"5:{shortest_path(np.array(l), indices=5, directed=False)}")





# # move_cost = 7 # 10
# # test = shortest_path(l, indices=5, directed=False)

# # # test = np.append(test, move_cost)
# # test += move_cost
# # test = np.append(test, 0)

# import copy
# test = copy.copy(l)
# # [0, 0, 0, 0, 0, 0],
# # [0, 0, 0, 0, 0, 0],
# # [0, 0, 0, 0, 0, 0],
# # [0, 0, 0, 0, 0, 0],
# # [0, 0, 0, 0, 0, 0],
# # [0, 0, 0, 0, 0, 0]]
# # l = [[0, 0, 0, 0, 0, 0, 0],
# #      [0, 0, 0, 0, 0, 0, 0],
# #      [0, 0, 0, 0, 0, 0, 0],
# #      [0, 0, 0, 0, 0, 0, 0],
# #      [0, 0, 0, 0, 0, 0, 0],
# #      [0, 0, 0, 0, 0, 0, 0],
# #      [0, 0, 0, 0, 0, 0, 0]]
# # print(l)

# # print(l+test)
# c0 = [0, 0, 0, 0, 0, 0]
# c1 = [0, 0, 0, 0, 0, 0]
# np.insert(l, 5, c0, axis=0)
# np.insert(l, 5, c1, axis=1)

# print(l)


# # print(f"5:{test}")


print("\n\n\n===== data x =====")

Node_l = ["s", "A", "B", "C", "D", "E", "x",      "F", "O", "g"]

old = "D" # "E" # 最後に一致したNode
# old = "C"

new = "x" # 発見できずに戻ると決めた場所

Node = Node_l.index(old)
# NextNode = Node_l.index(new)
X = Node_l.index(new)
Arc = 7
row = Node
# column = NextNode
column = X

if l[row][column] == 0 or Arc < l[row][column]:
    l[row][column] = Arc

print(l)

print("----- 無向グラフ -----")
print(shortest_path(l, directed=False))

print("----- 始点 = x の場合 -----")
print("Node : 0,  1,  2,  3,  4,  5,  X")
print(f" X : {shortest_path(np.array(l), indices=X, directed=False)}")