from pprint import pprint
import numpy as np
from reference_match_rate import Property
import pprint
import random
from Neural_ReLu import neural
import copy


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
        self.Stressfull = 8 # 6->env1 #10 # 6 # 8 # 10 # 4
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

        self.n = 1 # 0
        self.ind = ["O", "A", "B", "C"]
        self.data_node = []
        self.XnWn_list = []
        self.save_s = []
        self.save_s_all = []
        self.M = 1 # 0

    
    
            

    def Advance(self, STATE_HISTORY, state, TRIGAR, OBS, total_stress, grid, CrossRoad, x, TOTAL_STRESS_LIST, Node_s, Node_A, Node_B, Node_C, Node_D, Node_g, Cost_S, Cost_O, Cost_A, Cost_B, Cost_C, Cost_D, WEIGHT_CROSS_S, WEIGHT_CROSS_O, WEIGHT_CROSS_A, WEIGHT_CROSS_B, WEIGHT_CROSS_C, WEIGHT_CROSS_D):
        self.STATE_HISTORY = STATE_HISTORY
        self.state = state
        self.TRIGAR = TRIGAR

        # TEST
        self.grid = grid

        # add 0924
        self.total_stress = total_stress # 0 # 3 # Stressfull = 10 -3 = 7 # ???????????????????????????????????????????????????????????????
        print("TOTAl : {}".format(self.total_stress))
        self.OBS = OBS
        # self.action = self.env.actions[0] # ????????????????????? ??????????????????????????????????????? prev action ?????????
        self.action = random.choice(self.env.actions)
        self.Add_Advance = False
        GOAL = False
        self.CrossRoad = CrossRoad
        pre, Node, Arc, Arc_sum, PERMISSION = self.refer.reference() # self.callback()
        self.stress = 0
        # ??????
        index = Node.index("s")
        pprint.pprint(pre)

        # Add 1025
        self.TOTAL_STRESS_LIST = TOTAL_STRESS_LIST
        self.Node_s = Node_s
        self.Node_A = Node_A
        self.Node_B = Node_B
        self.Node_C = Node_C
        self.Node_D = Node_D
        self.Node_g = Node_g

        self.Cost_S = Cost_S
        self.Cost_O = Cost_O
        self.Cost_A = Cost_A
        self.Cost_B = Cost_B
        self.Cost_C = Cost_C
        self.Cost_D = Cost_D

        self.WEIGHT_CROSS_S = WEIGHT_CROSS_S
        self.WEIGHT_CROSS_O = WEIGHT_CROSS_O
        self.WEIGHT_CROSS_A = WEIGHT_CROSS_A
        self.WEIGHT_CROSS_B = WEIGHT_CROSS_B
        self.WEIGHT_CROSS_C = WEIGHT_CROSS_C
        self.WEIGHT_CROSS_D = WEIGHT_CROSS_D
        

        "-- ??????ver????????? --"

        # test Add 1029
        arc_s = 0
        ??S = 0

        "1205"
        nnn=1
        mmm=1
        "1205"
        



        print("--------------------------\n Neural \n--------------------------\n")

       

        while not self.done:
        
            print("\n-----{}Steps-----".format(self.COUNT+1))
            self.map_unexp_area = self.env.map_unexp_area(self.state)
            if self.map_unexp_area or self.FIRST:
                    self.FIRST = False
                    print("un explore area ! ???? ??????")
                # if not self.TRIGAR:
                    # if self.total_stress + self.stress >= 0:
                    if self.test_s + self.stress >= 0:
                        "---- Add 1029 ----"
                        # self.total_stress += self.stress
                        # if self.NODELIST[self.state.row][self.state.column] in pre:
                        #     index = Node.index(self.NODELIST[self.state.row][self.state.column])

                        "1205"
                        ex=(nnn/(nnn+mmm))
                        ex = -2*ex+2
                        "1205"
                            
                        try:
                            # self.total_stress += round(self.stress/float(Arc[index-1]), 3) # 2)
                            self.test_s += round(self.stress/float(Arc[index-1]), 3)               *ex # 1205 Add *ex
                            # self.test_s += round((self.stress/float(Arc[index-1]))/(self.n+1), 3)
                            self.total_stress += round(self.stress/float(Arc[index-1]), 3)         *ex # 1205 Add *ex
                            # self.total_stress += round((self.stress/float(Arc[index-1])/(self.n+1)), 3)
                        except:
                            # self.total_stress += 0
                            self.test_s += 0
                            self.total_stress += 0
                        print(" TEST 1029 : {}".format(Arc[index-1]))
                        "---- Add 1029 ----"
                    if self.NODELIST[self.state.row][self.state.column] in pre:
                        
                        # print(f"Total Stress:{self.total_stress}")
                        print(f"Arc Stress:{self.test_s}")
                        index = Node.index(self.NODELIST[self.state.row][self.state.column])
                        print("<{}> match !".format(self.NODELIST[self.state.row][self.state.column]))
                        print("?????????Arc : {}".format(Arc[index]))
                        # print("?????????Arc : {}".format(self.total_stress)) # x))
                        print("?????????Arc : {}".format(self.test_s))
                        # self.SAVE_ARC.append(self.total_stress)
                        self.SAVE_ARC.append(self.test_s)
                        print("?????? ??????????????????????????? : {}".format(self.SAVE_ARC))
                        # print("???????????????????????????+???????????????????????? : {}".format(self.SAVE_ARC_2))
                        print("Arc[index]:{}".format(float(Arc[index])))
                        print("----\n?????? permission : {} ???????????????\n----".format(PERMISSION[index][0]))

                        standard = []
                
                        " -- Add 1029 --"
                        # try:
                        #     # standard.append(round(test/int(Arc[index]), 2)) # ?????????????????? = total_stress ???????????????????????????????????????
                        #     standard.append(round(self.total_stress/float(Arc[index]), 2))
                        # except:
                        #     standard.append(0)
                        # standard.append(self.total_stress)
                        standard.append(self.test_s)
                        print("standard?????????????????? : {}".format(standard[0]))

                        # if standard[0] != 0:
                        "-- ???????????????????????Snode?????? ??????Arc ??????????????S?????? --"
                        
                        
                        "====================================== Add =========================================="
                        # arc_s = round(abs(1.0-standard[0]), 3)
                        ??S = 0.3 # 0.1, 0.2, 0.3 # ?????? arc_s
                        self.save_s_all.append(??S)
                        "----- 1120 -----"
                        self.n += 1
                        "1205"
                        nnn+=1
                        self.M=1
                        mmm=1
                        "1205"

                        Wn = np.array([1, -0.1])
                        print("??????Wn [w1, w2] : ", Wn)
                        model = neural(Wn)
                        print(f"??????Xn[??S, n] : {??S}, {self.n}")
                        neu_fire, XnWn = model.perceptron(np.array([??S, self.n])) # Relu??????
                        print(f"??????result [n={self.n} : {abs(neu_fire)}]")
                        if neu_fire > 0: # or src = neural
                            print("??????????????")
                            "----- Add 1122 -----"
                            self.save_s.append(round(??S-neu_fire, 2))
                            "----- Add 1122 -----"
                            # pass
                            ??S = neu_fire
                        else:
                            print("???????????????????????")
                            "----- Add 1122 -----"
                            self.save_s.append(??S)
                            "----- Add 1122 -----"
                            # pass
                            ??S = 0
                        self.data_node.append(abs(neu_fire))
                        self.XnWn_list.append(XnWn)
                        print("[result] : ", self.data_node)
                        print("[??????, ??????] : ", self.XnWn_list)
                        "----- 1120 -----"

                        "Add meeting 1120"
                        arc_s = round(abs(self.total_stress-standard[0]+??S), 3)
                        # arc_s = round(abs(??S), 3)
                        print("==========================================")
                        print("SUM : ", self.total_stress)
                        print("??S Arc : ", standard[0])
                        print("??S : ", ??S)
                        print("result : ", arc_s)
                        print("Save ??S-Neuron : ", self.save_s)
                        print("Save's ?? : ", round(sum(self.save_s), 2))
                        ?? = round(sum(self.save_s), 2)

                        print("Save ??S : ", self.save_s_all)
                        print("Save's All ?? : ", round(sum(self.save_s_all), 2))
                        print("==========================================")
                        "====================================== Add =========================================="

                        
                        # arc_s = round(1.0-standard[0], 2)
                        # if arc_s > 2:
                        #     arc_s = 1.0
                        # if arc_s == 0:
                        #     arc_s = 1.0
                        # else:
                            # arc_s = 0.5 # 0.0
                        print("arc stress???????????????????????? : {}".format(arc_s))  #??????????????????Arc????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????[1]????????? 
                    


                        if self.NODELIST[self.state.row][self.state.column] == "g":
                            print("???? GOAL????????????????????????")
                            GOAL = True
                            break
                        
                        ################################################
                        # ????????????????????????????????????????????????????????????????????????????????????
                        # self.Observation[self.state.row][self.state.column] = round(0.1 * random.randint(1, 10), 2) # ???????????????????????????????????????????????????????
                        # add 1007(????????????)
                        # comment out 1025
                        "----------------------------------------------------------------------------------------------------------"
                        "Node?????????????????????????????????"
                        # self.Observation[self.state.row][self.state.column] = self.Observation[self.state.row][self.state.column]
                        
                        "== ???????????????????????????????????????????????? + ????????????????????????????????????????????????????????? =="
                        # self.Observation[self.state.row][self.state.column] = round(abs(1.0 - arc_s), 3)
                        "== ???????????????????????????????????????????????? + stress???????????????????????????????????????????????? =="
                        
                        "1120"
                        self.Observation[self.state.row][self.state.column] = round(abs(arc_s), 3) # 1107 comment out

                        "????????????????????????????????????setting???observation??????????????????????????????"
                        "----------------------------------------------------------------------------------------------------------"
                        pprint.pprint(self.Observation)
                        try:
                            self.OBS.append(self.Observation[self.state.row][self.state.column])
                        except:
                            self.OBS = self.OBS.tolist()
                            self.OBS.append(self.Observation[self.state.row][self.state.column])
                        print("OBS : {}".format(self.OBS))
                        # ????????????????????????????????????????????????????????????????????????????????????
                        ################################################
                        
                        
                        print("???? NODE : ??????")

                        # if not self.NODELIST[self.state.row][self.state.column] == "s":
                        self.Add_Advance = True
                        self.BPLIST.append(self.state)

                        
                        # ????????????1??????pop?????????
                        print("???? Storage {}".format(self.BPLIST))

                        print("Storage append : {}".format(self.Storage))
                        length = len(self.BPLIST)
                        
                        NS = 0
                        NA = 0
                        NB = 0
                        NC = 0
                        ND = 0
                        NO = 0
                        
                        for bp, stress in zip(self.BPLIST, self.OBS):
                            if bp not in self.Storage:
                                self.Storage.append(bp)
                                self.Storage_Stress.append(stress)
                                
                        "-- ?????????????????? --"
                        if self.NODELIST[self.state.row][self.state.column] == "s":
                            NS = stress
                        elif self.NODELIST[self.state.row][self.state.column] == "A":
                            NA = stress
                        elif self.NODELIST[self.state.row][self.state.column] == "B":
                            NB = stress
                        elif self.NODELIST[self.state.row][self.state.column] == "C":
                            NC = stress
                        elif self.NODELIST[self.state.row][self.state.column] == "D":
                            ND = stress
                        elif self.NODELIST[self.state.row][self.state.column] == "O": #"g":
                            NO = stress

                        "--test--"
                        self.Node_s.append(NS)
                        self.Node_A.append(NA)
                        self.Node_B.append(NB)
                        self.Node_C.append(NC)
                        self.Node_D.append(ND)
                        self.Node_g.append(NO)

                        self.Cost_S.append(0)
                        self.Cost_A.append(0)
                        self.Cost_B.append(0)
                        self.Cost_C.append(0)
                        self.Cost_D.append(0)
                        self.Cost_O.append(0)

                        self.WEIGHT_CROSS_S.append(0)
                        self.WEIGHT_CROSS_O.append(0)
                        self.WEIGHT_CROSS_A.append(0)
                        self.WEIGHT_CROSS_B.append(0)
                        self.WEIGHT_CROSS_C.append(0)
                        self.WEIGHT_CROSS_D.append(0)
                        
                        print("Storage append : {}".format(self.Storage))
                        print("Storage Stress append : {}".format(self.Storage_Stress))
                        print("Storage Arc : {}".format(self.Storage_Arc))

                        self.STATE_HISTORY.append(self.state)
                        self.TOTAL_STRESS_LIST.append(self.total_stress)


                        # self.TOTAL_STRESS_LIST.append(abs(1.0-self.total_stress))
                        # self.TOTAL_STRESS_LIST.append(arc_s)

                        "---- comment out 1029 ----"
                        # self.Node_s.append(0)
                        # self.Node_A.append(0)
                        # self.Node_B.append(0)
                        # self.Node_C.append(0)
                        # self.Node_D.append(0)
                        # self.Node_g.append(0)
                        "---- comment out 1029 ----"
                        "Add 1029"

                        "-- comment out 1104 --"
                        # self.total_stress = 0
                        "-- comment out 1104 --" # ????????????????????????????????????????????????

                        # self.total_stress += self.test_s
                        self.test_s = 0
                        "-- Total Stress ???????????????(1-Node????????????????????????)???????????????????????? --"
                        # self.sigma += self.total_stress
                        # self.sigma = self.total_stress
                        # self.total_stress = 0
                        print("total stress : {}".format(self.total_stress))

                        "----- 1120 -----"
                        # self.total_stress -= (1-arc_s)
                        self.total_stress = 0
                        self.total_stress += arc_s
                        # self.n += 1
                        # "?????????????????????????????????????????????2???????????????0.2???????????????????????????????????????????????????"
                        # Wn = np.array([1, -0.1])
                        # print("??????Wn [w1, w2] : ", Wn)
                        # model = neural(Wn)
                        # neu, XnWn = model.perceptron(np.array([arc_s, self.n])) # Relu??????
                        # # print("??????result : ", abs(neu))
                        # print(f"??????result {x} : {abs(neu)}")
                        # if neu > 0: # or src = neural
                        #     print("??????????????")
                        #     self.total_stress += arc_s
                        # else:
                        #     print("???????????????????????")
                        #     pass
                        # self.data_node.append(abs(neu))
                        # self.XnWn_list.append(XnWn)
                        # print(self.data_node)
                        # print(self.XnWn_list)
                        # # model.graph(self.ind, self.data_node)
                        # # model.visalization(self.XnWn_list, self.data_node)
                        "----- 1120 -----"

                        self.SIGMA_LIST.append(self.total_stress)
                        print("SIGMA : {}".format(self.SIGMA_LIST))
                        # self.total_stress = self.sigma
                        # self.TOTAL_STRESS_LIST.append(self.total_stress)
                        print("total stress : {}".format(self.total_stress))
                        "--------------------------------------------------------------"
                    else:

                        if self.grid[self.state.row][self.state.column] == 5:
                            print("\n\n\n?????????! ????????????????????")

                            # for x in zip(self.BPLIST, self.OBS):
                            if self.state not in self.CrossRoad:

                                print("\n\n\n?????????????????????! ????????????????????")
                                self.CrossRoad.append(self.state)

                            print("CrossRoad : {}\n\n\n".format(self.CrossRoad))

                            
                        "----- Add 1124 -----"
                        print("?????????????????????Node!!!!!!!!!!!!")
                        if self.NODELIST[self.state.row][self.state.column] == "x":
                            self.M += 1
                            "1205"
                            mmm+=1
                            "1205"

                            "----- A -----"
                            # print("===== ???????????????????? =====")
                            # print("total : ", round(self.total_stress, 3))
                            # print("Save ??S-Neuron : ", self.save_s)
                            # print("Save's ?? : ", ??)
                            # self.total_stress += 0.2*??*self.M
                            # # self.total_stress += ??*self.M
                            # print("total : ", round(self.total_stress, 3))
                            # print("===== ???????????????????? =====")
                            "----- A -----"
                            
                            "----- B -----"
                            # # arc_s = round(abs(self.total_stress-self.test_s+0.2*??*self.M))
                            # print("===== ???????????????????? =====")
                            # print("total : ", round(self.total_stress, 3))
                            # print("Save ??S-Neuron : ", self.save_s)
                            # try:
                            #     print("Save's ?? : ", ??)
                            # except:
                            #     pass

                            # "parameter" # Add ??
                            # # ?? = 2 # 10
                            # # self.M = 1
                            # self.n = 2 # 5 # 5 # 2 # 3 # 10
                            # ?? = 0.3*self.n
                            # print("Save's ?? : ", ??)

                            # # self.n = 10
                            # self.n2 = copy.copy(self.n)
                            # self.n = 0
                            # "parameter"
                            # # self.total_stress += 0.2*??*self.M # m??????
                            # # self.total_stress += ??*self.M # ????????????????????????????????????????????? (M=0,1,2...) # m??????
                            # # self.total_stress += 0.1*??*self.M # m??????
                            # "----- Add 1128 -----"
                            # print("Save's ?? : ", ??)
                            # print("[M, n2] : ", self.M, self.n2)
                            # print("m/n2=", self.M/self.n2)
                            # print("total : ", round(self.total_stress, 3))
                            # # self.total_stress += ??*(self.M/self.n2)
                            # print("m/m+n=", self.M/(self.M+self.n2))
                            # # print("??*2*m/(m+n)=", ?? *2* (self.M/(self.M+self.n2)))
                            # # self.total_stress += ?? *2* (self.M/(self.M+self.n2))
                            # print("??*4*m/(m+n)=", ?? *4* (self.M/(self.M+self.n2)))
                            # self.total_stress += ?? *4* (self.M/(self.M+self.n2))
                            # print("total : ", round(self.total_stress, 3))
                            # "----- Add 1128 -----"
                            # # self.total_stress = 0
                            # # self.total_stress += arc_s
                            # self.STATE_HISTORY.append(self.state)
                            # self.TOTAL_STRESS_LIST.append(self.total_stress)
                            # self.total_stress -= self.test_s # ?????????????????????????????????????????????????????????????????
                            # print("total : ", round(self.total_stress, 3))
                            # self.test_s = 0
                            # print("===== ???????????????????? =====")
                            "----- B -----"

                            "----- C -----"
                            print("===== ???????????????????? =====")
                            print("total : ", round(self.total_stress, 3))
                            print("Save ??S-Neuron : ", self.save_s)
                            try:
                                print("Save's ?? : ", ??)
                            except:
                                pass
                            "----- parameter -----" # Add ??
                            # # ?? = 2 # 10
                            # # self.M = 1
                            # self.n = 5 # 2 # 5 # 3 # 10
                            # # "-- x --"
                            # # ?? = 0.3*self.n # 0.3, 0.1, 0.2
                            # # print("Save's ?? : ", ??)
                            ?? = 1 # 1.1 # 0.1
                            "-- x --"
                            self.n2 = copy.copy(self.n)
                            # self.n = 0
                            self.n=1
                            nnn=1
                            "----- parameter -----"
                            print("Save's ?? : ", ??)
                            print("[M, n2] : ", self.M, self.n2)
                            # print("m/n2=", self.M/self.n2)
                            print("total : ", round(self.total_stress, 3))
                            print("m/m+n=", self.M/(self.M+self.n2))
                            print("??*4*m/(m+n)=", ?? *4* (self.M/(self.M+self.n2)))
                            # self.total_stress += ?? *4.0* (self.M/(self.M+self.n2))
                            # self.total_stress += ?? *2.0* (self.M/(self.M+self.n2)) # n=5,0.2 # ??????
                            self.total_stress += ?? *1.0* (self.M/(self.M+self.n2)) # n=5,0.2 # ?????? main
                            # self.total_stress += ?? # row
                            # self.total_stress += ??*2 # row*2
                            
                            print("total : ", round(self.total_stress, 3))
                            self.STATE_HISTORY.append(self.state)
                            self.TOTAL_STRESS_LIST.append(self.total_stress)
                            self.total_stress -= self.test_s # ?????????????????????????????????????????????????????????????????
                            print("total : ", round(self.total_stress, 3))
                            self.test_s = 0
                            print("===== ???????????????????? =====")
                            "----- C -----"
                            
                        "----- Add 1124 -----"


                        print("???? NODE : ???")
                        print("no match!")

                    print("PERMISSION : {}".format(PERMISSION[index][0]))
                    print("??s = {}".format(self.stress))

                    # if self.total_stress >= permission: # self.Stressfull:
                    # if self.total_stress >= PERMISSION[index][0]               +x:  # ??????
                    if self.total_stress >= 2.0: # Add 1029 10:

                        self.TRIGAR = True
                        print(f"Total Stress:{self.total_stress}")
                        print("=================")
                        print("FULL ! MAX! ??????????")
                        print("=================")
                        self.COUNT += 1
                        self.BPLIST.append(self.state) # Arc??????????????????????????????????????????
                        self.Add_Advance = True
                        break
            else:
                print("================\n???? ?????????????????????????????????__2\n================")
                print("??????????????? = 1 ????????????????????????")
                # self.TRIGAR = True
                # break
                
            print(f"???? State:{self.state}")
            self.STATE_HISTORY.append(self.state)

            # 1025
            self.TOTAL_STRESS_LIST.append(self.total_stress)
            # self.TOTAL_STRESS_LIST.append(abs(1.0-self.total_stress))
            # self.TOTAL_STRESS_LIST.append(arc_s)
            print(f"Total Stress:{self.total_stress}")


            self.Node_s.append(0)
            self.Node_A.append(0)
            self.Node_B.append(0)
            self.Node_C.append(0)
            self.Node_D.append(0)
            self.Node_g.append(0)

            "--test--"
            self.Cost_S.append(0)
            self.Cost_A.append(0)
            self.Cost_B.append(0)
            self.Cost_C.append(0)
            self.Cost_D.append(0)
            self.Cost_O.append(0)

            self.WEIGHT_CROSS_S.append(0)
            self.WEIGHT_CROSS_O.append(0)
            self.WEIGHT_CROSS_A.append(0)
            self.WEIGHT_CROSS_B.append(0)
            self.WEIGHT_CROSS_C.append(0)
            self.WEIGHT_CROSS_D.append(0)
            
            self.action, self.Reverse, self.TRIGAR = self.agent.policy_advance(self.state, self.TRIGAR, self.action)
            if self.TRIGAR:
                self.env.mark(self.state, self.TRIGAR)
                print("???????????????")
                # self.TRIGAR = False

                # add 0929
                self.BPLIST.append(self.state) # Arc??????????????????????????????????????????
                self.Add_Advance = True
                break

            
            # self.next_state, self.stress, self.done = self.env._move(self.state, self.action, self.TRIGAR)
            self.next_state, self.stress, self.done = self.env.step(self.state, self.action, self.TRIGAR)
            self.prev_state = self.state # 1?????????????????????????????? -> ????????????????????????????????????

            self.state = self.next_state
            
            
            print("COUNT : {}".format(self.COUNT))
            if self.COUNT > 150: # 150:
                break
            self.COUNT += 1

        print("???? ?????? ???? Action : {}".format(self.action))
        print("TRIGAR : {}".format(self.TRIGAR))
        print("CrossRoad : {}\n\n\n".format(self.CrossRoad))

        return self.total_stress, self.STATE_HISTORY, self.state, self.TRIGAR, self.OBS, self.BPLIST, self.action, self.Add_Advance, GOAL, self.SAVE_ARC, self.CrossRoad, self.Storage, self.Storage_Stress, self.TOTAL_STRESS_LIST, self.Node_s, self.Node_A, self.Node_B, self.Node_C, self.Node_D, self.Node_g, self.Cost_S, self.Cost_O, self.Cost_A, self.Cost_B, self.Cost_C, self.Cost_D, self.WEIGHT_CROSS_S, self.WEIGHT_CROSS_O, self.WEIGHT_CROSS_A, self.WEIGHT_CROSS_B, self.WEIGHT_CROSS_C, self.WEIGHT_CROSS_D # , permission