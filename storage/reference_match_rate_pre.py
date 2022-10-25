
from lib2to3.pytree import Node
from sre_parse import State
import numpy as np
from itertools import count
import pprint




class Property():
    def __init__(self, *arg):

        # self.Pre = arg[0]
        # self.Act = arg[1]
        # self.env = arg[2]
        # self.Arc = arg[3]
        self.pre = np.array([
                            # [2, "g"],
                            # [3, "C"],
                            # [1, "B"],
                            # [2, "A"],
                            # [0, "s"]
                            # [2, "g"],
                            # [3, "C"],
                            # [2, "B"],
                            # [3, "A"],
                            # [0, "s"]

                            # [5, "g"],
                            # [6, "D"],
                            # [5, "C"],
                            # [1, "B"],
                            # [3, "A"],
                            # [0, "s"]

                            # [4.2, "g"],
                            # [2.8, "D"],
                            # [3.2, "C"],
                            # [4.5, "B"],
                            # [3.2, "A"],
                            # [0, "s"]

                            [8.2, "g"],
                            [6, "D"],
                            [7, "C"],
                            [7.5, "B"],
                            [3.2, "A"],
                            [0, "s"]

                            # [8.2, "g"],
                            # [7, "C"],
                            # [7.5, "B"],
                            # [3.2, "A"],
                            # [0, "s"]


                            # [5, "g"],
                            # [6, "C"],
                            # [3, "B"],
                            # [2, "A"],
                            # [0, "s"]
                            ])

    
    def reference(self):
        
        
        Node = self.pre[:, 1]
        Arc = self.pre[:, 0]
        print(Node)
        print(Arc)
        Node = Node.tolist()
        Arc = Arc.tolist()
        num = [float(i) for i in Arc]
        print(type(num))
        Arc_sum = sum(num)
        print(Arc_sum)

        PERMISSION = [
                # [0],
                # [2],
                # [5],
                # [7],
                # [10]
                # [Arc_sum-int(Arc[4])-int(Arc[3])-int(Arc[2])-int(Arc[1])-int(Arc[0])],
                # [Arc_sum-int(Arc[4])-int(Arc[3])-int(Arc[2])-int(Arc[1])],
                # [Arc_sum-int(Arc[4])-int(Arc[3])-int(Arc[2])],
                # [Arc_sum-int(Arc[4])-int(Arc[3])],
                # [Arc_sum-int(Arc[4])],
                # [Arc_sum]
                # [Arc_sum-float(Arc[4])-float(Arc[3])-float(Arc[2])-float(Arc[1])-float(Arc[0])],
                # [Arc_sum-float(Arc[4])-float(Arc[3])-float(Arc[2])-float(Arc[1])],
                # [Arc_sum-float(Arc[4])-float(Arc[3])-float(Arc[2])],
                # [Arc_sum-float(Arc[4])-float(Arc[3])],
                # [Arc_sum-float(Arc[4])],
                # [Arc_sum]

                # [0],
                # [5],
                # [5],
                # [5],
                # [5],
                # [8]


                # [0],
                # [10],
                # [10],
                # [12],
                # [20],
                # [30]
                [Arc_sum-float(Arc[5])-float(Arc[4])-float(Arc[3])-float(Arc[2])-float(Arc[1])-float(Arc[0])],
                [Arc_sum-float(Arc[5])-float(Arc[4])-float(Arc[3])-float(Arc[2])-float(Arc[1])],
                [Arc_sum-float(Arc[5])-float(Arc[4])-float(Arc[3])-float(Arc[2])],
                [Arc_sum-float(Arc[5])-float(Arc[4])-float(Arc[3])],
                [Arc_sum-float(Arc[5])-float(Arc[4])],
                [Arc_sum-float(Arc[5])],
                [Arc_sum]

                # [0],
                # [7],
                # [8],
                # [11],
                # [4]
        ]

        return self.pre, Node, Arc, Arc_sum, PERMISSION