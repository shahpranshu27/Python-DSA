class Solution:
    def fizzbuzz(self, n: int) -> list[str]:
        ans = []
        for i in range(1, n+1):
            if i%3==0 and i%5==0:
                ans.append("FizzBuzz")
            elif i%3==0:
                ans.append("Fizz")
            elif i%5==0:
                ans.append("Buzz")
            else:
                ans.append(i)
        return ans

obj = Solution()
result = obj.fizzbuzz(20)
print(result)