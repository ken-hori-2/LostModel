from enum import Enum
from pprint import pprint
from tkinter import FIRST
import numpy as np
import random

# import sys
# sys.path.append("/Users/ken/Desktop/model/src/Oneroad/explore/agent")

from sklearn import preprocessing

# from Env_full import Environment
# from environment import Environment
from environment_prob import Environment

# from bp_Algorithm import Algorithm_bp
from bp_1024_viz import Algorithm_bp # 戻る行動の可視化ver.

# from bp_Algorithm_re import Algorithm_bp_re

from exp_Algorithm import Algorithm_exp

from agent import Agent

# from setting import Setting
from setting_large_bp import Setting

import pprint

from advance_Algorithm import Algorithm_advance
# from advance_Algorithm_re import Algorithm_advance_re
# from exp_Algorithm_re import Algorithm_exp_re

from reference_match_rate import Property





def main():

    # Try 10 game.
    result = []
    little = []
    over = []
    goal_count = 0

    for test in range(1):

        set = Setting()

        NODELIST, ARCLIST, Observation, map, grid = set.Infomation()

        # refer = Property()
        # reference = refer.reference

        GOAL_STATE = [0, 2]

        test = [grid, map, NODELIST] # , GOAL_STATE]



        marking_param = 1
        
        # env = Environment(grid, NODELIST, map)
        env = Environment(*test)
        
        # agent = Agent(env, GOAL_STATE, NODELIST, map, grid)
        agent = Agent(env, marking_param, *test)



        STATE_HISTORY = []
        CrossRoad = []
            

            

    
        for x in range(5):
            print("=================== {} Steps\n===================".format(x))
            
            # Initialize position of agent.
            state = env.reset()

            demo = [state, env, agent, NODELIST, Observation] # , reference]

            Advance_action = Algorithm_advance(*demo)

            back_position = Algorithm_bp(*demo)

            explore_action = Algorithm_exp(*demo)

            # STATE_HISTORY = []
            TRIGAR = False
            OBS = []
            total_stress = 0
            # CrossRoad = []

            TOTAL_STRESS_LIST = []
            
            for i in range(20): # 4 戻るノードの個数以上は回す
                print("===================\n🐬🍏🍋test 0921 : {}\n===================".format(i))

                total_stress, STATE_HISTORY, state, TRIGAR, OBS, BPLIST, action, Add_Advance, GOAL, SAVE_ARC, CrossRoad, Storage, Storage_Stress = Advance_action.Advance(STATE_HISTORY, state, TRIGAR, OBS, total_stress, grid, CrossRoad, x)
                if GOAL:
                    print("探索済みのノード Storage : {}".format(Storage))
                    print("未探索のノード CrossRoad : {}".format(CrossRoad))
                    print("探索終了")
                    break

                print("\n============================\n🤖 🔛　アルゴリズム切り替え -> agent Back position\n============================")

                total_stress, STATE_HISTORY, state, OBS, BackPosition_finish = back_position.BP(STATE_HISTORY, state, TRIGAR, OBS, BPLIST, action, Add_Advance, total_stress, SAVE_ARC)

                if BackPosition_finish:
                    BackPosition_finish = False
                    print(" = 戻り切った状態 🤖🔚 {}回目".format(x+1))
                    # map, bplist reset
                    
                    ##### Storage を空にする # parameterをリセット
                    set = Setting()
                    map = set.reset()
                    test = [grid, map, NODELIST] # , GOAL_STATE]
                    env = Environment(*test)
                    # agent = Agent(env, *test)
                    # marking_param += 1
                    agent = Agent(env, marking_param, *test)
                    break
                    ####
                    # # demo = [state, env, agent, NODELIST, Observation]
                    # marking_param += 1
                    # agent = Agent(env, marking_param, *test)
                    # # env = Environment(*test)
                    # demo = [state, env, agent, NODELIST, Observation]
                    # back_position_re = Algorithm_bp_re(*demo)
                    # explore_action_re = Algorithm_exp_re(*demo)
                    # Advance_action_re = Algorithm_advance_re(*demo)
                    # pprint.pprint(map)
                    # print("探索済みのノード Storage : {}".format(Storage))
                    # print("未探索のノード CrossRoad : {}".format(CrossRoad))
                    # print("戻れる場所に戻って再度探索\n\n\n\n\n\n\n\n\n\n")
                    # # Add_Advance = False
                    # Storage.append(state)
                    # # Re_first = True
                    # for re in range(5):
                    #     Re_first = True
                    #     total_stress, STATE_HISTORY, state, Storage_Stress, BackPosition_finish = back_position_re.BP_re(STATE_HISTORY, state, TRIGAR, Storage_Stress, Storage, action, Add_Advance, total_stress, SAVE_ARC, Storage, CrossRoad, Storage_Stress, Re_first)
                    #     total_stress, STATE_HISTORY, state, TRIGAR, CrossRoad, GOAL = explore_action_re.Explore_re(STATE_HISTORY, state, TRIGAR, total_stress, grid, Storage, CrossRoad, x=re)
                    #     if GOAL:
                    #         print("探索済みのノード Storage : {}".format(Storage))
                    #         print("未探索のノード CrossRoad : {}".format(CrossRoad))
                    #         print("探索終了")
                    #         break
                        
                    #     total_stress, STATE_HISTORY, state, TRIGAR, Storage_Stress, Storage, action, Add_Advance, GOAL, SAVE_ARC, CrossRoad, Storage, Storage_Stress = Advance_action_re.Advance_re(STATE_HISTORY, state, TRIGAR, Storage, Storage_Stress, total_stress, grid, CrossRoad, x=re)
                    #     print("戻れる場所に戻って再度探索終了\n\n\n\n\n\n\n\n\n\n")
                    #     if GOAL:
                    #         print("探索済みのノード Storage : {}".format(Storage))
                    #         print("未探索のノード CrossRoad : {}".format(CrossRoad))
                    #         print("探索終了")
                    #         break
                    #     if BackPosition_finish:
                    #         BackPosition_finish = False
                    #         break
                    # break
                
                print("============\n=🤖　🌟　⚠️ =\n============")
                print("\n============================\n🤖 🔛　アルゴリズム切り替え -> agent Explore\n============================")

                total_stress, STATE_HISTORY, state, TRIGAR, CrossRoad, GOAL = explore_action.Explore(STATE_HISTORY, state, TRIGAR, total_stress, grid, CrossRoad, x)

                if GOAL:
                    print("探索済みのノード Storage : {}".format(Storage))
                    print("未探索のノード CrossRoad : {}".format(CrossRoad))
                    print("探索終了")
                    break

                print("\n============================\n🤖 🔛　アルゴリズム切り替え -> agent Advance\n============================")

            print("Episode {}: Agent gets {} stress.".format(i, total_stress))
            print("state_history : {}".format(STATE_HISTORY))

            if GOAL:
                print(" {} 回目".format(x+1))
                goal_count += 1
                break

            # total_stress, STATE_HISTORY = explore_action.Explore()

        import pandas as pd
        import numpy as np

        df = pd.Series(data=STATE_HISTORY)
        df = df[df != df.shift(1)]
        print('-----削除後データ----')
        print("Steps:{}".format((len(df))))
        result.append((len(df)))
        if len(df) <= 100:
            little.append(len(df))

        if len(df) >= 1000:
            over.append(len(df))

    print(result)
    # print(result/100)
    print("最小:{}".format(min(result)))
    print("最大:{}".format(max(result)))
    print("150 以内 : {}".format(len(little)))
    print("1000以上 : {}".format(len(over)))
    print("goal : {}".format(goal_count))


if __name__ == "__main__":
    main()
