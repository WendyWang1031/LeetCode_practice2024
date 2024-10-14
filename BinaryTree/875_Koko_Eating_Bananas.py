"""
Koko loves to eat bananas. There are n piles of bananas, 
the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, 
she chooses some pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, 
she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23

"""
import math
# 新手解
class Solution1(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        k = 1
        
        while True:
            hours_needed = 0

            for pile in piles:
                hours_needed += math.ceil(pile/k) # (pile + k -1 ) // k 用這個計算方式也可以取整

            if hours_needed <= h:
                return k
            
            k+=1

solution = Solution1()
piles1 = [3, 6, 7, 11]
h1 = 8
result = solution.minEatingSpeed(piles1,h1)
print(result)

piles2 = [30,11,23,4,20]
h2 = 5
result = solution.minEatingSpeed(piles2,h2)
print(result)

piles3 = [30,11,23,4,20]
h3 = 6
result = solution.minEatingSpeed(piles3,h3)
print(result)

# 最佳解
class Solution(object):
    def minEatingSpeed(self, piles, h):
        left , right = 1, max(piles)
        
        while left <= right:
            mid = (left + right) // 2
            hours_needed = 0

            for pile in piles:
                hours_needed += (pile + mid - 1) // mid

            if hours_needed <= h:
                right = mid - 1
            else:
                left = mid + 1

        return left


solution = Solution()
piles1 = [3, 6, 7, 11]
h1 = 8
result = solution.minEatingSpeed(piles1,h1)
print(result)

piles2 = [30,11,23,4,20]
h2 = 5
result = solution.minEatingSpeed(piles2,h2)
print(result)

piles3 = [30,11,23,4,20]
h3 = 6
result = solution.minEatingSpeed(piles3,h3)
print(result)