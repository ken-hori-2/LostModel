
import math
from reference_match_rate import Property

# from cal import Cal

class Algorithm_bp_re():

    
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
            

    def BP_re(self, STATE_HISTORY, state, TRIGAR, OBS, BPLIST, action, Add_Advance, total_stress, SAVE_ARC, Storage, CrossRoad, Storage_Stress, Re_first):
        self.STATE_HISTORY = STATE_HISTORY
        self.state = state
        self.TRIGAR = TRIGAR
        # self.OBS = OBS
        # self.BPLIST = BPLIST
        self.Advance_action = action
        # test
        # self.lost = False
        self.bf = True
        self.state_history_first = True
        self.Add_Advance = Add_Advance

        # add 0929
        # self.TRIGAR_REVERSE = False
        # add 0929
        self.total_stress = total_stress
        self.SAVE_ARC = SAVE_ARC
        

        self.first_pop = True



        self.BackPosition_finish = False
        self.Storage = Storage
        self.Storage_Stress = Storage_Stress


        if not type(self.Storage) == list:
            self.Storage = self.Storage.tolist()
        
        if not type(self.Storage_Stress) == list:
            self.Storage_Stress = self.Storage_Stress.tolist()

        if not type(self.OBS) == list:
            self.OBS = self.OBS.tolist()


        pre, Node, Arc, Arc_sum, PERMISSION = self.refer.reference()

        self.Storage = Storage
        self.CrossRoad = CrossRoad
        self.Storage_Stress = Storage_Stress

        self.Re_first = Re_first
        # if self.first_pop:
        #     self.Storage.append([state.row*0, state.column*0])
        #     self.first_pop = False

        while not self.done:
            # self.bf = True
        
            print("\n-----{}Steps-----".format(self.COUNT+1))

            
            if self.BACK or self.bf:
                    try:
                        
                        if self.bf: # ストレスが溜まってから初回
                            # 🔑今は観測されている前提の簡単なやつ
                            # self.Storage_Stress = self.OBS
                            print(f"🥌 WEIGHT = {self.Storage_Stress}")
                            # 手動で設定
                            print("手動で設定!!!!!")
                            
                            print("SAVE ARC : {}".format(self.SAVE_ARC))

                            if not self.Re_first:

                                self.bf = False
                                
                            
                            

                                print("############## DEMO2 ##############")
                                # self.Arc = [math.sqrt((self.Storage[-1].row - self.Storage[x].row) ** 2 + (self.Storage[-1].column - self.Storage[x].column) ** 2) for x in range(len(self.Storage))]
                                if self.Add_Advance:
                                    # add 0923 直線距離
                                    self.Arc = [math.sqrt((self.Storage[-1].row - self.Storage[x].row) ** 2 + (self.Storage[-1].column - self.Storage[x].column) ** 2) for x in range(len(self.Storage))]

                                    
                                    self.SAVE = []
                                    
                                    SUM = 0
                                    first = True
                                    for x in self.SAVE_ARC:
                                        
                                        if first:
                                            first = False
                                        else:
                                            self.SAVE.insert(0, self.SAVE_ARC[-1] + SUM)
                                        SUM += x
                                    print("############## DEMO ############## : {}".format(self.SAVE))
                                        


                                    print("👟 Arc[移動コスト]:{}".format(self.Arc))
                                    index = self.Arc.index(0)

                                    zero_Index = [i for i, x in enumerate(self.Arc) if x == 0]
                                    print("\nZero INDEX : {}".format(zero_Index))
                                    if len(zero_Index) > 1:
                                        print("0が複数個あります。")
                                        self.Arc.pop(-1)

                                    else:
                                        self.Arc.pop(index)
                                    print("👟 Arc(remove 0[現在位置]):{}".format(self.Arc))
                                    print("📂 Storage {}".format(self.Storage))


                                    # if self.Add_Advance:
                                    self.Storage.pop(-1) # advanceアドバンスで追加した現在地の文を削除
                                    # でも、advanceで追加してない時は消しちゃいけない
                                    # おそらくアークも消してしまっている？？

                                    # self.SAVE_ARC.pop(0)

                                    # self.Storage_Arc = self.Cal.caluculate(self.SAVE_ARC)
                                    # print("Storage Arc : {}".format(self.Storage_Arc))

                                
                                    print("📂 Storage(remove) {}".format(self.Storage))

                            

                            else:
                                print("👟 Arc[移動コスト]:{}".format(self.Arc))
                                print("👟 Arc(remove 0[現在位置]):{}".format(self.Arc))
                                print("📂 Storage {}".format(self.Storage))
                                # self.Re_first = False

                            
                        else:
                            print(f"🥌 WEIGHT = {self.Storage_Stress}")
                            print("👟 Arc[移動コスト]:{}".format(self.Arc))

                            print("📂 Storage {}".format(self.Storage))
                        # self.bf = False
                        self.BACK = False
                        
                        # callback
                        # self.next_position = self.agent.back_position(self.BPLIST, self.Storage_Stress, self.Arc)
                        if not self.Re_first:
                            self.next_position = self.agent.back_position(self.Storage, self.Storage_Stress, self.Arc)
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
                        # self.STATE_HISTORY.append(self.state)

                        print("リトライ行動終了！")


                        print(" = 戻り切った状態 🤖🔚")
                        self.BackPosition_finish = True
                        
                        if self.Re_first:
                            self.Re_first = False
                            print("############ test")
                            self.next_position = state*0
                            self.Add_Advance = False
                            # self.Storage.append(state*0)
                            continue
                        break

                        
                
            try:

                if not self.Re_first:
                    if self.state == self.next_position:

                        # self.lost = False
                        
                        # callback
                        self.Storage, self.Storage_Stress, self.Arc, self.OBS = self.agent.back_end(self.Storage, self.next_position, self.Storage_Stress, self.Storage_Stress)
                        self.BACK =True
                        print("🔚 ARRIVE AT BACK POSITION (戻り終わりました。)")
                        print(f"🤖 State:{self.state}")
                        print("OBS : {}".format(self.Storage_Stress))

                        self.STATE_HISTORY.append(self.state)
                        self.STATE_HISTORY.append(self.state)
                        self.STATE_HISTORY.append(self.state)



                        # add 1002
                        self.STATE_HISTORY.append(self.state)
                        self.STATE_HISTORY.append(self.state)
                        self.STATE_HISTORY.append(self.state)
                        self.STATE_HISTORY.append(self.state)
                        self.STATE_HISTORY.append(self.state)
                        self.STATE_HISTORY.append(self.state)
                        self.STATE_HISTORY.append(self.state)
                        self.STATE_HISTORY.append(self.state)
                        self.STATE_HISTORY.append(self.state)

                        self.total_stress = 0
                        


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

                    # if self.lost:
                    #     print("==========\nこれ以上戻れない状態\n==========")
                        
                        
            # except:
            except Exception as e:
                print('=== エラー内容 ===')
                print('type:' + str(type(e)))
                print('args:' + str(e.args))
                print('message:' + e.message)
                print('e自身:' + str(e))
                print("state:{}".format(self.state))
                print("これ以上戻れません。 終了します。")
                    
                    


                break # expansion 無しの場合は何回も繰り返さない
                
            print(f"🤖 State:{self.state}")
            if not self.state_history_first:
                self.STATE_HISTORY.append(self.state)
            print(f"Total Stress:{self.total_stress}")

            print("TRIGAR : {}".format(self.TRIGAR))
            self.state_history_first = False


            if not self.Re_first:
                self.Re_first = False
                self.state = self.next_position
            
            
            print("COUNT : {}".format(self.COUNT))
            if self.COUNT > 100: # 50: # 150:

                print("\n######## BREAK ########\n")
                # breakではなくて、戻る場所に戻れないから別の戻る場所にするとか
                print("\n📂 Storage {}\n\n\n".format(self.Storage))
                break
            self.COUNT += 1

            self.Re_first = False

        # print("state_history : {}".format(self.STATE_HISTORY))
        self.COUNT = 0

        return self.total_stress, self.STATE_HISTORY, self.state, self.Storage_Stress, self.BackPosition_finish