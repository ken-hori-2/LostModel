from pprint import pprint
import numpy as np
from reference_match_rate_Robosin import Property
import pprint
import random


class Algorithm_advance():
    
    def __init__(self, *arg):
        
        self.state = arg[0] # state
        self.env = arg[1] # env
        self.agent = arg[2] # agent
        self.NODELIST = arg[3] # NODELIST
        self.Observation = arg[4]
        self.refer = Property() # arg[5]
        # self.Cal = Cal()
        ########## parameter ##########
        self.total_stress = 0
        self.stress = 0
        self.Stressfull = 2.0
        self.COUNT = 0
        self.done = False
        self.TRIGAR = False
        self.TRIGAR_REVERSE = False
        self.BACK = False
        self.BACK_REVERSE = False
        self.on_the_way = False
        self.bf = True
        ########## parameter ##########
        self.STATE_HISTORY = []
        self.BPLIST = []
        self.PROB = []
        self.Arc = []
        self.OBS = []
        self.FIRST = True
        self.SAVE_ARC = []
        self.Storage = []
        self.Storage_Stress = []
        self.Storage_Arc = []
        # self.Crossroad = []
        self.DEMO_LIST = []
        self.SIGMA_LIST = []
        self.sigma = 0
        self.test_s = 0


    def Advance(self, STATE_HISTORY, state, TRIGAR, OBS, total_stress, grid, CrossRoad, x, TOTAL_STRESS_LIST):
        self.STATE_HISTORY = STATE_HISTORY
        self.state = state
        self.TRIGAR = TRIGAR
        # TEST
        self.grid = grid
        # add 0924
        self.total_stress = total_stress
        print("TOTAl : {}".format(self.total_stress))
        self.OBS = OBS
        # self.action = self.env.actions[0] # コメントアウト 何も処理されない時はこれが prev action に入る
        self.action = random.choice(self.env.actions)
        self.Add_Advance = False
        GOAL = False
        self.CrossRoad = CrossRoad
        pre, Node, Arc, Arc_sum, PERMISSION = self.refer.reference()
        self.stress = 0
        # 初期
        index = Node.index("s")
        pprint.pprint(pre)
        self.TOTAL_STRESS_LIST = TOTAL_STRESS_LIST
        arc_s = 0


        while not self.done:
        
            print("\n-----{}Steps-----".format(self.COUNT+1))

            self.map_unexp_area = self.env.map_unexp_area(self.state)
            if self.map_unexp_area or self.FIRST:
                    self.FIRST = False
                    print("un explore area ! 🤖 ❓❓")
                # if not self.TRIGAR:
                    # if self.total_stress + self.stress >= 0:
                        # self.total_stress += self.stress
                    if self.test_s + self.stress >= 0:
                        try:
                            self.test_s += round(self.stress/float(Arc[index-1]), 3) # 2)
                            self.total_stress += round(self.stress/float(Arc[index-1]), 3)
                        except:
                            self.test_s += 0
                            self.total_stress += 0
                        print("Arc to the next node : {}".format(Arc[index-1]))

                    if self.NODELIST[self.state.row][self.state.column] in pre:
                        print("🪧 NODE : ⭕️")
                        print(f"Arc Stress:{self.test_s}")
                        print(f"Total Stress:{self.total_stress}")
                        # self.total_stress = 0
                
                        index = Node.index(self.NODELIST[self.state.row][self.state.column])
                        print("<{}> match !".format(self.NODELIST[self.state.row][self.state.column]))
                        print("Pre_Arc (事前のArc) : {}".format(Arc[index]))
                        print("Act_Arc (実際のArc) : {}".format(self.test_s))
                        self.SAVE_ARC.append(self.test_s)
                        print("⚠️ 実際のアークの配列 : {}".format(self.SAVE_ARC))
                        # print("実際のアークの配列+現在地からの距離 : {}".format(self.SAVE_ARC_2))
                        print("Arc[index]:{}".format(float(Arc[index])))
                        print("----\n今の permission : {} 以内に発見\n----".format(PERMISSION[index][0]))

                        standard = []
                        standard.append(self.test_s)
                        print("standard【基準距離】 : {}".format(standard[0]))
                        if standard[0] != 0:
                            "-- これがいずれのΔSnodeの式 今はArc に対するΔSのみ --"
                            arc_s = round(abs(1.0-standard[0]), 2)

                            if arc_s > 2:
                                arc_s = 1.0
                        else:
                            arc_s = 0.5 # 0.0 start 地点
                        print("ΔS_Arc【基準ストレス】 : {}".format(arc_s))  #このままだとArcが大きくなるとストレス値も大きくなってしまい、ストレス値の重みが変わってしまうので、基準[1]にする 

                        if self.NODELIST[self.state.row][self.state.column] == "g":
                            print("🤖 GOALに到達しました。")
                            GOAL = True
                            self.STATE_HISTORY.append(self.state)
                            self.TOTAL_STRESS_LIST.append(self.total_stress)
                            break
                        
                        ################################################
                        # 本当はここで見つけた時に、現場情報のリストに格納していく
                        # Observation[state.row][state.column] = round(0.1 * random.randint(1, 10), 2) # 🔑今は観測されている前提の簡単なやつ
                        "===================================================================="
                        "== 基準距離でノードに対するストレス + stressの小ささで戻るノードを決める場合 =="
                        self.Observation[self.state.row][self.state.column] = round(abs(arc_s), 3)
                        "全部コメントアウトの時はsettingのobservationの数値をそのまま使う"
                        "===================================================================="
                        pprint.pprint(self.Observation)
                        try:
                            self.OBS.append(self.Observation[self.state.row][self.state.column])
                        except:
                            self.OBS = self.OBS.tolist()
                            self.OBS.append(self.Observation[self.state.row][self.state.column])
                        print("OBS : {}".format(self.OBS))
                        # 本当はここで見つけた時に、現場情報のリストに格納していく
                        ################################################

                        self.Add_Advance = True
                        self.BPLIST.append(self.state)

                        # 一個前が1ならpopで削除
                        print("📂 Storage {}".format(self.BPLIST))
                        print("Storage append : {}".format(self.Storage))
                        length = len(self.BPLIST)

                        # self.total_stress = 0

                        # BPLIST を保存
                        # self.test_arc = []
                        # self.test_arc = self.SAVE_ARC
                        # print("test[0]:{}".format(self.test_arc[0]))
                        # self.test_arc.pop(0)
                        for bp, stress in zip(self.BPLIST, self.OBS):
                            if bp not in self.Storage:
                                self.Storage.append(bp)
                                self.Storage_Stress.append(stress)

                        # for bp, arc in zip(self.BPLIST, self.SAVE_ARC):
                            # if bp in self.Storage:
                                # self.Storage_Arc.append(sum(self.test_arc))
                                # try:
                                #     # self.test_arc.pop(0)
                                #     print("test arc : {}".format(self.test_arc))
                                # except:
                                #     continue
                        
                        print("Storage append : {}".format(self.Storage))
                        print("Storage Stress append : {}".format(self.Storage_Stress))
                        print("Storage Arc : {}".format(self.Storage_Arc))

                        self.STATE_HISTORY.append(self.state)
                        self.TOTAL_STRESS_LIST.append(self.total_stress)

                        self.test_s = 0
                        "-- Total Stress を発見した(1-Nodeに対するストレス)分だけ減少させる --"
                        print("Total Stress (減少前) : {}".format(self.total_stress))
                        if self.total_stress - (1-arc_s) >= 0:
                            self.total_stress -= (1-arc_s)
                        else:
                            self.total_stress = 0
                        self.SIGMA_LIST.append(self.total_stress)
                        print("SIGMA : {}".format(self.SIGMA_LIST))
                        print("Total Stress (減少後) : {}".format(self.total_stress))
                        "--------------------------------------------------------------"
                    else:

                        if self.grid[self.state.row][self.state.column] == 5:
                            print("\n\n\n交差点! 🚥　🚙　✖️")
                            if self.state not in self.CrossRoad:
                                print("\n\n\n未探索の交差点! 🚥　🚙　✖️")
                                self.CrossRoad.append(self.state)

                            print("CrossRoad : {}\n\n\n".format(self.CrossRoad))
                        print("🪧 NODE : ❌")
                        print("no match!")

                    print("PERMISSION : {}".format(PERMISSION[index][0]))
                    print("Δs = {}".format(self.stress))

                    # if self.total_stress >= PERMISSION[index][0]               +x:  # 追加
                    if self.total_stress >= self.Stressfull: # 2.0:
                        self.TRIGAR = True
                        print(f"Total Stress:{self.total_stress}")
                        print("=================")
                        print("FULL ! MAX! 🔙⛔️")
                        print("=================")
                        self.COUNT += 1
                        self.BPLIST.append(self.state) # Arcを計算する為に、最初だけ必要
                        self.Add_Advance = True
                        "Add1108"
                        print(f"🤖 State:{self.state}")
                        self.STATE_HISTORY.append(self.state)
                        self.TOTAL_STRESS_LIST.append(self.total_stress)
                        print(f"Total Stress:{self.total_stress}")
                        break
            else:
                print("================\n🤖 何も処理しませんでした__2\n================")
                print("マーキング = 1 の探索済みエリア")
                # self.TRIGAR = True
                # break
                
            print(f"🤖 State:{self.state}")
            self.STATE_HISTORY.append(self.state)
            self.TOTAL_STRESS_LIST.append(self.total_stress)
            print(f"Total Stress:{self.total_stress}")

            self.action, self.Reverse, self.TRIGAR = self.agent.policy_advance(self.state, self.TRIGAR, self.action)
            if self.TRIGAR:
                self.env.mark(self.state, self.TRIGAR)
                print("終了します")
                # self.TRIGAR = False
                self.BPLIST.append(self.state) # Arcを計算する為に、最初だけ必要
                self.Add_Advance = True
                break

            # self.next_state, self.stress, self.done = self.env._move(self.state, self.action, self.TRIGAR)
            self.next_state, self.stress, self.done = self.env.step(self.state, self.action, self.TRIGAR)
            self.prev_state = self.state # 1つ前のステップを保存 -> 後でストレスの減少に使う
            self.state = self.next_state

            print("COUNT : {}".format(self.COUNT))
            if self.COUNT > 150: # 150:
                break
            self.COUNT += 1

        print("🍏 ⚠️ 🍐 Action : {}".format(self.action))
        print("TRIGAR : {}".format(self.TRIGAR))
        print("CrossRoad : {}\n\n\n".format(self.CrossRoad))

        return self.total_stress, self.STATE_HISTORY, self.state, self.TRIGAR, self.OBS, self.BPLIST, self.action, self.Add_Advance, GOAL, self.SAVE_ARC, self.CrossRoad, self.Storage, self.Storage_Stress, self.TOTAL_STRESS_LIST # , permission