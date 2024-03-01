class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = []
        for i in range(len(bank)):
            if bank[i].count("1") == 0:
                continue
            else:
                temp = bank[i].count("1")
                ans.append(temp)
        result = 0
        for i in range(len(ans) - 1):
            result += ans[i]*ans[i + 1]
        return result



