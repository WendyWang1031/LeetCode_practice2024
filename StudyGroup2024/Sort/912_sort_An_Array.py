# 自己解
class Solution1(object):
    def bubble_sort(self, nums):
        n = len(nums)
        for i in range (n):
            swapped = False
            for j in range (0 , n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j+1] , nums[j] = nums[j] , nums[j+1]
                    swapped = True
            if not swapped:
                break
        return nums

solution = Solution1()
arr1 = [5,1,1,2,0,0]
result = solution.bubble_sort(arr1)
print(result)

# 最佳解其一：Quick Sort
class Solution2(object):
    def sortArray(self, nums):
        def quicksort(arr):
            if len(arr) <=1:
                return arr
            
            pivot = arr[len(arr) // 2]
            left = []
            middle = []
            right =[]

            for x in arr:
                if x < pivot:
                    left.append(x)
                elif x == pivot:
                    middle.append(x)
                elif x > pivot:
                    right.append(x)

            return quicksort(left) + middle + quicksort(right)
        return quicksort(nums)

solution = Solution2()
arr2 = [5,1,1,2,0,0]
result = solution.sortArray(arr2)
print(result)