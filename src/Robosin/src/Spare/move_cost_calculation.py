
import copy

# class cal():
class move_cost_cal():

    def __init__(self, data):
        # self.SAVE_ARC = [1, 2, 3, 4, 5]
        # self.SAVE_ARC = [1, 2, 3]

        self.SAVE_ARC = data
        self.result_list = []
    
    def test(self):

        result = 0
        
        num = copy.copy(self.SAVE_ARC) # 値渡し/深いコピー

        # first = True

        for x in self.SAVE_ARC:
            print(f"num : {num}")
            print(f"SAVE ARC : {self.SAVE_ARC}")
            result = 0
            # if first:
            #     first = False
            # else:
            for number in num:
                result += number
        
            self.result_list.append(result)
            num.pop(0)

        print(self.result_list)

        return self.result_list


if __name__ == "__main__":

    # demo = cal()
    data = [1, 2, 3, 4, 5]
    demo = move_cost_cal(data)

    demo.test()