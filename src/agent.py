from cgi import test
from tkinter.messagebox import NO
import numpy as np
from sklearn import preprocessing
import random

from reference_match_rate import Property
import math


class Agent():

    # def __init__(self, env, GOAL_STATE, NODELIST, map, grid):
    def __init__(self, env, marking_param, *arg):
        self.env = env
        self.actions = env.actions
        self.GOAL_REACH_EXP_VALUE = 50 # max_theta # 50
        self.lost = False
        self.test = False
        self.grid = arg[0]
        self.map = arg[1]
        self.NODELIST = arg[2]
        # self.goal = arg[3]

        self.refer = Property() # arg[5]

        # self.actions = self.env.actions
        # self.goal = GOAL_STATE
        # self.NODELIST = NODELIST
        # self.map = map
        # self.grid = grid
        # print("GOAL STATE : {}".format(self.goal))
        self.marking_param = marking_param

        

    def policy_advance(self, state, TRIGAR, action):
        
        self.TRIGAR_advance = TRIGAR
        self.prev_action = action
        print("Prev Action : {}".format(action))

        # try:
        action = self.model_advance(state)
        self.Advance_action = action
    
        print("Action : {}".format(action))
        print("Advance action : {}".format(self.Advance_action))
        
        print("ð ð ð ð ð")
        # return action, self.All, self.Reverse
        # except:
        if action == None:
            print("ERROR ð¤")
            ############ã³ã¡ã³ãã¢ã¦ã##############
            # self.TRIGAR_advance = True
            ############ã³ã¡ã³ãã¢ã¦ã##############

            # return self.actions[1], self.Reverse, self.TRIGAR_advance # ãã®action[1]ãã¨ã©ã¼ã®åå 
            return self.prev_action, self.Reverse, self.TRIGAR_advance # ãã®prev action ãä»®
            
        return action, self.Reverse, self.TRIGAR_advance

    def policy_bp(self, state, TRIGAR, TRIGAR_REVERSE, COUNT):
        self.TRIGAR_bp = TRIGAR
        self.TRIGAR_REVERSE_bp = TRIGAR_REVERSE

        # All = False
        self.All = False
        self.Reverse = False
        # self.lost = False
        self.COUNT = COUNT

        try:
            # self.lost = False
            action, self.Reverse = self.model_bp(state)
            print("Action : {}".format(action))
        except:
        # except Exception as e:
        #     print('=== ã¨ã©ã¼åå®¹ ===')
        #     print('type:' + str(type(e)))
        #     print('args:' + str(e.args))
        #     print('message:' + e.message)
        #     print('eèªèº«:' + str(e))
            print("agent / policy_bp ERROR")

            # if NOT_MOVE:
            #     self.All = True




            # ããã®ãããã§æ²¼ã§ãå°ãåãã¦ãã
            # return self.actions[1], self.Reverse    , self.lost
            return random.choice(self.actions), self.Reverse    , self.lost

        print("ð ð ð ð ð")
        # return action, self.All, self.Reverse
        return action, self.Reverse , self.lost


    



    def policy_exp(self, state, TRIGAR):
        self.trigar = TRIGAR
        attribute = self.NODELIST[state.row][state.column]
        next_direction = random.choice(self.actions)
        self.All = False
        bp = False
        self.lost = False

        self.Reverse = False
        
        try:
            y_n, action, bp = self.model_exp(state)
            
            print("y/n:{}".format(y_n))
            print("Action : {}".format(action))
        except:
            print("ãã®ãã¼ãããæ¢ç´¢ã§ããè¨±å®¹ç¯å²ã¯æ¢ç´¢æ¸ã¿\næ»ãå ´ææ±ºå®ã®ã¢ã«ã´ãªãºã ã¸")
            print("TRIGAR : {}".format(self.trigar))
            
            # Add 1024 â  ããã¯è¿½å ããªãã¦ãå¤§ä¸å¤«ã ã£ã
            # self.All = True
            # Add 1024 â 




            return self.actions[1], bp, self.All, self.trigar, self.Reverse, self.lost

        
        return action, bp, self.All, self.trigar, self.Reverse, self.lost



    def model_exp(self, state):

        next_diretion = [(self.actions[0]), (self.actions[1]), (self.actions[2]), (self.actions[3])]

        y_n = False
        bp = False
        
        pre, Node, Arc, Arc_sum, PERMISSION = self.refer.reference()

        # if self.NODELIST[state.row][state.column] == 1: # 2: # ä»ã¯ããã«å¥ã£ã¦bp_algorithmã«é·ç§»ãã¦ãã
        if self.NODELIST[state.row][state.column] in pre:
                print("========\næ¢ç´¢çµäº\n========")
                self.trigar = False
                bp = True

        elif self.NODELIST[state.row][state.column] == "x":
            print("========\näº¤å·®ç¹\n========")
            self.trigar = False

            
        print("========\næ¢ç´¢éå§\n========")
        # if not self.trigar:

        exp_action = []
        for dir in next_diretion:

            print("dir:{}".format(dir))
            y_n, action = self.env.expected_move(state, dir, self.trigar, self.All, self.marking_param)




            # ããã«ããã§ããæ°ããæå ±ãå¾ãããããªæ¹åãåªåçã«æ¢ã
            # åæ°ãä¿å­ãã´ã¼ã«æ¹å
            # 1.æªæ¢ç´¢
            # 2.æ»ãä»¥å¤ã®3æ¹åããã©ã³ãã (ç¾ç¶) (1. == 2.)

            # ä»¥ä¸ãããæ°ããæå ±ãå¾ãããããªæ¹åã®æ±ºå®
            # 3.ã´ã¼ã«æ¹å
            # 4.åæ°ã®å¤ãæ¹å
            # print(self.actions)
            # print(self.actions[0])
            # exp_action = []
            if y_n:
                y_n = False
                exp_action.append(action)
                print("================================================== exp action : {}".format(exp_action))









            
            # if y_n:
            #     return y_n, action, bp
            # print("y/n:{}".format(y_n))
        if exp_action:
            for x in exp_action:
                print("1015 exp action : {}".format(x))
                if x == self.actions[2]:
                    print("========= Action.LEFT 1015 test =========")
            y_n = True
            return y_n, exp_action[0], bp
        print("y/n:{}".format(y_n))



        
        if not bp:
            print("==========\nããä»¥ä¸é²ããªãç¶æ\n or æ¬¡ã®ãã¹ã¯æ¢ç´¢æ¸ã¿\n==========") # ã©ã®é¸æè¢ã y_n = False
            self.lost = True
            # self.trigar = True
        else:
            self.All = True # False
                # for dir in next_diretion:
                #     print("\ndir:{}".format(dir))
                #     y_n, action = self.env.expected_move_return(state, dir, self.trigar, self.All)

                #     if y_n:
                #         return y_n, action, bp
                #     print("y/n:{}".format(y_n))
        # else:
        #     for dir in next_diretion:
        #         print("\ndir:{}".format(dir))
        #         y_n, action = self.env.expected_move_return(state, dir, self.trigar, self.All)

        #         if y_n:
        #             return y_n, action, bp
        #         print("y/n:{}".format(y_n))

        print("==========\nè¿·ã£ãç¶æ\n==========") # ã©ã®é¸æè¢ã y_n = False
        print("= ç¾å¨å°ããã´ã¼ã«ã«è¿ããé¸æè¢ã¯ãªã\n")
        # self.lost = True


    def model_advance(self, state):

        next_diretion = [(self.actions[0]), (self.actions[1]), (self.actions[2]), (self.actions[3])]
        # next_diretion = [(self.actions[1]), (self.actions[0]), (self.actions[2]), (self.actions[3])]
        # next_diretion = []

        pre, Node, Arc, Arc_sum, PERMISSION = self.refer.reference()
        if self.NODELIST[state.row][state.column] in pre:
            print("ã©ã³ãã ã«æ±ºå®")
            next_diretion = self.advance_direction_decision(next_diretion)
        else:
            next_diretion = [(self.actions[0]), (self.actions[1]), (self.actions[2]), (self.actions[3])]
        # è©¦ãã«ã³ã¡ã³ãã¢ã¦ã0923
        # advanceã®è¡åã®åªååº¦ããããããè¨­å®


        if self.NODELIST[state.row][state.column] == "x":
            print("ã©ã³ãã ã«æ±ºå®")
            next_diretion = self.advance_direction_decision(next_diretion)

        
        print("next dir : {}".format(next_diretion))

        y_n = False
        # bp = False
        self.All = False


        self.Reverse = False
        if self.NODELIST[state.row][state.column] == "x":
            print("========\näº¤å·®ç¹\n========")
            self.TRIGAR_advance = False

        print("========\nAdvanceéå§\n========")
        if not self.TRIGAR_advance:
            for dir in next_diretion:

                print("dir:{}".format(dir))
                y_n, action = self.env.expected_move(state, dir, self.TRIGAR_advance, self.All, self.marking_param)
                # self.prev_action = action
                # print("prev action : {}".format(self.prev_action))
                
                if y_n:
                    self.prev_action = action
                    # print("prev action : {}".format(self.prev_action))
                    
                    return action
                print("y/n:{}".format(y_n))
            

        print("==========\nè¿·ã£ããè¨±å®¹ãè¶ãããç¶æ\n==========") # ã©ã®é¸æè¢ã y_n = False
        print("= ããä»¥ä¸åã«ç¾å¨å°ããã´ã¼ã«ã«è¿ããé¸æè¢ã¯ãªã\n= ä¸æ¦ä½å¶ãæ´ãã\n= æ»ã")

        print("\n ã¨ããããã¯ã¹ãã¬ã¹ãæºã¾ãåãåã«ããä»¥ä¸é²ããªããªã£ã¦ã¨ã©ã¼ãåºã")
        self.TRIGAR_advance = True
        # # self.trigar = True
        # print("prev action2 : {}".format(self.prev_action))
        # lost = True
        # return self.prev_action

    def model_bp(self, state):

        # next_diretion = [(self.actions[0]), (self.actions[1]), (self.actions[2]), (self.actions[3])]
        # next_diretion = [(self.actions[1]), (self.actions[0]), (self.actions[2]), (self.actions[3])]

        
        # if self.NODELIST[state.row][state.column] == "x":
        #     print("========\näº¤å·®ç¹\n========")
        #     self.TRIGAR_bp = False
        #     self.TRIGAR_REVERSE_bp = False
        pre, Node, Arc, Arc_sum, PERMISSION = self.refer.reference()

        
        
        
        
        
        
        
        
        # Add 1024 â¡ ããã¯è¿½å ããªãã¦ãå¤§ä¸å¤«ã ã£ã
        # if self.COUNT > 30:
        #     # if self.NODELIST[self.state.row][self.state.column] in pre:
        #     #     pass
        #     print("æ²¼ã«ããã£ãæã«ã¨ãããã1ã®ãã¼ã­ã³ã°éãã«æ»ãæ©è½")
        #     next_diretion = self.next_direction_decision("trigar")
        #     for dir in next_diretion:
        #         print("\ndir:{}".format(dir))
        #         y_n, action = self.env.expected_move_return(state, dir, self.TRIGAR_bp, self.All)

        #         if y_n:
        #             self.lost = False
        #             return action, self.Reverse

        #     print("ãã¼ã­ã³ã°ã1ã®æ¹åã¯ã©ãã«ããªã -> ãã¼ã­ã³ã°2ã®æ¹åãç®æã")
        #     for dir in next_diretion:
        #         print("\ndir:{}".format(dir))
        #         y_n, action = self.env.expected_move_return_reverse(state, dir, self.TRIGAR_REVERSE_bp, self.Reverse)

        #         if y_n:
        #             self.lost = False
        #             return action, self.Reverse

        # Add 1024 â¡


        
        print("========\nBACK éå§\n========")
        print("TRIGAR : {}".format(self.TRIGAR_bp))
        print("REVERSE : {}".format(self.TRIGAR_REVERSE_bp))

        
        
        if self.TRIGAR_REVERSE_bp:
            self.Reverse = True
            # next_diretion = self.next_direction_trigar() # [(self.actions[0]), (self.actions[1]), (self.actions[2]), (self.actions[3])]
            next_diretion = self.next_direction_decision("reverse")
            for dir in next_diretion:
                print("\ndir:{}".format(dir))
                y_n, action = self.env.expected_move_return_reverse(state, dir, self.TRIGAR_REVERSE_bp, self.Reverse)

                if y_n:
                    self.lost = False
                    return action, self.Reverse
                print("y/n:{}".format(y_n))
            print("TRIGAR REVERSE â¡ï¸ð")

            
            
        
        if self.TRIGAR_bp:
            # next_diretion = self.next_direction_trigar_reverse() # [(self.actions[1]), (self.actions[0]), (self.actions[2]), (self.actions[3])]
            next_diretion = self.next_direction_decision("trigar")
            print("TEST!!!!!")

            # add0926
            # self.TRIGAR_REVERSE_bp = False

            
            for dir in next_diretion:
                print("\ndir:{}".format(dir))
                y_n, action = self.env.expected_move_return(state, dir, self.TRIGAR_bp, self.All)

                if y_n:
                    self.lost = False
                    return action, self.Reverse
                print("y/n:{}".format(y_n))

            # add 0924
            # if not bp:
            if self.lost:
                print("==========\nããä»¥ä¸æ»ããªãç¶æ\n or æ¬¡ã®ãã¹ã¯ä»¥åæ»ã£ãå ´æ\n==========") # ã©ã®é¸æè¢ã y_n = False
                # self.lost = False
                # self.trigar = True
                for dir in next_diretion:
                    print("\ndir:{}".format(dir))
                    y_n, action = self.env.expected_not_move(state, dir, self.trigar, self.All)

                    if y_n:
                        return action, self.Reverse # , self.lost
                    print("y/n:{}".format(y_n))

        

        print("==========\næ»ãçµãã£ãç¶æ\n==========") # ã©ã®é¸æè¢ã y_n = False
        print("= ç¾å¨å°ããæ¬¡ã«ã´ã¼ã«ã«è¿ããé¸æè¢ãé¸ã¶ãæªæ¢ç´¢æ¹åã\n")
        self.lost = True







    def back_position(self, BPLIST, w, Arc):
        "== ä¸è´åº¦ã®å¤§ããã§æ»ããã¼ããæ±ºããå ´å =="
        # try:
        #     Arc_INVERSE = [round(1/Arc[x],2) for x in range(len(Arc))]
        # except:
        # #     # Arc_INVERSE = [round(Arc[x],2) for x in range(len(Arc))]
        #     print("ERROR")
        #     Arc_INVERSE = []
        #     for x in range(len(Arc)):
        #         try:
        #             Arc_INVERSE.append(round(1/Arc[x],2))
        #         except:
        #             Arc_INVERSE.append(0)
        "----------------------------------------------------------------------"
        # ã¹ãã¬ã¹ã®å°ãããã¼ãã«æ»ãver.
        "== stressã®å°ããã§æ»ããã¼ããæ±ºããå ´å =="
        Arc_INVERSE = [round(Arc[x],2) for x in range(len(Arc))] # Arc_INVERSE ã§ã¯ãªã Arc
        "----------------------------------------------------------------------"

            
        "----------------------------------------------------------------------"
        # æ­£è¦åã«ããã¨0, 1ãåºã¦ãã¾ãã®ã§ãstressÃcost ã§0ã«ãªãããããããã«æ»ããã¨ãå¤ããªã£ã¦ãã¾ã 1026

        
        # w = np.round(preprocessing.minmax_scale(w), 3)
        # Arc = np.round(preprocessing.minmax_scale(Arc), 3)
        # Arc_INVERSE = np.round(preprocessing.minmax_scale(Arc_INVERSE), 3)
        "----------------------------------------------------------------------"
        print("ðæ­£è¦å w : {}, Arc : {}".format(w, Arc))
        print("ð æ­£è¦å WEIGHT : {}, Arc_INVERSE : {}".format(w, Arc_INVERSE))

        # Arc = [0, 0]ã®æ,Arc = [1, 1]ã«å¤æ´
        if all(elem  == 0 for elem in Arc_INVERSE):
            Arc_INVERSE = [1 for elem in Arc_INVERSE]
            print("   Arc = [0, 0]ã®æ, Arc_INVERSE : {}".format(Arc_INVERSE))
        if all(elem  == 0 for elem in w):
            w = [1 for elem in w]
            print("   WEIGHT = [0, 0]ã®æ, WEIGHT : {}".format(w))


        WEIGHT_CROSS = [round(x*y, 3) for x,y in zip(w,Arc_INVERSE)]
        print("â¡ï¸ WEIGHT CROSS:{}".format(WEIGHT_CROSS))

        if all(elem  == 0 for elem in WEIGHT_CROSS):
            print("WEIGHT CROSSã¯å¨é¨0ã§ãã")
            
            # Arc = Arc.tolist() # 1026

            print("Arc type : {}".format(type(Arc)))
            near_index = Arc.index(min(Arc))
            print("Arc:{}, index:{}".format(Arc, near_index))
            WEIGHT_CROSS[near_index] = 1
            print("â¡ï¸ WEIGHT CROSS:{}".format(WEIGHT_CROSS))

        # try:
        #     w = w.tolist()
        # except:
        #     pass
        # next_position = BPLIST[w.index(max(w))] # stressã®ã¿ã§æ»ãå ´ææ±ºå®
        # 1024
        "----------------------------------------------------------------------"
        # next_position = BPLIST[WEIGHT_CROSS.index(max(WEIGHT_CROSS))] # stress + cost
        # Add 1026
        next_position = BPLIST[WEIGHT_CROSS.index(min(WEIGHT_CROSS))] # stress + cost
        "----------------------------------------------------------------------"









        

        return next_position

    def back_end(self, BPLIST, next_position, w, OBS):
        
        bpindex = BPLIST.index(next_position)
        # Arc = [(abs(BPLIST[bpindex].row-BPLIST[x].row)) for x in range(len(BPLIST))]
        Arc = [math.sqrt((BPLIST[-1].row - BPLIST[x].row) ** 2 + (BPLIST[-1].column - BPLIST[x].column) ** 2) for x in range(len(BPLIST))]
        print("ð Arc[ç§»åã³ã¹ã]:{}".format(Arc))
        index = Arc.index(0)
        Arc.pop(index)
        print("ð Arc(remove 0[ç¾å¨ä½ç½®]):{}".format(Arc))
        print("ð Storage {}".format(BPLIST))
        BPLIST.remove(next_position)
        print("ð Storage(remove) {}".format(BPLIST))
        w = np.delete(w, bpindex)
        print("ð¥ WEIGHT(remove):{}".format(w))

        # print("ð¥ OBS:{}".format(OBS))
        # OBS = np.delete(OBS, bpindex)
        try:
            OBS.pop(bpindex)
        except:
            OBS = OBS.tolist()
            OBS.pop(bpindex)
        print("ð¥ OBS(remove):{}".format(OBS))

        return BPLIST, w, Arc, OBS



    



    def next_direction_decision(self, trigar__or__reverse):
        if self.Advance_action == self.actions[0]: # Action.UP:
        # if self.Advance_action == self.actions[1]: # Action.UP:
            self.BP_action = self.actions[1] # [0] # [1]
            next_diretion_trigar = [(self.actions[1]), (self.actions[0]), (self.actions[2]), (self.actions[3])]
            next_diretion_trigar_reverse = [(self.actions[0]), (self.actions[1]), (self.actions[2]), (self.actions[3])]
            # next_diretion_trigar_reverse = [(self.actions[1]), (self.actions[0]), (self.actions[2]), (self.actions[3])]
            # next_diretion_trigar = [(self.actions[0]), (self.actions[1]), (self.actions[2]), (self.actions[3])]

        elif self.Advance_action == self.actions[1]: # Action.DOWN:
        # elif self.Advance_action == self.actions[0]: # Action.DOWN:
            self.BP_action = self.actions[0] # [1] # [0]
            next_diretion_trigar = [(self.actions[0]), (self.actions[1]), (self.actions[2]), (self.actions[3])]
            next_diretion_trigar_reverse = [(self.actions[1]), (self.actions[0]), (self.actions[2]), (self.actions[3])]
            # next_diretion_trigar_reverse = [(self.actions[0]), (self.actions[1]), (self.actions[2]), (self.actions[3])]
            # next_diretion_trigar = [(self.actions[1]), (self.actions[0]), (self.actions[2]), (self.actions[3])]

        elif self.Advance_action == self.actions[2]: # Action.LEFT:
        # elif self.Advance_action == self.actions[3]: # Action.LEFT:
            self.BP_action = self.actions[3] # [2] # [3]
            next_diretion_trigar = [(self.actions[3]), (self.actions[2]), (self.actions[0]), (self.actions[1])]
            next_diretion_trigar_reverse = [(self.actions[2]), (self.actions[3]), (self.actions[0]), (self.actions[1])]
            # next_diretion_trigar_reverse = [(self.actions[3]), (self.actions[2]), (self.actions[0]), (self.actions[1])]
            # next_diretion_trigar = [(self.actions[2]), (self.actions[3]), (self.actions[0]), (self.actions[1])]

        elif self.Advance_action == self.actions[3]: # Action.RIGHT:
        # elif self.Advance_action == self.actions[2]: # Action.RIGHT:
            self.BP_action = self.actions[2] # [3] # [2]
            next_diretion_trigar = [(self.actions[2]), (self.actions[3]), (self.actions[0]), (self.actions[1])]
            next_diretion_trigar_reverse = [(self.actions[3]), (self.actions[2]), (self.actions[0]), (self.actions[1])]
            # next_diretion_trigar_reverse = [(self.actions[2]), (self.actions[3]), (self.actions[0]), (self.actions[1])]
            # next_diretion_trigar = [(self.actions[3]), (self.actions[2]), (self.actions[0]), (self.actions[1])]

        else:
            next_diretion_trigar, next_diretion_trigar_reverse = self.next_direction_decision_prev_action()

        if trigar__or__reverse == "trigar":
            print("tigar__or__reverse : {}".format(trigar__or__reverse))
            return next_diretion_trigar
        if trigar__or__reverse == "reverse":
            print("tigar__or__reverse : {}".format(trigar__or__reverse))
            return next_diretion_trigar_reverse

    def next_direction_decision_prev_action(self):
        if self.prev_action == self.actions[0]: # Action.UP:
            self.BP_action = self.actions[1]
            next_diretion_trigar = [(self.actions[1]), (self.actions[0]), (self.actions[2]), (self.actions[3])]
            next_diretion_trigar_reverse = [(self.actions[0]), (self.actions[1]), (self.actions[2]), (self.actions[3])]

        elif self.prev_action == self.actions[1]: # Action.DOWN:
            self.BP_action = self.actions[0]
            next_diretion_trigar = [(self.actions[0]), (self.actions[1]), (self.actions[2]), (self.actions[3])]
            next_diretion_trigar_reverse = [(self.actions[1]), (self.actions[0]), (self.actions[2]), (self.actions[3])]

        elif self.prev_action == self.actions[2]: # Action.LEFT:
            self.BP_action = self.actions[3]
            next_diretion_trigar = [(self.actions[3]), (self.actions[2]), (self.actions[0]), (self.actions[1])]
            next_diretion_trigar_reverse = [(self.actions[2]), (self.actions[3]), (self.actions[0]), (self.actions[1])]

        elif self.prev_action == self.actions[3]: # Action.RIGHT:
            self.BP_action = self.actions[2]
            next_diretion_trigar = [(self.actions[2]), (self.actions[3]), (self.actions[0]), (self.actions[1])]
            next_diretion_trigar_reverse = [(self.actions[3]), (self.actions[2]), (self.actions[0]), (self.actions[1])]

        return next_diretion_trigar, next_diretion_trigar_reverse


    def advance_direction_decision(self, dir):

        
        test = random.sample(dir, len(dir))
        print("test dir : {}, dir : {}".format(test, dir))

        # test = [(self.actions[3]), (self.actions[1]), (self.actions[0]), (self.actions[1])]
        # test = [(self.actions[2]), (self.actions[1]), (self.actions[3]), (self.actions[0])]
        return test # random.shuffle(dir)


        #  [<Action.RIGHT: -2>, <Action.DOWN: -1>, <Action.UP: 1>, <Action.LEFT: 2>]
