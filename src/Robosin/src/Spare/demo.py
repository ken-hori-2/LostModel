
import copy

class cal():

    def __init__(self):
        self.SAVE_ARC = [1, 2, 3, 4, 5]
        # self.SAVE_ARC = [1, 2, 3]
        self.result_list = []
    
    def test(self):

        result = 0
        
        num = copy.copy(self.SAVE_ARC) # 値渡し/深いコピー

        for x in self.SAVE_ARC:
            print(f"num : {num}")
            print(f"SAVE ARC : {self.SAVE_ARC}")
            result = 0
            for number in num:
                result += number
            
            self.result_list.append(result)
            num.pop(0)
            
        print(self.result_list)


if __name__ == "__main__":

    demo = cal()

    demo.test()