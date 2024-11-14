"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""

class Solution(object):
    def climbStairs_recursive(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 0:
            return 1
        return self.climbStairs_recursive(n-1)+self.climbStairs_recursive(n-2)
    
    def climbStairs_memoization(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        def climb(n):
            if n<= 1:
                return 1
            if n in memo:
                return memo[n]
            memo[n] = climb(n-1) + climb(n-2)
            return memo[n]
        return climb(n)
    
    def climbStairs_tabulation(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        dp = [0] * (n+1)
        dp[0] , dp[1] = 1 , 1
        for i in range(2 , n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    def climbStairs_SpaceOptimization(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        prev1 , prev2 = 1 , 1
        for _ in range(2 , n+1):
            current = prev1 + prev2
            prev2 , prev1 = prev1 , current

        return prev1
    
"""
解法 1：遞迴（Recursive）
時間複雜度：O(2^n)，因為每層遞迴分裂成兩次呼叫。
空間複雜度：O(n)，由於遞迴深度最多為 n。

解法 2：備忘錄（Memoization）
時間複雜度：O(n)，每一層的結果只計算一次並存儲。
空間複雜度：O(n)，備忘錄和遞迴深度最多為 n。
"""