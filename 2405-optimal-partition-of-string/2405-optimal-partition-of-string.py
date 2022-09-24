class Solution:

    def partitionString(self, s: str) -> int:
        start = 0
        end = 0
        visit = set()
        answer = 0
        while end < len(s):
            if s[end] in visit:
                answer += 1
                start = end
                visit = set()
            else:
                visit.add(s[end])
                end += 1
        if visit:
            answer += 1
        return answer