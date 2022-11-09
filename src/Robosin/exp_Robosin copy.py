from pprint import pprint
import numpy as np
import pprint
# from reference_match_rate import Property
# Add 1027 Robosin
from reference_match_rate_Robosin import Property


class Algorithm_exp():

    
    def __init__(self, *arg):
        
        self.state = arg[0] # state
        self.env = arg[1] # env
        self.agent = arg[2] # agent
        self.NODELIST = arg[3] # NODELIST
        self.Observation = arg[4]
        self.refer = Property() # arg[5]
        
        ########## parameter ##########
        self.total_stress = 0
        self.stress = 0
        self.Stressfull = 8 # 4 #8 # 10 # 4
        self.COUNT = 0
        self.done = False
        self.TRIGAR = False
        ########## parameter ##########
        self.STATE_HISTORY = []

        self.bp_end = False
            

    def Explore(self, STATE_HISTORY, state, TRIGAR, total_stress, grid, CrossRoad, x): # , PERMISSION):

        self.STATE_HISTORY = STATE_HISTORY
        self.state = state
        self.TRIGAR = False # TRIGAR

        pre, Node, Arc, Arc_sum, PERMISSION = self.refer.reference()
        pprint.pprint(PERMISSION)


        self.NODE_POSITION = state

        # self.map_unexp_area = map_unexp_area
        self.lost = False
        self.grid = grid
        self.CrossRoad = CrossRoad
        GOAL = False



        
        self.total_stress = 0 # total_stress # 0
        self.stress = 0
        # 初期
        index = Node.index("s")

        self.STATE_HISTORY.append(self.state)
        self.STATE_HISTORY.append(self.state)
        self.STATE_HISTORY.append(self.state)
        self.STATE_HISTORY.append(self.state)
        # self.STATE_HISTORY.append(self.state)
        # self.STATE_HISTORY.append(self.state)
        # self.STATE_HISTORY.append(self.state)
        # self.STATE_HISTORY.append(self.state)
        # self.STATE_HISTORY.append(self.state)

        while not self.done:
            print("\n========== 🌟 {}steps ==========".format(self.COUNT+1))

            # if self.total_stress + self.stress >= 0:
            #     self.total_stress += self.stress


            
            
            
            self.STATE_HISTORY.append(self.state)
            
            print(f"🤖 State:{self.state}")
            print("stress : {}".format(self.stress))

            # if not self.crossroad:
            self.map_unexp_area = self.env.map_unexp_area(self.state)
            if self.map_unexp_area:
                print("un explore area ! 🤖 ❓❓")
                # Add 0924################################################
                # if self.NODELIST[self.state.row][self.state.column] > 0.0:
                if self.NODELIST[self.state.row][self.state.column] in pre:

                    print("🪧 NODE : ⭕️")
                    
                    if self.total_stress + self.stress >= 0:
                        self.total_stress += self.stress


                    if self.NODELIST[self.state.row][self.state.column] == "g":
                        print("🤖 GOALに到達しました。")
                        GOAL = True
                        self.STATE_HISTORY.append(self.state)
                        self.STATE_HISTORY.append(self.state)
                        break
                    
                    
                    
                    
                    # self.TRIGAR = False # ここでFalseにすることでadvance_Algorithmで撮った場所のノードも追加してしまう

                    print("\n============================\n🤖 🔛　アルゴリズム切り替え\n============================")
                    break # Advanceに移行する？
                # Add 0924################################################

            if self.NODELIST[self.state.row][self.state.column] in pre:
                index = Node.index(self.NODELIST[self.state.row][self.state.column])
                # test = x-sum_test
            
                print("<{}> match !".format(self.NODELIST[self.state.row][self.state.column]))
                print("事前のArc : {}".format(Arc[index]))
                self.total_stress = 0

            # if not self.lost:
            else:
                if self.total_stress + self.stress >= 0:
                    self.total_stress += self.stress


                if self.grid[self.state.row][self.state.column] == 5:
                    print("\n\n\n交差点! 🚥　🚙　✖️")
                    if self.state not in self.CrossRoad:
                        print("\n\n\n未探索の交差点! 🚥　🚙　✖️")
                        self.CrossRoad.append(self.state)

                    print("CrossRoad : {}\n\n\n".format(self.CrossRoad))

            print("PERMISSION : {}".format(PERMISSION[index][0]))
            # if self.total_stress >= self.Stressfull:
            if self.total_stress >= PERMISSION[index][0]                +x: # or self.lost:　　　　# 追加
                self.TRIGAR = True
                print("=================")
                print("FULL ! MAX! 🔙⛔️")
                print("=================")
                self.state = self.NODE_POSITION
                self.STATE_HISTORY.append(self.state)
                # self.STATE_HISTORY.append(self.state)
                # self.STATE_HISTORY.append(self.state)
                print(f"🤖 State:{self.state}")
                self.total_stress = 0
                
             

            
            print(f"Total Stress:{self.total_stress}")
            print("trigar : {}".format(self.TRIGAR))



            self.action, self.bp_end, self.All_explore, self.TRIGAR, self.Reverse, self.lost = self.agent.policy_exp(self.state, self.TRIGAR)
            if self.lost:
                self.TRIGAR = True
                print("=================")
                print("LOST! 🔙⛔️")
                print("=================")
                self.state = self.NODE_POSITION
                self.STATE_HISTORY.append(self.state)
                # self.STATE_HISTORY.append(self.state)
                # self.STATE_HISTORY.append(self.state)
                print(f"🤖 State:{self.state}")
                self.total_stress = 0
                # break
                
            print("All explore : {}".format(self.All_explore))
            if self.All_explore:
                self.env.mark_all(state)
                # self.STATE_HISTORY.append(self.state)
                print("終了します")
                self.All_explore = False
                # self.total_stress = 0

                ############コメントアウト##############
                # self.TRIGAR = True
                ############コメントアウト##############
                break
            # self.next_state, self.stress, self.done = self.env._move(self.state, self.action, self.TRIGAR, self.All_explore, self.Reverse)
            if not self.lost:
                # self.next_state, self.stress, self.done = self.env._move(self.state, self.action, self.TRIGAR)
                self.next_state, self.stress, self.done = self.env.step(self.state, self.action, self.TRIGAR)
                self.prev_state = self.state # 1つ前のステップを保存 -> 後でストレスの減少に使う
                self.state = self.next_state
            else:
                self.lost = False

            # print(f"Total Stress 2 :{self.total_stress}")

            if self.COUNT > 150: # 50: # 150:
                break
            self.COUNT += 1

        # print("state_history : {}".format(self.STATE_HISTORY))
        if self.done:
            print("GOAL")

        return self.total_stress, self.STATE_HISTORY, self.state, self.TRIGAR, self.CrossRoad, GOAL