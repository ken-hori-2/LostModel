    
class Setting():

    def __init__(self, *arg):
        
        self.NODELIST = [

                

                # 一本道のシミュレーション
                # ["", "", "", "", "", "", "", "", "g", "", "", "", "", "", "", "", "g"],
                ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "g"],
                ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "x", "", "", "", "", "", "DorC", "", ""], # meeting ver.
                ["", "", "", "", "", "", "", "", "D", "", "", "", "", "", "C", "", ""], # 1024 meeting
                ["", "", "x", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "x", "", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "", "C", "", "", "", "", "", "", "", ""], # meeting ver. # 1024 meeting
                ["x", "", "x", "", "x", "", "x", "", "x", "", "x", "", "x", "", "x", "", ""],
                ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                ["", "", "x", "", "", "", "", "", "B", "", "", "", "", "", "B", "", ""],
                ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "", "A", "", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "", "O", "", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],

                ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "", "s", "", "", "", "", "", "", "", ""],

                # # add1016
                # # ["", "", "", "", "", "", "", "", "g", "", "", "", "", "", "", "", "g"],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "g"],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "DorC", "", ""],
                # ["", "", "", "", "", "", "", "", "D", "", "", "", "", "", "C", "", ""],
                # ["", "", "x", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "C", "", "", "", "", "", "", "", ""],
                # ["x", "", "x", "", "x", "", "x", "", "x", "", "x", "", "x", "", "x", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "x", "", "", "", "", "", "B", "", "", "", "", "", "B", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "A", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "O", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],

                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "s", "", "", "", "", "", "", "", ""],





                
                # ["", "", "", "", "", "", "", "", "", "", "g", "", "", "", "", "", "g"],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "x", "", ""],
                # ["", "", "x", "", "", "", "", "", "C", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["x", "", "x", "", "x", "", "x", "", "x", "", "x", "", "x", "", "x", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "x", "", "", "", "", "", "B", "", "", "", "", "", "x", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "A", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "s", "", "", "", "", "", "", "", ""],
                # ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ]

        self.ARCLIST = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        
        self.Observation = [
            
                
                

                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],

                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],

                # add 1007 # 一本道のシミュレーション用
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0, 0, 0,  0, 0, 0, 0, 0],
                
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0.7, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0.3, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0.8, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],

                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0, 0,  0, 0, 0, 0, 0],
                
                # case1
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0.4, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0.2, 0, 0, 0,  0, 0, 0, 0, 0],
                
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0.7, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0.3, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0.8, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],

                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                # [0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0, 0,  0, 0, 0, 0, 0],
                # case2
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0.4, 0, 0, 0,  0, 0, 0, 0, 0],
                
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0.7, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0.3, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0.8, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],

                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0.6, 0, 0, 0,  0, 0, 0, 0, 0],
        ]

        self.map = [
                

                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],

                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
        ]
        
        self.grid = [
                
                # [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
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
                # [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
                # [9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9],

                # [9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9],
                # [9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9],
                # [9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9],
                # [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],

                [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 0, 5, 0, 0],
                [0, 0, 5, 0, 0, 9, 0, 9, 5, 9, 0, 9, 9, 9, 0, 9, 9], # 9
                [9, 9, 0, 9, 9, 9, 9, 9, 0, 9, 9, 9, 0, 9, 0, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
                
                [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0],
                [0, 0, 5, 0, 0, 9, 0, 9, 5, 9, 0, 9, 0, 0, 5, 0, 0],
                [9, 9, 0, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 0, 9, 9],
                [9, 9, 0, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 0, 9, 9],
                [9, 9, 0, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 0, 9, 9],
                [9, 9, 0, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 0, 9, 9],
                [9, 9, 0, 0, 0, 0, 9, 9, 5, 9, 0, 0, 0, 0, 0, 9, 9], # 一本道
                # [9, 9, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9],
                [9, 0, 0, 0, 0, 0, 0, 9, 5, 9, 0, 0, 0, 0, 0, 0, 9], # 一本道
                # [9, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 9],
                [9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9],

                [9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9],
                [9, 0, 0, 0, 0, 0, 0, 9, 0, 9, 0, 0, 0, 0, 0, 0, 9],

                
                
        ]
        

    def call(self, *args):

        self.env_set = [self.NODELIST, self.ARCLIST, self.Observation, self.map, self.grid]

        return self.env_set

    def Infomation(self):
        
        return self.NODELIST, self.ARCLIST, self.Observation, self.map, self.grid

    def reset(self):

        import pprint

        # pprint.pprint(self.map)
        # self.map.__init__()

        return self.map