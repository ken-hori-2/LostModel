
import math
from reference_match_rate_Robosin import Property
import copy
from Spare.move_cost_calculation import move_cost_cal

class Algorithm_bp():

    def __init__(self, *arg):
        
        self.state = arg[0] # state
        self.env = arg[1] # env
        self.agent = arg[2] # agent
        self.NODELIST = arg[3] # NODELIST
        self.Observation = arg[4]
        self.refer = Property()
        # self.Cal = Cal()
        ########## parameter ##########
        self.total_stress = 0
        self.stress = 0
        self.Stressfull = 8 # 10 # 4
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
        # self.next_position = []
        self.Storage_Arc = []
        self.SAVE = []

        # self.COST = move_cost_cal()
            

    def BP(self, STATE_HISTORY, state, TRIGAR, OBS, BPLIST, action, Add_Advance, total_stress, SAVE_ARC, TOTAL_STRESS_LIST):
        self.STATE_HISTORY = STATE_HISTORY
        self.state = state
        self.TRIGAR = TRIGAR
        self.OBS = OBS
        self.BPLIST = BPLIST
        self.Advance_action = action
        self.bf = True
        self.state_history_first = True
        self.Add_Advance = Add_Advance
        self.total_stress = total_stress
        self.SAVE_ARC = SAVE_ARC
        self.first_pop = True
        self.BackPosition_finish = False
        pre, Node, Arc, Arc_sum, PERMISSION = self.refer.reference()
        self.TOTAL_STRESS_LIST = TOTAL_STRESS_LIST


        while not self.done:
        
            print("\n-----{}Steps-----".format(self.COUNT+1))

            
            
            "戻る行動の可視化ver.の場合はここにReverseが入る"




            if self.BACK or self.bf:
                    try:
                        
                        if self.bf: # ストレスが溜まってから初回
                            self.w = self.OBS
                            print(f"🥌 WEIGHT = {self.w}")
                            print("SAVE ARC : {}".format(self.SAVE_ARC))

                            if self.Add_Advance:
                                # ユークリッド距離
                                self.Arc = [math.sqrt((self.BPLIST[-1].row - self.BPLIST[x].row) ** 2 + (self.BPLIST[-1].column - self.BPLIST[x].column) ** 2) for x in range(len(self.BPLIST))]

                                # self.Arc = self.SAVE_ARC
                                # 以下をBPLISTと紐づけられればできるかもしれない
                                # self.SAVE_ARC = [
                                #     [0, 0, 0, 0], # ?->sまでの距離
                                #     [4, 0, 0, 0], # sまでの距離
                                #     [8, 4, 0, 0], # s, Aまでの距離
                                #     [12, 8, 4, 0], # s, A, Bまでの距離
                                #     [15, 11, 7, 3], # s, A, B, Cまでの距離
                                #     # [19, 15, 11, 7], # s, A, B, C, Dまでの距離
                                # ]
                                # self.Arc = []
                                # for x in range(len(self.BPLIST)):
                                #     self.Arc.append(x)
                                
                                
                                "Comment Out"
                                # self.SAVE = []

                                # SUM = 0
                                # first = True
                                # for x in self.SAVE_ARC:
                                #     if first:
                                #         first = False
                                #     else:
                                #         self.SAVE.insert(0, self.SAVE_ARC[-1] + SUM)
                                #     SUM += x
                                # print("############## DEMO ############## : {}".format(self.SAVE))
                                "Comment Out"

                                "===== Add 1111 ====="
                                self.test = copy.copy(self.SAVE_ARC)
                                self.COST = move_cost_cal(self.test)
                                self.result_list = self.COST.test()
                                print("========== Move Cost Calculation ==========")
                                print(self.result_list)
                                print("========== Move Cost Calculation ==========")
                                self.SAVE_ARC.pop(-1)
                                "===== Add 1111 ====="




                                
                                # self.Arc = self.SAVE

                                print("👟 Arc[移動コスト]:{}".format(self.Arc))
                                index = self.Arc.index(0)
                                self.Arc.pop(index)
                                print("👟 Arc(remove 0[現在位置]):{}".format(self.Arc))
                                print("📂 Storage {}".format(self.BPLIST))

                                self.BPLIST.pop(-1) # advanceアドバンスで追加した現在地の文を削除
                                # でも、advanceで追加してない時は消しちゃいけない
                                # おそらくアークも消してしまっている？？
                                # self.SAVE_ARC.pop(0)
                                # self.Storage_Arc = self.Cal.caluculate(self.SAVE_ARC)
                                # print("Storage Arc : {}".format(self.Storage_Arc))
                                print("📂 Storage(remove) {}".format(self.BPLIST))

                            print("👟 Arc[移動コスト]:{}".format(self.Arc))
                            print("👟 Arc(remove 0[現在位置]):{}".format(self.Arc))
                            print("📂 Storage {}".format(self.BPLIST))  
                        else:
                            print(f"🥌 WEIGHT = {self.w}")
                            print("👟 Arc[移動コスト]:{}".format(self.Arc))
                            print("📂 Storage {}".format(self.BPLIST))
                        self.bf = False
                        self.BACK = False

                        self.next_position = self.agent.back_position(self.BPLIST, self.w, self.Arc)
                        print(f"========Decision Next State=======\n⚠️  NEXT POSITION:{self.next_position}\n==================================")
                        self.on_the_way = True 
                    except:
                    # except Exception as e:
                    #     print('=== エラー内容 ===')
                    #     print('type:' + str(type(e)))
                    #     print('args:' + str(e.args))
                    #     print('message:' + e.message)
                    #     print('e自身:' + str(e))
                        print("ERROR!")
                        print("リトライ行動終了！")
                        print(" = 戻り切った状態 🤖🔚")
                        self.BackPosition_finish = True
                        break
            try:

                if self.state == self.next_position:

                    # self.lost = False
                    self.BPLIST, self.w, self.Arc, self.OBS = self.agent.back_end(self.BPLIST, self.next_position, self.w, self.OBS)
                    self.BACK =True
                    print("🔚 ARRIVE AT BACK POSITION (戻り終わりました。)")
                    print(f"🤖 State:{self.state}")
                    print("OBS : {}".format(self.OBS))

                    # self.total_stress = 0 # 1108
                    "-- test1104 --"
                    "==========================="
                    "⚠️ 要検討 ⚠️ 戻った時にどのくらい減少させるか test_s = 進んだ分だけ減少させるか = その場所までのストレスまで減少させるか"
                    print("⚠️ total : {}".format(self.total_stress))
                    delta_s = self.Observation[self.state.row][self.state.column]
                    delta_s = round(abs(1.0-delta_s), 3)
                    if delta_s > 2:
                        delta_s = 1.0

                    if self.total_stress - delta_s >= 0:
                        self.total_stress -= delta_s
                    else:
                        self.total_stress = 0

                    print("⚠️ delta_s : {}".format(delta_s))
                    print("⚠️ total : {}".format(self.total_stress))
                    "-- test1104 --"
                    self.STATE_HISTORY.append(self.state)
                    self.TOTAL_STRESS_LIST.append(self.total_stress)

                    # self.total_stress = 0 # 1108

                    # Add 1027 Robosin
                    self.TRIGAR = False
                    self.TRIGAR_REVERSE = False

                    # 0921 統合テスト
                    print("\n============================\n🤖 🔛　アルゴリズム切り替え\n============================")
                    break

                    COUNT += 1
                    continue
                else:
                    if self.on_the_way:
                        self.on_the_way = False
                    else:
                        print("🔛 On the way BACK")
            except:
                # except Exception as e:
                #     print('=== エラー内容 ===')
                #     print('type:' + str(type(e)))
                #     print('args:' + str(e.args))
                #     print('message:' + e.message)
                #     print('e自身:' + str(e))
                    print("state:{}".format(self.state))
                    print("これ以上戻れません。 終了します。")
                    break # expansion 無しの場合は何回も繰り返さない
                
            print(f"🤖 State:{self.state}")
            if not self.state_history_first:
                self.STATE_HISTORY.append(self.state)
                self.TOTAL_STRESS_LIST.append(self.total_stress)
            print(f"Total Stress:{self.total_stress}")
            print("TRIGAR : {}".format(self.TRIGAR))
            self.state_history_first = False
            self.state = self.next_position
            print("COUNT : {}".format(self.COUNT))

            if self.COUNT > 100: # 50: # 150:
                print("\n######## BREAK ########\n")
                
                # breakではなくて、戻る場所に戻れないから別の戻る場所にするとか
                print("\n📂 Storage {}\n\n\n".format(self.BPLIST))
                break
            self.COUNT += 1
        self.COUNT = 0

        return self.total_stress, self.STATE_HISTORY, self.state, self.OBS, self.BackPosition_finish, self.TOTAL_STRESS_LIST