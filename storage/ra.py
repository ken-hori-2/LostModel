from enum import Enum
from random import random

import random
from turtle import done
class State():

    def __init__(self, row=-1, column=-1):
        self.row = row
        self.column = column

    def __repr__(self):
        
        return "[{}, {}]".format(self.row, self.column)

    def clone(self):
        return State(self.row, self.column)

    def __hash__(self):
        return hash((self.row, self.column))

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column
        
class Action(Enum):
    UP = 1
    DOWN = -1
    LEFT = 2
    RIGHT = -2

class Enviroment():

    def __init__(self, grid, NODELIST):
        
        self.agent_state = State()
        self.reset()

        self.grid = grid

        self.NODELIST = NODELIST

        self.default_stress = 1

    @property
    def row_length(self):
        return len(self.grid)

    @property
    def column_length(self):
        return len(self.grid[0])

    @property
    def actions(self):
        return [Action.UP, Action.DOWN,
                Action.LEFT, Action.RIGHT]

    def reset(self):
        self.agent_state = State(22, 8)
        # self.agent_state = State(6, 0)
        return self.agent_state

    def can_action_at(self, state):
        if self.grid[state.row][state.column] == 0 or self.grid[state.row][state.column] == 5:
            return True
        else:
            return False

    def _move(self, state, action, TRIGAR):
        if not self.can_action_at(state):
            raise Exception("Can't move from here!")

        next_state = state.clone()

        # Execute an action (move).
        if action == Action.UP:
            next_state.row -= 1
            # next_state.row += 1
        elif action == Action.DOWN:
            # next_state.row -= 1
            next_state.row += 1
        elif action == Action.LEFT:
            # next_state.column += 1
            next_state.column -= 1
        elif action == Action.RIGHT:
            # next_state.column -= 1
            next_state.column += 1

        

        # Check whether a state is out of the grid.
        if not (0 <= next_state.row < self.row_length):
            next_state = state
            
        if not (0 <= next_state.column < self.column_length):
            next_state = state
            

        # Check whether the agent bumped a block cell.
        if self.grid[next_state.row][next_state.column] == 9:
            next_state = state

        stress, done = self.stress_func(next_state, TRIGAR)
        # return next_state, stress, done

        return next_state, stress, done

    def stress_func(self, state, TRIGAR):
       
        done = False

        # Check an attribute of next state.
        attribute = self.NODELIST[state.row][state.column]

        if attribute == 1:
            print("GOAL !!!!!!!!!")
            done = True

        # if TRIGAR:
        #     stress = -self.default_stress
        # else:
            
        #     if attribute > 0.0:
        #         # Get reward! and the game ends.
        stress = 0 # -1 # 0                              # ここが reward = None の原因 or grid の 1->0 で解決
        #     else:
        #         stress = self.default_stress


        return stress, done

class Agent():

    def __init__(self, env): # , GOAL_STATE):
        self.actions = env.actions
        

    def policy(self, state, TRIGAR):
        
        # if random.random() < 0.3: # epsilon:
        return random.choice(self.actions)
        # else:
        #     # if not state.column == self.goal[1]:
        #     #     if state.column > self.goal[1]:
        #     #         return (self.actions[2])
        #     #     elif state.column < self.goal[1]:
        #     #         return (self.actions[3])
        #     # if state.row < self.goal[0]:
        #     return (self.actions[0])
    # def get_action(s, epsilon):

    #     # 行動を決める
    #     next_direction = -1
        
    #     # εの確率でランダムに動く
    #     if random.random() < epsilon:
    #         while True:
    #             next_direction = random.randint(0, 3)
    #             if pi[s][next_direction] > 0:
    #                 break
                
    #     # Qの最大値の行動を採用する
    #     else:
    #         max_action = max(Q[s])
    #         next_direction = Q[s].index(max_action)

    #     # 行動をindexに
    #     if next_direction == DIR_UP:
    #         action = 0
    #     elif next_direction == DIR_RIGHT:
    #         action = 1
    #     elif next_direction == DIR_DOWN:
    #         action = 2
    #     elif next_direction == DIR_LEFT:
    #         action = 3
    #     return action

    

def main():

    # Try 10 game.
    result = []
    little = []
    over = []

    for test in range(101):

        total_stress = 0
        TRIGAR = False
        theta_list = [0]*5 # [] # [0]*20
        lost = False
        done = False

        GOAL_STATE = [0, 2]

        NODELIST = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # start
        ]
        
        # grid = [
        #     [0, 9, 0, 9, 0, 0],
        #     [0, 0, 0, 9, 0, 0],
        #     [0, 9, 0, 0, 0, 9],
        #     [0, 9, 0, 9, 0, 0],
        #     [0, 9, 0, 9, 9, 0],
        #     [0, 0, 0, 0, 0, 0],
        #     [0, 9, 0, 9, 0, 0]
        # ]
        grid = [
                    # [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 7],
                    # [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
                    # [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
                    # [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
                    # [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
                    # [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 0, 5, 0, 0],
                    # [0, 0, 5, 0, 0, 9, 0, 0, 5, 0, 0, 9, 9, 9, 0, 9, 9], # 9
                    # [9, 9, 0, 9, 9, 9, 9, 9, 0, 9, 9, 9, 0, 9, 0, 9, 0],
                    # [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
                    # [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
                    
                    # [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
                    # [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
                    # [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
                    # [0, 0, 5, 0, 0, 9, 0, 0, 5, 0, 0, 9, 0, 0, 5, 0, 0],
                    # [9, 9, 0, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 0, 9, 9],
                    # [9, 9, 0, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 0, 9, 9],
                    # [9, 9, 0, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 0, 9, 9],
                    # [9, 9, 0, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 0, 9, 9],
                    # [9, 9, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 9, 9],
                    # [9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9],
                    # [9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9],
                    # [9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9],
                    # [9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9],

                    [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
                    [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
                    [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
                    [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
                    [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
                    [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 0, 5, 0, 0],
                    [0, 0, 5, 0, 0, 9, 0, 0, 5, 0, 0, 9, 9, 9, 0, 9, 9], # 9
                    [9, 9, 0, 9, 9, 9, 9, 9, 0, 9, 9, 9, 0, 9, 0, 9, 0],
                    [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
                    [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
                    
                    [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
                    [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
                    [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
                    [0, 0, 5, 0, 0, 9, 0, 0, 5, 0, 0, 9, 0, 0, 5, 0, 0],
                    [9, 9, 0, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 0, 9, 9],
                    [9, 9, 0, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 0, 9, 9],
                    [9, 9, 0, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 0, 9, 9],
                    [9, 9, 0, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 0, 9, 9],
                    [9, 9, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 9, 9],
                    [9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9],
                    [9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9],
                    [9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9],
                    [9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9],

                    [9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9],
                    [9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9],
                    [9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]


        env = Enviroment(grid, NODELIST)
        
        agent = Agent(env) #, GOAL_STATE)
        
        state = env.reset()

        state_history = []
        print(state)
        state_history.append(state)

        
        i = 0
        while not done:
            print("\n========== 🌟 {}steps ==========".format(i+1))
            print(f"🤖 State:{state}")

            # try:
            action = agent.policy(state, TRIGAR)
            next_state, stress, done = env._move(state, action, TRIGAR)
            prev_state = state # 1つ前のステップを保存 -> 後でストレスの減少に使う
            state = next_state
            # print(state)
            state_history.append(state)
            # except:
            #     print("エラーメッセージ")

            # print(f"🤖 next State:{state}")
            print(f"Total Stress:{total_stress}")
            i += 1
        print(f"🤖 State:{state}")

            
        print(state_history)


        import pandas as pd
        import numpy as np

        df = pd.Series(data=state_history)
        df = df[df != df.shift(1)]
        print('-----削除後データ----')
        print("Steps:{}".format((len(df))))
        result.append((len(df)))
        if len(df) <= 150:
            little.append(len(df))

        if len(df) >= 1000:
            over.append(len(df))

    print(result)
    # print(result/100)
    print("最小:{}".format(min(result)))
    print("最大:{}".format(max(result)))
    print("150 以内 : {}".format(len(little)))
    print("1000以上 : {}".format(len(over)))

main()