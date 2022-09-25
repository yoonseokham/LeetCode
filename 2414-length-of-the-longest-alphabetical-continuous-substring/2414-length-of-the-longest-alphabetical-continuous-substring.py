class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        index_dict = {}
        for index, char in enumerate("abcdefghijklmnopqrstuvwxyz"):
            index_dict[char] = index

        previous = -1
        current = 0
        local_answer = 1
        global_answer = 1
        for i in s:
            current = index_dict[i]
            if previous == -1:
                previous = current
            elif previous + 1 == current:
                local_answer += 1
                previous = current
            else:
                previous = current
                global_answer = max(global_answer, local_answer)
                local_answer = 1
        global_answer = max(global_answer, local_answer)
        return global_answer