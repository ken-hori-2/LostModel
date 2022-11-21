import numpy as np
import math
import matplotlib.pyplot as plt

#パーセプトロン
  #3次元の入力

  #2次元の入力
  #1次元の出力

def step(x):
    return 1.0*(x>=0)

#sigmoid関数
def sigmoid(x):
    return 1/(1+np.exp(-x))

#ReLu関数定義
def relu(x):
    return x*(x>=0)

def perceptron(Xn):
    
    # ①重み
    # Wn = np.array([-0.8,1.2,0.6])
    # Wn = np.array([1, 0.25])
    Wn = np.array([1, 0.1])
    print("重みWn [w1, w2] : ", Wn)
    
    # ②バイアス
    # B = 0.25
    B = -0.1
    
    # ③入力値の重み付け(ベクトルの内積で計算) + バイアス
    XnWn = round(np.dot(Xn,Wn), 3) + B
    # XnWn = round(Wn[0]*Xn[0] + Wn[1]*Xn[1], 3) + B
    
    # # ④活性化関数で出力(シグモイド関数)を用いて出力
    # Output = 1 / (1 + math.exp(-XnWn))
    # # Output = 1*(XnWn >= 0) # .0)
    "活性化関数"
    # Output = step(XnWn)
    # Output = sigmoid(XnWn)
    Output = relu(XnWn)
    
    print("sum (XnWn) : ", XnWn)
    return Output, XnWn

#入力
# Xn = np.array([0.2,0.3,-0.1])
Xn = np.array([0.5, -1])
Xn = np.array([0.5, -2])
Xn = np.array([0.5, -3])
Xn = np.array([0.5, -4])


# Xn = np.array([0.6, -2])
print("入力Xn [x1, x2] : ", Xn)

#出力
result, XnWn = perceptron(Xn)
print(result)



"----- Visualization -----"
# #描画
# fig = plt.figure()
# ax = fig.add_subplot(111)
# x = np.linspace(-1,1,500)
# y = step(x)
# ax.plot(x,y)
# ax.scatter(XnWn, result, color="orange")
# plt.show()

#描画
# fig = plt.figure()
# ax = fig.add_subplot(111) # (211)
# #sigmoid関数入出力データ作成
# x = np.linspace(-5,5)
# y = sigmoid(x)
# ax.plot(x,y)
# ax.scatter(XnWn, result, color="orange")
# plt.title('sigmoid')
# plt.show()



#描画
fig = plt.figure()
ax = fig.add_subplot(111) # (211)
#ReLu関数の入出力データ作成
x = np.linspace(-5,5,500)
y = relu(x)
ax.plot(x,y)
ax.scatter(XnWn, result, color="orange")
plt.title('ReLu')
plt.show()