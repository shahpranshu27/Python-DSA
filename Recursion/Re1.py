class Solution:
      
    def printNos(self,N):
        #Your code here
        if N == 0:
            return
        self.printNos(N-1)
        print(N, end=" ")
    
sol1 = Solution()
sol1.printNos(10)