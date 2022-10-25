from numpy import average
import random
import pprint
from environment_prob import Environment

# self.actions[0] -> i =  1 (↑)UP
# self.actions[1] -> i = -1 (↓)DOWN
# self.actions[2] -> i =  2 (←)LEFT
# self.actions[3] -> i = -2 (→)RIGHT

class Agent():

    def __init__(self, env):
        
        self.Value_LIST = []
        self.Episode_0 =[[], []] # action, Rt

        self.UP = 1
        self.DOWN = -1
        self.LEFT = 2
        self.RIGHT = -2
        self.Action = [self.UP, self.DOWN, self.LEFT, self.RIGHT] # At

        # test
        self.env = env
        self.Action = env.actions
        print("Action : {}".format(self.Action))





        self.action_length = len(self.Action)
        # print(self.action_length)

        # self.explore_action = [self.LEFT, self.RIGHT]
        # self.explore_action = [self.RIGHT, self.LEFT]
        self.explore_action = [self.UP, self.RIGHT, self.LEFT]
        self.explore_action = [self.env.actions[0], self.env.actions[3], self.env.actions[2]]

        self.demo_index = []
        for x in self.explore_action:
            self.demo_index.append(self.Action.index(x))
        print("demo index : {}".format(self.demo_index))


    def policy(self, Average_Value):

        # print("\n----- 🤖🌟 agent policy -----")

        # self.explore_actionの中から選択
        # 今回は左右方向がそうだった場合
        print("Average Value [⬆️ ⬇️ ⬅️ ➡️ ] : {}".format(Average_Value))
        self.demo = []
        for x in self.demo_index:
            self.demo.append(Average_Value[x])
        print("[⬆️ ➡️ ⬅️ ] : {}".format(self.demo))


        
        try:
            print("\n==============================================\n ⚠️　各行動ごとの平均価値が一番大きい行動を選択\n==============================================")
            maxIndex = [i for i, x in enumerate(Average_Value) if x == max(Average_Value)]
            # print("\nMAX INDEX_0 : {}".format(maxIndex))
            if len(maxIndex) > 1:
                print("平均価値の最大が複数個あります。")
                maxIndex = [random.choice(maxIndex)]
                print("ランダムで Average_Value{} = {} を選択しました。".format(maxIndex, self.Action[maxIndex[0]]))
            else:
                print("平均価値の最大が一つあります。")
            next_action = self.Action[maxIndex[0]]
            print("次の行動At : {}, t-1までの平均価値 : {}".format(next_action, max(Average_Value)))
        # except:
        except Exception as e:
            print(Average_Value)
            print('=== エラー内容 ===')
            print('type:' + str(type(e)))
            print('args:' + str(e.args))
            print('message:' + e.message)
            print('e自身:' + str(e))
            print("ERROR")
            next_action = random.choice(self.Action)
            print("ランダムで {} を選択しました。".format(next_action))


        return next_action

    def value(self):
        print("\n======================\n ⚠️ 行動ごとに価値計算\n======================\n")

        print("🔑 Episode[Action, Rt] : {}".format(self.Episode_0))
        # ここで毎回リセットしないと前回の総和の計算結果を引き継いでしまう
        self.Value = [0]*self.action_length # 4
        print("len = {}".format(len(self.Episode_0[0])))
        self.L_0 = [len(self.Episode_0[0])]*self.action_length # 4
       
        for i in range(len(self.Episode_0[0])):

            if self.Episode_0[0][i] ==  self.UP:                        # 類似エピソードの中の行動ごとに分類 (Episode_2 = prev_action = LEFT)
                # print("🌟")
                self.Value[0] += self.Episode_0[1][i]                     # その類似エピソードの時の行動の結果の価値を加算
            if self.Episode_0[0][i] == self.DOWN:
                # print("🌟 🌟")
                self.Value[1] += self.Episode_0[1][i]
            
            if self.Episode_0[0][i] ==  self.LEFT:
                # print("🌟 🌟 🌟")
                self.Value[2] += self.Episode_0[1][i]
            if self.Episode_0[0][i] == self.RIGHT:
                # print("🌟 🌟 🌟 🌟")
                self.Value[3] += self.Episode_0[1][i]
            

        print("================================\n ⚠️　V = 各行動後に得た報酬の総和\n================================")
        print(" Value :{}, Length : {}".format(self.Value, self.L_0))
        try:
            # print("エラーではない！！！！！")
            Average_Value = [self.Value[x] / self.L_0[x] for x in range(len(self.Value))]
        except:
            # print("エラー！！！！！")
            Average_Value = self.Value
        print("\n価値 Value [UP, DOWN, LEFT, RIGHT] = {}, <<{} 回中>>".format(self.Value, len(self.Episode_0[0])))
        print("価値の平均[UP, DOWN, LEFT, RIGHT] : {}".format(Average_Value))
        

        

        return Average_Value

    def save_episode(self, action):
        # 今回は上と左方向に進んだ時に0.5の確率でストレスが減らせる前提
        # ここには、行動の結果Node⭕️が発見できたかどうかの情報を用いる
        print("\n=============\n ⚠️ 結果の保存 \n=============\n")
        
        
        if action == self.UP:
            print("⚡️ UP Rt = 1")

            self.Episode_0[0].append(action)
            # self.Episode_0[1].append(1) # 今は次の行動で必ず発見できる前提(R = 1)
            self.Episode_0[1].append(random.choice([0, 1])) # 0.5の確率でノード発見 == 新しい情報が得られる == ストレス軽減
            print("🔑 [⬆️　(1) , ⬇️　(-1) , ⬅️　(2) , ⬆️　(-2) ], [Rt] : ") # {}".format(self.Episode_0))
            pprint.pprint(self.Episode_0)
           
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
    
    Average_list = []
    
    RESULT = []
    data = []


    print("\n------------START------------\n")
    # コッチはデータをもとに行動がどのようになるかの実験
                
    test = [[0], [0], [0]]
    env = Environment(*test)
    agent = Agent(env)


    for epoch in range(1, 10):
        print("\n\n############### {}steps ###############\n\n".format(epoch))

        
        ##############
        Average_Value = agent.value()
        ##############


        print("\n===================\n🤖⚡️ Average_Value:{}".format(Average_Value))
        

        print(" == 各行動後にストレスが減らせる確率:{}".format(Average_Value))
        print(" == つまり、新しい情報が得られる確率:{} -----> これが一番重要・・・未探索かつこの数値が大きい方向の行動を選択\n===================\n".format(Average_Value))
        Average_list.append(Average_Value)
        
        ##############
        action = agent.policy(Average_Value)
        ##############
        


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
        

        
        print("\n---------- ⚠️  {}試行後の結果----------".format(epoch))
        
        print("過去のエピソードから、現時点では、🤖⚠️ At == {}を選択する".format(action))
        # Z = 類似エピソード
        
        ##############
        Episode_0 = agent.save_episode(action)
        ##############


        data.append(action)

    print("\n---------- ⚠️  試行終了----------")
    
    print("平均価値[左からN回目]\n")
    print("Value(⬆️ ⬇️ ⬅️ ➡️ ) : ")
    pprint.pprint(Average_list)
    
    
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