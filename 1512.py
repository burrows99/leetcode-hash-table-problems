class Solution:
    def numIdenticalPairs(self, array: List[int]) -> int:
        n=len(array)
        d={}
        for i in range(n):
            if(array[i] not in d):
                d[array[i]]=[i]
            else:
                d[array[i]].append(i)
        ans=0
        for i in d:
            n=len(d[i])
            ans=ans+int(((n*(n-1))/2))
        return(ans)
