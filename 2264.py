class Solution:
    def largestGoodInteger(self, num: str) -> str:
        if(len(num)<3):
            return ""
        ans = ""
        for i in range(len(num)-2):
            if len(set([num[i],num[i+1],num[i+2]]))==1:
                ans = max(ans, num[i])
        return ans*3
