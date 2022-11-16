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

# old = "s"
# new = "B"
# Node = Node_l.index(old)
# NextNode = Node_l.index(new)
# Arc = 6
# row = Node
# column = NextNode

# if l[row][column] == 0 or Arc < l[row][column]:
#     l[row][column] = Arc

# # print(l)
# # print("----------")

# old = "A"
# new = "B"
# Node = Node_l.index(old)
# NextNode = Node_l.index(new)
# Arc = 2
# row = Node
# column = NextNode

# if l[row][column] == 0 or Arc < l[row][column]:
#     l[row][column] = Arc

# # print(l)
# # print("----------")

# old = "B"
# new = "C"
# Node = Node_l.index(old)
# NextNode = Node_l.index(new)
# Arc = 5
# row = Node
# column = NextNode

# if l[row][column] == 0 or Arc < l[row][column]:
#     l[row][column] = Arc

# # print(l)
# # print("----------")



# old = "C"
# new = "E"
# Node = Node_l.index(old)
# NextNode = Node_l.index(new)
# Arc = 7
# row = Node
# column = NextNode

# if l[row][column] == 0 or Arc < l[row][column]:
#     l[row][column] = Arc

# # print(l)
# # print("----------")


# old = "E"
# new = "D"
# Node = Node_l.index(old)
# NextNode = Node_l.index(new)
# Arc = 5
# row = Node
# column = NextNode

# if l[row][column] == 0 or Arc < l[row][column]:
#     l[row][column] = Arc

# print(l)
# print("              |\n              |\n              v")

# print("===== data x =====")

# # Node_l = ["s", "A", "B", "C", "D", "E", "x",      "F", "O", "g"]
Node_l = ["s", "A", "B", "C", "D", "E", "F", "O", "g", "x"]

# old = "D" # "E" # 最後に一致したNode
# # old = "C"

# new = "x" # 発見できずに戻ると決めた場所

# Node = Node_l.index(old)
# # NextNode = Node_l.index(new)
# X = Node_l.index(new)
# Arc = 7
# row = Node
# # column = NextNode
# column = X

# if l[row][column] == 0 or Arc < l[row][column]:
#     l[row][column] = Arc

# print(l)

# print("----- 無向グラフ -----")
# print(shortest_path(l, directed=False))

# print("----- 始点 = x の場合 -----")
# # print("Node : 0,  1,  2,  3,  4,  5,  X")
# print("Node : 0,  1,  2,  3,  4,  5,  6,  7,  8,  X")
# print(f" X : {shortest_path(np.array(l), indices=X, directed=False)}")

# result = []
# result = shortest_path(np.array(l), indices=X, directed=False)
# print(f" X : {result}")
# print(type(shortest_path(np.array(l), indices=X, directed=False)))
# print(type(result))




# "----- inf -> 0 に置換 -----"
# "----- inf -> nan に置換 -----"
# result[result == np.inf] = np.nan # 0
# print(result)

# import pandas as pd
# # result = pd.Series([1, 2, 3, np.nan, 0, None], index=['A','B','C','D','E','F'])
# result = pd.Series(result, index=Node_l)
# result.dropna(inplace=True)
# print(result)

# print(result["A"])
# print(result["E"])

# Node = "x"
# print(result[Node])

# # result.drop(index=["A"], inplace=True)
# # print(result)
# # result.drop(index=["s"], inplace=True)
# # print(result)
# # result.drop(index=["D"], inplace=True)
# # print(result)
# # result.drop(index=["x"], inplace=True)
# test1 = "A"
# test2 = "x"
# result.drop(index=[f"{test1}", f"{test2}"], inplace=True)
# print(result)


# # result.drop([30.0], inplace=True)
# # print(result)

# # move_cost_result = shortest_path(result, indices=X, directed=False) # bpで使う
# # print(move_cost_result)


print(l)
import pandas as pd
import copy
# test = pd.Series(l, index=Node_l)
# print(test)

l = {"s":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     "A":[10, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     "B":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     "C":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     "D":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     "E":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     "F":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     "O":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     "g":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     "x":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
     
df = pd.DataFrame(l)

print(df.T)

print(df["A"])

# test = pd.Series(df.T, index=Node_l)
# print(test)


old = "A"
new = "B"
Node = Node_l.index(old)
NextNode = Node_l.index(new)
Arc = 2
row = Node
column = NextNode

# if l[row][column] == 0 or Arc < l[row][column]:
#     l[row][column] = Arc
# if df[row][column] == 0 or Arc < df[row][column]:
#     df[row][column] = Arc
# if df[row][column] == 0 or Arc < df[row][column]:
df["A"] = Arc


print("----------")
old_2 = "B"
Node = Node_l.index(old_2)

df[old_2][NextNode] = 1
print(df.T)

df[old_2] = 7
print(df.T)

# df[1] = 1
# print(df.T)

# # df.drop(index=["D"], inplace=True)
# df.drop(index=Node, inplace=True)
# print(df.T)

# df.set_index("Product ID",inplace=True)
# print(df.T)




l_2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
     
# df = pd.DataFrame(l_2, # こっちでもいい
df = pd.DataFrame(np.array(l_2),
                  columns=[Node_l],
                  index=[Node_l])

print(df)

old = "A"
new = "B"

# df[old][new] = 1
# print(df)

df.loc[old,new] = 100
print(df)

old = "B"
new = "x"
df.loc[old,new] = 7
print(df)



df_copy = copy.copy(df)
df_copy = copy.deepcopy(df) # 基本、行列はこっちらしいがどっちでもできている

test1 = "A"
test2 = "O" # "x"
# # df_copy.drop(index=[f"{test1}", f"{test2}"], inplace=True)
# # df_copy.drop(index=[f"{test1}","B","C","D","E"], axis=0, inplace=True)

# # df_copy._drop_axis(labels="x", axis="x", level=1, errors=1)
# print(df_copy.drop(["s","A"], axis=0)) # index でも axis=0で指定してもいい 省略も可
# # df_copy.drop(labels="A", axis="B")
# # print(df_copy)


backed = ["s", "A", "B"]
backed.append(test2)
df_copy.drop(index=backed, inplace=True) # warningが出るため改善策を検討中
print(df_copy)

print("-----")
# print(df)
df_copy.drop(columns=backed, inplace=True) # warningが出るため改善策を検討中
print(df_copy)

df.drop(index=backed, columns=backed, inplace=True, level=0) # warningが出るため改善策を検討中
print(df)

df.loc["C","E"] = 10

print(df)

df_index_x = df.index.get_loc("x")
print(df_index_x.start)
# df_index = df.index.get_loc("C")
# print(df_index.start)
# df_index = df.index.get_loc("E")
# print(df_index.start)

df.loc["C","x"] = 10
print(df)
print(shortest_path(df, directed=False))
test = ["C","D","E","F","g","x"]

print("-----")

print(test)
print(shortest_path(df, indices=df_index_x.start, directed=False))

print("-----")
# move_cost_result = pd.Series(shortest_path(df, indices=df_index_x.start, directed=False), index=test) # bpで使う
move_cost_result = pd.Series(shortest_path(df, indices=df_index_x.start, directed=False), index=test)
print(move_cost_result)



move_cost_result[move_cost_result == np.inf] = np.nan
move_cost_result.dropna(inplace=True)
print(move_cost_result)



# df.loc["s":"x",['Node','Next Node','Arc']]

# df_sample2=pd.pivot_table(data=df,index='Node',columns=['Next Node'], values='Arc')
# print(df_sample2)