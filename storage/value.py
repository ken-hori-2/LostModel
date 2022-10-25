import math
from operator import length_hint
from tkinter import LEFT, RIGHT

from numpy import average
import random
import collections

import pprint


# agent_add_Episode_Edit.py の整理ver.

# self.actions[0] -> i =  1 (↑)UP
# self.actions[1] -> i = -1 (↓)DOWN
# self.actions[2] -> i =  2 (←)LEFT
# self.actions[3] -> i = -2 (→)RIGHT

class Agent():

    def __init__(self):
        
        self.V_0_LIST = []
        

        self.Episode_0 =[[], []] # action, Rt

        self.UP = 1
        self.DOWN = -1
        self.LEFT = 2
        self.RIGHT = -2
        self.A_0 = [self.UP, self.DOWN, self.LEFT, self.RIGHT] # At

        self.action_length = len(self.A_0)
        print(self.action_length)


    def policy(self, ave_0):

        # print("\n----- 🤖🌟 agent policy -----")
        
        try:
            print("\n==============================================\n ⚠️　各行動ごとの平均価値が一番大きい行動を選択\n==============================================")
            maxIndex = [i for i, x in enumerate(ave_0) if x == max(ave_0)]
            # print("\nMAX INDEX_0 : {}".format(maxIndex))
            if len(maxIndex) > 1:
                print("平均価値の最大が複数個あります。")
                maxIndex = [random.choice(maxIndex)]
                print("ランダムで ave_0{} = {} を選択しました。".format(maxIndex, self.A_0[maxIndex[0]]))
            else:
                print("平均価値の最大が一つあります。")
            # next_action_0 = A_0[maxIndex_0[0]]
            next_action = self.A_0[maxIndex[0]]
            print("次の行動At : {}, t-1までの平均価値 : {}".format(next_action, max(ave_0)))
        # except:
        except Exception as e:
            print(ave_0)
            print('=== エラー内容 ===')
            print('type:' + str(type(e)))
            print('args:' + str(e.args))
            print('message:' + e.message)
            print('e自身:' + str(e))
            print("ERROR")
            # next_action_0 = random.choice(A_0)
            next_action = random.choice(self.A_0)
            print("ランダムで {} を選択しました。".format(next_action))
        

        

        
        
        return next_action

    def value(self):

        # print("\n----- ⚠️  類似エピソード(At-1)ごとに価値計算-----\n")
        print("\n======================\n ⚠️ 行動ごとに価値計算\n======================\n")

        print("🔑 Episode[Action, Rt] : {}".format(self.Episode_0))

        # ここで毎回リセットしないと前回の総和の計算結果を引き継いでしまう
        self.V_0 = [0]*self.action_length # 4
        
        print("len = {}".format(len(self.Episode_0[0])))

        self.L_0 = [len(self.Episode_0[0])]*self.action_length # 4
        

        # if prev_action == self.UP:
        for i in range(len(self.Episode_0[0])):

            if self.Episode_0[0][i] ==  self.UP:                        # 類似エピソードの中の行動ごとに分類 (Episode_2 = prev_action = LEFT)
                # print("🌟")
                self.V_0[0] += self.Episode_0[1][i]                     # その類似エピソードの時の行動の結果の価値を加算
            if self.Episode_0[0][i] == self.DOWN:
                # print("🌟 🌟")
                self.V_0[1] += self.Episode_0[1][i]
            
            if self.Episode_0[0][i] ==  self.LEFT:
                # print("🌟 🌟 🌟")
                self.V_0[2] += self.Episode_0[1][i]
            if self.Episode_0[0][i] == self.RIGHT:
                # print("🌟 🌟 🌟 🌟")
                self.V_0[3] += self.Episode_0[1][i]
            

        print("================================\n ⚠️　V = 各行動後に得た報酬の総和\n================================")
        print(" V_0 :{}, L : {}".format(self.V_0, self.L_0))
        try:
            # print("エラーではない！！！！！")
            ave_0 = [self.V_0[x] / self.L_0[x] for x in range(len(self.V_0))]
        except:
            # print("エラー！！！！！")
            ave_0 = self.V_0
        print("\n価値 V_0 [UP, DOWN, LEFT, RIGHT] = {}, <<{} 回中>>".format(self.V_0, len(self.Episode_0[0])))
        print("価値の平均[UP, DOWN, LEFT, RIGHT] : {}".format(ave_0))
        

        

        return ave_0


    # def save_episode(self, prev_action, action):
    def save_episode(self, action):

        
        # 今回は上と左方向に進んだ時に0.5の確率でストレスが減らせる前提




        print("\n=============\n ⚠️ 結果の保存 \n=============\n")
        
        
        if action == self.UP:
            print("⚡️ UP Rt = 1")

            self.Episode_0[0].append(action)
            # self.Episode_0[1].append(1) # 今は次の行動で必ず発見できる前提(R = 1)
            self.Episode_0[1].append(random.choice([0, 1])) # 0.5の確率でノード発見 == 新しい情報が得られる == ストレス軽減
            print("🔑 [⬆️　(1) , ⬇️　(-1) , ⬅️　(2) , ⬆️　(-2) ], [Rt] : ") # {}".format(self.Episode_0))
            pprint.pprint(self.Episode_0)
            # self.Episode_2[2].append(random.choice([0, 1]))

        elif action == self.LEFT:
            print("⚡️ LEFT Rt = 1")

            self.Episode_0[0].append(action)
            # self.Episode_0[1].append(1) # 今は次の行動で必ず発見できる前提(R = 1)
            self.Episode_0[1].append(random.choice([0, 1])) # 0.5の確率でノード発見 == 新しい情報が得られる == ストレス軽減
            print("🔑 [⬆️　(1) , ⬇️　(-1) , ⬅️　(2) , ⬆️　(-2) ], [Rt] : ") # {}".format(self.Episode_0))
            pprint.pprint(self.Episode_0)
        else:
            self.Episode_0[0].append(action)
            self.Episode_0[1].append(0)



        

        print("\nノード発見 == 新しい情報が得られる == ストレス軽減 できる方向を保存")

        

        return self.Episode_0




def main():

    UP = 1
    DOWN = -1
    LEFT = 2
    RIGHT = -2
    
    # 目印を発見している限りは行動を継続している(つまり、未発見になって初めて方向を変える)と仮定すると、At-1で戻る時、その前のAt-2も戻る方向と同じ
    
    AVE_0_LIST = []
    
    RESULT = []
    data = []


    print("\n------------START------------\n")
    # コッチはデータをもとに行動がどのようになるかの実験
                
    agent = Agent()


    for epoch in range(1, 10): # 4): # 50):
        print("\n\n############### {}steps ###############\n\n".format(epoch))

        
        ave_0 = agent.value()
        print("\n===================\n🤖⚡️ ave:{}".format(ave_0))
        

        print(" == 各行動後にストレスが減らせる確率:{}".format(ave_0))
        print(" == つまり、新しい情報が得られる確率:{} -----> これが一番重要・・・未探索かつこの数値が大きい方向の行動を選択\n===================\n".format(ave_0))
        AVE_0_LIST.append(ave_0)
        
        action = agent.policy(ave_0)
        


        if action==  LEFT:
            NEXT = "LEFT  ⬅️"
            print("    At :-> {}".format(NEXT))
        if action == RIGHT:
            NEXT = "RIGHT ➡️"
            print("    At :-> {}".format(NEXT))  
        if action ==  UP:
            NEXT = "UP    ⬆️"
            print("    At :-> {}".format(NEXT))
        if action == DOWN:
            NEXT = "DOWN  ⬇️"
            print("    At :-> {}".format(NEXT))
        

        # print("\n---------- ⚠️ {}試行後の結果----------".format(5*epoch))
        print("\n---------- ⚠️  {}試行後の結果----------".format(epoch))
        # print("過去のエピソードから、現時点では、At-1の時、Atを選択する")
        print("過去のエピソードから、現時点では、🤖⚠️ At == {}を選択する".format(action))
        # Z = 類似エピソード
        
        "test0824"
        # Add Episode いつどの行動を取ったらどのくらい報酬が得られたか
       
        # print("\n----- ⚠️  action = {} -----".format(action))
        
        Episode_0 = agent.save_episode(action)

        

        data.append(action)

    print("\n---------- ⚠️  試行終了----------")
    
    print("平均価値[左からN回目]\n")
    print("V_0(⬆️ ⬇️ ⬅️ ➡️ ) : ")
    pprint.pprint(AVE_0_LIST)
    
    
    print("UP    : {}".format(data.count(1)))
    print("DOWN  : {}".format(data.count(-1)))
    RESULT.append(data.count(1))
    RESULT.append(data.count(-1))
    
    print("LEFT  : {}".format(data.count(2)))
    print("RIGHT : {}".format(data.count(-2)))
    RESULT.append(data.count(2))
    RESULT.append(data.count(-2))

    print("RESULT:{}".format(RESULT))

main()