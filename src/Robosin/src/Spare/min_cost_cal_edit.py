import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix



"----- parameter-default -----"
# indices = All          # 始点の指定
# method = 'auto'        # アルゴリズムの選択   
# directed = True        # 有向 or 無向
# unweighted = False     # 変の重みを加味するか


l = [[0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0]]


l = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

l = np.array(l)

# print(l)

Node_l = ["s", "A", "B", "C", "D", "E", "F", "O", "g"]

old = "s"
new = "B"
Node = Node_l.index(old)
NextNode = Node_l.index(new)
Arc = 6
row = Node
column = NextNode

if l[row][column] == 0 or Arc < l[row][column]:
    l[row][column] = Arc

# print(l)
# print("----------")

old = "A"
new = "B"
Node = Node_l.index(old)
NextNode = Node_l.index(new)
Arc = 2
row = Node
column = NextNode

if l[row][column] == 0 or Arc < l[row][column]:
    l[row][column] = Arc

# print(l)
# print("----------")

old = "B"
new = "C"
Node = Node_l.index(old)
NextNode = Node_l.index(new)
Arc = 5
row = Node
column = NextNode

if l[row][column] == 0 or Arc < l[row][column]:
    l[row][column] = Arc

# print(l)
# print("----------")



old = "C"
new = "E"
Node = Node_l.index(old)
NextNode = Node_l.index(new)
Arc = 7
row = Node
column = NextNode

if l[row][column] == 0 or Arc < l[row][column]:
    l[row][column] = Arc

# print(l)
# print("----------")


old = "E"
new = "D"
Node = Node_l.index(old)
NextNode = Node_l.index(new)
Arc = 5
row = Node
column = NextNode

if l[row][column] == 0 or Arc < l[row][column]:
    l[row][column] = Arc

print(l)
print("              |\n              |\n              v")

print("===== data x =====")

# Node_l = ["s", "A", "B", "C", "D", "E", "x",      "F", "O", "g"]
Node_l = ["s", "A", "B", "C", "D", "E", "F", "O", "g", "x"]

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
# print("Node : 0,  1,  2,  3,  4,  5,  X")
print("Node : 0,  1,  2,  3,  4,  5,  6,  7,  8,  X")
print(f" X : {shortest_path(np.array(l), indices=X, directed=False)}")

result = []
result = shortest_path(np.array(l), indices=X, directed=False)
print(f" X : {result}")
print(type(shortest_path(np.array(l), indices=X, directed=False)))
print(type(result))




"----- inf -> 0 に置換 -----"
"----- inf -> nan に置換 -----"
result[result == np.inf] = np.nan # 0
print(result)

import pandas as pd
# result = pd.Series([1, 2, 3, np.nan, 0, None], index=['A','B','C','D','E','F'])
result = pd.Series(result, index=Node_l)
result.dropna(inplace=True)
print(result)

print(result["A"])
print(result["E"])

Node = "x"
print(result[Node])

# result.drop(index=["A"], inplace=True)
# print(result)
# result.drop(index=["s"], inplace=True)
# print(result)
# result.drop(index=["D"], inplace=True)
# print(result)
# result.drop(index=["x"], inplace=True)
test1 = "A"
test2 = "x"
result.drop(index=[f"{test1}", f"{test2}"], inplace=True)
print(result)


# result.drop([30.0], inplace=True)
# print(result)

# move_cost_result = shortest_path(result, indices=X, directed=False) # bpで使う
# print(move_cost_result)