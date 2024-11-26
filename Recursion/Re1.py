# class Solution:
      
#     def printNos(self,N):
#         if N == 0:
#             return
#         self.printNos(N-1)
#         print(N, end=" ")
    
# sol1 = Solution()
# sol1.printNos(10)

def printNos(n):
    if n==0:
        return 
    printNos(n-1)
    print(n, end=" ")

printNos(5)

'''
Recursion -> function calls itself inside the function, until specified condition is fulfilled

StackOverflow in Recursion -> When the base condition is not specified, the function calls itself indefinately. This leads to the condition known as stack overflow, where the memory limit exceeds.
'''