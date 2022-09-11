import collections
import itertools


class Solution:

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        data = collections.defaultdict(int)
        for barcode in barcodes:
            data[barcode] += 1
        data_keys = collections.deque(
            sorted(list(data.keys()), key=lambda x: -data[x]))

        odd_list = []
        even_list = []
        is_odd_turn = True

        def get_next_list(getSmall=True):
            returnBigger = lambda a, b: a if len(a) >= len(b) else b
            returnSmaller = lambda a, b: a if len(a) < len(b) else b
            if getSmall:
                return returnSmaller
            return returnBigger

        while data_keys:
            current_turn = get_next_list()(odd_list, even_list)
            current_key = data_keys.popleft()
            for _ in range(data[current_key]):
                current_turn.append(current_key)

        big_list = get_next_list(False)(odd_list, even_list)
        small_list = get_next_list()(odd_list, even_list)
        third_list = []
        if len(big_list) - len(small_list) >= 2:
            big_list, third_list = big_list[:len(small_list
                                                )], big_list[len(small_list):]
        answer = []
        for i in range(len(big_list)):
            for any_list in (big_list, small_list, third_list):
                if i < len(any_list):
                    answer.append(any_list[i])
        return answer