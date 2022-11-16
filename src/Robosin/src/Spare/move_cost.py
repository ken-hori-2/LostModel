import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix
import pandas as pd
import copy

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
# print(df.loc[old, new] - 10)
# print(df[df.loc[old, new] == 0])
# print(df.loc[old, new] == 0)

# print(df.where(df.loc['A','B'] =='0',100))
# print(df.where(df.loc['A','B'] == 0, 10))
# df.loc["A", "B"] = np.where(df.loc['A','B'] == 0, 100)
# print(df)

# df.loc[old,new] = 10

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





print("\n\n\n\n\n")

# print(df.query('A,B == 0'))
# print(df[(df['A'] == 0) & (df['B'] == 0)])

# if df[df.loc[old, new] == 0]:
# if (df.loc[old, new] == 0):
# if df == 0:
# print(df[df.loc[old, new] == 0])
# df.loc[df['A'] == -1, 'A'] = -100
# df.loc[['A','B'] == 0] = -100
# print(df.filter(items=['A', 'C']))
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
# # df_copy.drop(index=[f"{test1}", f"{test2}"], inplace=True)
# # df_copy.drop(index=[f"{test1}","B","C","D","E"], axis=0, inplace=True)

# # df_copy._drop_axis(labels="x", axis="x", level=1, errors=1)
# print(df_copy.drop(["s","A"], axis=0)) # index でも axis=0で指定してもいい 省略も可
# # df_copy.drop(labels="A", axis="B")
# # print(df_copy)


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
# move_cost_result = pd.Series(shortest_path(df, indices=df_index_x.start, directed=False), index=test) # bpで使う
# move_cost_result = pd.Series(shortest_path(df, indices=df_index_x.start, directed=False), index=test)
# print(move_cost_result)



# move_cost_result[move_cost_result == np.inf] = np.nan
# move_cost_result.dropna(inplace=True)
# print(move_cost_result)



print("-----")
"----- 戻った場所を削除 -----"
Node = ["s", "A", "B", "C", "D", "E", "F", "O", "g", "x"]

Unbacked = [i for i in Node if i not in backed]
print("Backed : ", backed)
print("UnBacked : ", Unbacked)
"----- 戻った場所を削除 -----"

print("----- 戻っていないNode群までの各距離 -----")
move_cost_result = pd.Series(shortest_path(df, indices=df_index_x.start, directed=False), index=Unbacked)
# move_cost_result = shortest_path(df, indices=df_index_x.start, directed=False)
print(move_cost_result)
move_cost_result[move_cost_result == np.inf] = np.nan
move_cost_result.dropna(inplace=True)
print("UnBack:\n",move_cost_result)

print("Arc (x -> E) : ", move_cost_result["E"])