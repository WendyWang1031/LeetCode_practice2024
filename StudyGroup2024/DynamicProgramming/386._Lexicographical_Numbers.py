# 自己解 時間複雜度是 O(n log n)
class Solution1(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arr = []
        for i in range(1 , n+1):
            arr.append(i)
        
        arr.sort(key=str)
        print("final:" ,arr)
        return arr
    
solution1 = Solution1()
print(solution1.lexicalOrder(13))

#最佳解
class Solution2(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arr = []
        def dfs(current):
            if current > n :
                return
            arr.append(current)
            for i in range(10):
                next_num = current * 10 + i
                if next_num > n :
                    break
                dfs(next_num)

        for i in range (1,10):
            dfs(i)
        return arr
    
solution2 = Solution2()
print(solution2.lexicalOrder(13))