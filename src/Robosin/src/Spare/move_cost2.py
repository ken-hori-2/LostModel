import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix
import pandas as pd
import copy


# data = {"A":[0,1,2],
#         "B":[10, 11, 12],
#         "C":[20, 21, 22], }
data = {"s":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "A":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "B":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "C":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "D":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "E":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "F":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "O":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "g":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "x":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}

Node = ["s", "A", "B", "C", "D", "E", "F", "O", "g", "x"]
 
df = pd.DataFrame(data, index = pd.Index(Node))
print(df)

print(df.loc["A", "B"])
df.loc["A","B"] = 100
print(df)
if df.loc["A","B"] == 100:
     df.loc["A","B"] = 700
     print(df)




Node_l = ["s", "A", "B", "C", "D", "E", "F", "O", "g", "x"]

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

# df = pd.DataFrame(np.array(l_2),
#                   columns=[Node_l])

# print(df)
old = "A"
new = "B"

# df = pd.Series(shortest_path(df, directed=False), index=Node_l)
print(type(df))
print(df)


demo = copy.copy(df)
# df_index_x = df.index.get_loc(old)
# # df_index_x = df.index(old)
# print(df_index_x)
# print(type(demo))
# demo = shortest_path(demo, indices=1, directed=False)
# print("-----")
# # print(shortest_path(demo, indices=df_index_x, directed=False))
# print("-----")
# # demo= shortest_path(df, indices=df_index_x.start, directed=False)
# print(demo)
# demo[demo == np.inf] = np.nan
print(demo[old])
print(df.loc[old,new])





print("\n\n\n\n\n")




print(df)

df.loc[old,new] = 10
print(df)

old = "B"
new = "x"
df.loc[old,new] = 10
print(df)

old = "C"
new = "D"
df.loc[old,new] = 10
print(df)

old = "E"
new = "O"
df.loc[old,new] = 10
print(df)

df_copy = copy.copy(df)
df_copy = copy.deepcopy(df) # 基本、行列はこっちらしいがどっちでもできている

test1 = "A"
test2 = "O" # "x"


print("----- 戻った場所の行列を削除 -----")
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
print("----- 戻った場所の行列を削除 -----")

df.loc["C","E"] = 10

print(df)

df_index_x = df.index.get_loc("x")
print(type(df_index_x))
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
print(shortest_path(df, indices=df_index_x.start, directed=False))
print("-----")



print("-----")
"----- 戻った場所を削除 -----"
Node = ["s", "A", "B", "C", "D", "E", "F", "O", "g", "x"]

Unbacked = [i for i in Node if i not in backed]
print("Backed : ", backed)
print("UnBacked : ", Unbacked)
"----- 戻った場所を削除 -----"

print("----- 戻っていないNode群までの各距離 -----")
# move_cost_result = pd.Series(shortest_path(df, indices=df_index_x.start, directed=False), index=Unbacked)
move_cost_result = shortest_path(df, indices=df_index_x.start, directed=False)
print(move_cost_result)
move_cost_result = pd.Series(move_cost_result, index=Unbacked)

# move_cost_result = shortest_path(df, indices=df_index_x.start, directed=False)
print(move_cost_result)
move_cost_result[move_cost_result == np.inf] = np.nan
move_cost_result.dropna(inplace=True)
print("UnBack:\n",move_cost_result)

print("Arc (x -> E) : ", move_cost_result["E"])