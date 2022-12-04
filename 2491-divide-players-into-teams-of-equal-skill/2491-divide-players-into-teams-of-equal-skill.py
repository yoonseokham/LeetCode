import collections
class Solution:

    def dividePlayers(self, skill: List[int]) -> int:
        total_skill_sum = sum(skill)
        if total_skill_sum%(len(skill)//2):
            return -1
        each_team_sum = total_skill_sum//(len(skill)//2)
        skill.sort()
        start = 0
        end = len(skill) - 1
        answer = 0
        while start < end:
            if skill[start]+skill[end] == each_team_sum:
                answer += (skill[start]*skill[end])
                start += 1
                end -= 1
            else:
                return -1
        return answer
            