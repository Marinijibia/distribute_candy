class Solution:
    def candy(self, A):
        n = len(A)
        candies = [1] * n

        # Traverse from left to right
        for i in range(1, n):
            if A[i] > A[i-1]:
                candies[i] = candies[i-1] + 1

        # Traverse from right to left
        for i in range(n-2, -1, -1):
            if A[i] > A[i+1] and candies[i] <= candies[i+1]:
                candies[i] = candies[i+1] + 1

        return sum(candies)