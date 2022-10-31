
from lib2to3.pytree import Node
from sre_parse import State
import numpy as np
from itertools import count
import pprint




class Property():
    def __init__(self, *arg):

        
        self.pre = np.array([
                            

                            # [7, "g"],
                            # [8, "D"],
                            # [9, "C"],
                            # [11, "B"],
                            # [5, "A"],
                            # [5, "O"],
                            # [0, "s"]
                            [7, "g"],
                            [3, "D"],
                            # [9, "C"],
                            [10, "C"],
                            # [1, "B"],
                            # [7, "B"],
                            # [7.5, "B"],
                            [8, "B"],
                            # [4, "A"],
                            # [2.5, "A"],
                            [2.75, "A"],
                            [4, "O"],
                            # [6, "O"],
                            [0, "s"]

                            # [7, "g"],
                            # [3, "D"],
                            # [3, "C"],
                            # [6, "B"],
                            # [3, "A"],
                            # [4, "O"],
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

                # [0],
                # [5],
                # [8],
                # [10],
                # [4]

                # [0],
                # [5],
                # [8],
                # [11],
                # [4]
                # [0],
                # [7],
                # [15],
                # [26],
                # [30]
        ]

        return self.pre, Node, Arc, Arc_sum, PERMISSION

if __name__ == "__main__":
   test = Property()
   test.reference