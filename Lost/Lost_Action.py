from numpy import average
import random
import pprint
from environment_prob import Environment

# self.actions[0] -> i =  1 (â)UP
# self.actions[1] -> i = -1 (â)DOWN
# self.actions[2] -> i =  2 (â)LEFT
# self.actions[3] -> i = -2 (â)RIGHT

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

        # print("\n----- ð¤ð agent policy -----")

        # self.explore_actionã®ä¸­ããé¸æ
        # ä»åã¯å·¦å³æ¹åãããã ã£ãå ´å
        print("Average Value [â¬ï¸ â¬ï¸ â¬ï¸ â¡ï¸ ] : {}".format(Average_Value))
        self.demo = []
        for x in self.demo_index:
            self.demo.append(Average_Value[x])
        print("[â¬ï¸ â¡ï¸ â¬ï¸ ] : {}".format(self.demo))


        
        try:
            print("\n==============================================\n â ï¸ãåè¡åãã¨ã®å¹³åä¾¡å¤ãä¸çªå¤§ããè¡åãé¸æ\n==============================================")
            maxIndex = [i for i, x in enumerate(Average_Value) if x == max(Average_Value)]
            # print("\nMAX INDEX_0 : {}".format(maxIndex))
            if len(maxIndex) > 1:
                print("å¹³åä¾¡å¤ã®æå¤§ãè¤æ°åããã¾ãã")
                maxIndex = [random.choice(maxIndex)]
                print("ã©ã³ãã ã§ Average_Value{} = {} ãé¸æãã¾ããã".format(maxIndex, self.Action[maxIndex[0]]))
            else:
                print("å¹³åä¾¡å¤ã®æå¤§ãä¸ã¤ããã¾ãã")
            next_action = self.Action[maxIndex[0]]
            print("æ¬¡ã®è¡åAt : {}, t-1ã¾ã§ã®å¹³åä¾¡å¤ : {}".format(next_action, max(Average_Value)))
        # except:
        except Exception as e:
            print(Average_Value)
            print('=== ã¨ã©ã¼åå®¹ ===')
            print('type:' + str(type(e)))
            print('args:' + str(e.args))
            print('message:' + e.message)
            print('eèªèº«:' + str(e))
            print("ERROR")
            next_action = random.choice(self.Action)
            print("ã©ã³ãã ã§ {} ãé¸æãã¾ããã".format(next_action))


        return next_action

    def value(self):
        print("\n======================\n â ï¸ è¡åãã¨ã«ä¾¡å¤è¨ç®\n======================\n")

        print("ð Episode[Action, Rt] : {}".format(self.Episode_0))
        # ããã§æ¯åãªã»ããããªãã¨ååã®ç·åã®è¨ç®çµæãå¼ãç¶ãã§ãã¾ã
        self.Value = [0]*self.action_length # 4
        print("len = {}".format(len(self.Episode_0[0])))
        self.L_0 = [len(self.Episode_0[0])]*self.action_length # 4
       
        for i in range(len(self.Episode_0[0])):

            if self.Episode_0[0][i] ==  self.UP:                        # é¡ä¼¼ã¨ãã½ã¼ãã®ä¸­ã®è¡åãã¨ã«åé¡ (Episode_2 = prev_action = LEFT)
                # print("ð")
                self.Value[0] += self.Episode_0[1][i]                     # ãã®é¡ä¼¼ã¨ãã½ã¼ãã®æã®è¡åã®çµæã®ä¾¡å¤ãå ç®
            if self.Episode_0[0][i] == self.DOWN:
                # print("ð ð")
                self.Value[1] += self.Episode_0[1][i]
            
            if self.Episode_0[0][i] ==  self.LEFT:
                # print("ð ð ð")
                self.Value[2] += self.Episode_0[1][i]
            if self.Episode_0[0][i] == self.RIGHT:
                # print("ð ð ð ð")
                self.Value[3] += self.Episode_0[1][i]
            

        print("================================\n â ï¸ãV = åè¡åå¾ã«å¾ãå ±é¬ã®ç·å\n================================")
        print(" Value :{}, Length : {}".format(self.Value, self.L_0))
        try:
            # print("ã¨ã©ã¼ã§ã¯ãªãï¼ï¼ï¼ï¼ï¼")
            Average_Value = [self.Value[x] / self.L_0[x] for x in range(len(self.Value))]
        except:
            # print("ã¨ã©ã¼ï¼ï¼ï¼ï¼ï¼")
            Average_Value = self.Value
        print("\nä¾¡å¤ Value [UP, DOWN, LEFT, RIGHT] = {}, <<{} åä¸­>>".format(self.Value, len(self.Episode_0[0])))
        print("ä¾¡å¤ã®å¹³å[UP, DOWN, LEFT, RIGHT] : {}".format(Average_Value))
        

        

        return Average_Value

    def save_episode(self, action):
        # ä»åã¯ä¸ã¨å·¦æ¹åã«é²ãã æã«0.5ã®ç¢ºçã§ã¹ãã¬ã¹ãæ¸ãããåæ
        # ããã«ã¯ãè¡åã®çµæNodeâ­ï¸ãçºè¦ã§ãããã©ããã®æå ±ãç¨ãã
        print("\n=============\n â ï¸ çµæã®ä¿å­ \n=============\n")
        
        
        if action == self.UP:
            print("â¡ï¸ UP Rt = 1")

            self.Episode_0[0].append(action)
            # self.Episode_0[1].append(1) # ä»ã¯æ¬¡ã®è¡åã§å¿ãçºè¦ã§ããåæ(R = 1)
            self.Episode_0[1].append(random.choice([0, 1])) # 0.5ã®ç¢ºçã§ãã¼ãçºè¦ == æ°ããæå ±ãå¾ããã == ã¹ãã¬ã¹è»½æ¸
            print("ð [â¬ï¸ã(1) , â¬ï¸ã(-1) , â¬ï¸ã(2) , â¬ï¸ã(-2) ], [Rt] : ") # {}".format(self.Episode_0))
            pprint.pprint(self.Episode_0)
           
        elif action == self.LEFT:
            print("â¡ï¸ LEFT Rt = 1")

            self.Episode_0[0].append(action)
            # self.Episode_0[1].append(1) # ä»ã¯æ¬¡ã®è¡åã§å¿ãçºè¦ã§ããåæ(R = 1)
            self.Episode_0[1].append(random.choice([0, 1])) # 0.5ã®ç¢ºçã§ãã¼ãçºè¦ == æ°ããæå ±ãå¾ããã == ã¹ãã¬ã¹è»½æ¸
            print("ð [â¬ï¸ã(1) , â¬ï¸ã(-1) , â¬ï¸ã(2) , â¬ï¸ã(-2) ], [Rt] : ") # {}".format(self.Episode_0))
            pprint.pprint(self.Episode_0)
        else:
            self.Episode_0[0].append(action)
            self.Episode_0[1].append(0)


        print("\nãã¼ãçºè¦ == æ°ããæå ±ãå¾ããã == ã¹ãã¬ã¹è»½æ¸ ã§ããæ¹åãä¿å­")

        

        return self.Episode_0




def main():

    UP = 1
    DOWN = -1
    LEFT = 2
    RIGHT = -2
    
    # ç®å°ãçºè¦ãã¦ããéãã¯è¡åãç¶ç¶ãã¦ãã(ã¤ã¾ããæªçºè¦ã«ãªã£ã¦åãã¦æ¹åãå¤ãã)ã¨ä»®å®ããã¨ãAt-1ã§æ»ãæããã®åã®At-2ãæ»ãæ¹åã¨åã
    
    Average_list = []
    
    RESULT = []
    data = []


    print("\n------------START------------\n")
    # ã³ããã¯ãã¼ã¿ããã¨ã«è¡åãã©ã®ããã«ãªããã®å®é¨
                
    test = [[0], [0], [0]]
    env = Environment(*test)
    agent = Agent(env)


    for epoch in range(1, 10):
        print("\n\n############### {}steps ###############\n\n".format(epoch))

        
        ##############
        Average_Value = agent.value()
        ##############


        print("\n===================\nð¤â¡ï¸ Average_Value:{}".format(Average_Value))
        

        print(" == åè¡åå¾ã«ã¹ãã¬ã¹ãæ¸ãããç¢ºç:{}".format(Average_Value))
        print(" == ã¤ã¾ããæ°ããæå ±ãå¾ãããç¢ºç:{} -----> ãããä¸çªéè¦ã»ã»ã»æªæ¢ç´¢ãã¤ãã®æ°å¤ãå¤§ããæ¹åã®è¡åãé¸æ\n===================\n".format(Average_Value))
        Average_list.append(Average_Value)
        
        ##############
        action = agent.policy(Average_Value)
        ##############
        


        if action==  LEFT:
            NEXT = "LEFT  â¬ï¸"
            print("    At :-> {}".format(NEXT))
        if action == RIGHT:
            NEXT = "RIGHT â¡ï¸"
            print("    At :-> {}".format(NEXT))  
        if action ==  UP:
            NEXT = "UP    â¬ï¸"
            print("    At :-> {}".format(NEXT))
        if action == DOWN:
            NEXT = "DOWN  â¬ï¸"
            print("    At :-> {}".format(NEXT))
        

        
        print("\n---------- â ï¸  {}è©¦è¡å¾ã®çµæ----------".format(epoch))
        
        print("éå»ã®ã¨ãã½ã¼ããããç¾æç¹ã§ã¯ãð¤â ï¸ At == {}ãé¸æãã".format(action))
        # Z = é¡ä¼¼ã¨ãã½ã¼ã
        
        ##############
        Episode_0 = agent.save_episode(action)
        ##############


        data.append(action)

    print("\n---------- â ï¸  è©¦è¡çµäº----------")
    
    print("å¹³åä¾¡å¤[å·¦ããNåç®]\n")
    print("Value(â¬ï¸ â¬ï¸ â¬ï¸ â¡ï¸ ) : ")
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