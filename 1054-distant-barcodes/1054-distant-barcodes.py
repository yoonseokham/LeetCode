import collections
import itertools

class Solution:

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        data = collections.defaultdict(int)
        for barcode in barcodes:
            data[barcode] += 1
        data_keys = collections.deque(sorted(list(data.keys()),key = lambda x :-data[x]))
        
        odd_list = []
        even_list = []
        is_odd_turn = True
        
        def get_append_list(odd_list,even_list):
            return odd_list if len(odd_list) < len(even_list) else even_list
        def get_overflow_list(odd_list,even_list):
            return odd_list if len(odd_list) >= len(even_list) else even_list
        
        while data_keys:
            current_turn = get_append_list(odd_list,even_list)
            current_key = data_keys.popleft()
            for _ in range(data[current_key]):
                current_turn.append(current_key)
        
        over_flow_list = get_overflow_list(odd_list,even_list)
        small_list = get_append_list(odd_list,even_list)
        third_list = []
        if len(over_flow_list) - len(small_list) >= 2:
            over_flow_list, third_list = over_flow_list[:len(small_list)],over_flow_list[len(small_list):]
        print(small_list)
        print(over_flow_list)
        print(third_list)
        answer = []
        for i in range(len(over_flow_list)):
            for any_list in (over_flow_list,small_list,third_list):
                if i < len(any_list):
                    answer.append(any_list[i])
        return answer
                    
        
        '''
        [1,1,1,2,2,2]
        [1,1,1,1,2,2,3,3]
        [1]
        [1,1,2]
        [1,2,2,2,4,4]
        [7,7,7,8,5,7,5,5,5,8]
        '''