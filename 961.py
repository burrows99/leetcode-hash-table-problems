class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        def f(array):
            n=len(array)
            d={}
            for i in range(n):
                if(array[i] not in d):
                    d[array[i]]=1
                else:
                    d[array[i]]+=1
            return(d)
        def F(array):
            two_n=len(array)
            n=int(two_n/2)
            Array=f(array)
            for i in Array:
                if(Array[i]==n):
                    return(i)
        return(F(A))
