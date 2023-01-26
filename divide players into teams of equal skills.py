class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        prev = skill[0] + skill[-1]
        chemistry = 0
        for i in range(len(skill) // 2):
            if skill[i] + skill[len(skill) - 1 - i] != prev:
                return -1
            prev = skill[i] + skill[len(skill) - 1 - i]
            chemistry += (skill[i] * skill[len(skill) - 1 - i])
        return chemistry
