import numpy as np
import math
import matplotlib.pyplot as plt

# def graph(index, data_node):

#         # # カラーマップインスタンス生成
#         # cm_n = plt.get_cmap("Greens")
#         # seikika_node = data_node # np.round(preprocessing.minmax_scale(data_node), 3)
#         # color_maps_node = [cm_n(seikika_node[0]), cm_n(seikika_node[1]), cm_n(seikika_node[2]), cm_n(seikika_node[3])]

#         plt.bar(index, data_node, color="green", label="state of mind", alpha=0.5)
#         plt.title('Psychological state of the agent')
#         plt.legend()
#         plt.show()


# index = ["安心", "不安度"]

# data_node = [0.6, 0.4]

# graph(index, data_node)



# パラメータを指定
# phi = 0.3
phi = 0.5

# 作図用の値を作成
x_vals = np.array([0.0, 1.0])
# probability = np.array([1.0 - phi, phi])
probability = np.array([phi, 1.0 - phi])
print(x_vals)
print(probability)

# ベルヌーイ分布を作図
plt.figure(figsize=(9, 8)) # 図の設定
plt.bar(x_vals, probability, color='#00A968') # 棒グラフ
plt.plot([-0.5, 1.5], [0.5, 0.5], color='orange', linestyle='--', label='0.5') # 平均

#plt.vlines(x=E_x, ymin=0.0, ymax=np.max(probability), color='orange', linestyle='--', label='$E[x]$') # 平均
#plt.vlines(x=E_x - V_x, ymin=0.0, ymax=np.max(probability), color='orange', linestyle=':', label='$E[x] - \sqrt{V[x]}$') # 平均 - 標準偏差
#plt.vlines(x=E_x + V_x, ymin=0.0, ymax=np.max(probability), color='orange', linestyle=':', label='$E[x] + \sqrt{V[x]}$') # 平均 + 標準偏差
plt.xlabel('x') # x軸ラベル
plt.ylabel('probability') # y軸ラベル
plt.suptitle('Bernoulli Distribution', fontsize=20) # 図タイトル
plt.title('$\phi=' + str(phi) + '$', loc='left') # タイトル
plt.xticks(ticks=[0, 1]) # x軸目盛
plt.legend() # 凡例
plt.ylim(0,1)
plt.grid() # グリッド線
plt.show() # 描画


