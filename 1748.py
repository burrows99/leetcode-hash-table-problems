class Solution:
    def sumOfUnique(self, array: List[int]) -> int:
        n=len(array)
        d={}
        for i in range(n):
            if(array[i] not in d):
                d[array[i]]=1
            else:
                d[array[i]]+=1
        ans=0
        for i in d:
            if(d[i]==1):
                ans=ans+i
        return(ans)
