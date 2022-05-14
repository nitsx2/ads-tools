import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums)-1)
        return nums            
    
    
    def quicksort(self, nums, start, end):
        if start >= end: return

        def get_pivot_index():
            randomindex = random.randint(start, end)
            nums[randomindex], nums[end] = nums[end], nums[randomindex]
            pivotindex  = end
            cpi = start

            for j in range(start, end):
                if nums[j] <= nums[pivotindex]:
                    nums[cpi], nums[j] = nums[j], nums[cpi]
                    cpi += 1

            nums[cpi], nums[pivotindex] = nums[pivotindex], nums[cpi]
            return cpi    

        pivot = get_pivot_index()
        self.quicksort(nums, start, pivot-1)
        self.quicksort(nums, pivot+1, end)
        


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergesort(nums)

    
    
    def mergesort(self, nums):
        n = len(nums)
        if n < 2: return nums
        
        mid = n // 2 
        
        part1 = nums[0:mid]
        part2 = nums[mid:]
        
        sorted1 = self.mergesort(part1)
        sorted2 = self.mergesort(part2)
        
        def merge_two_sorteds(nums1, nums2):
            i = j = k = 0
            n, m = len(nums1), len(nums2) 
            res = [0]*(n+m)
            
            while i < n and j < m:
                if nums1[i] < nums2[j]:
                    res[k] = nums1[i]
                    i += 1
                    k += 1
                else:
                    res[k] = nums2[j]
                    j += 1
                    k += 1
            
            while i < n:
                res[k] = nums1[i]
                i += 1
                k += 1
            
            while j < m:
                res[k] = nums2[j]
                j += 1
                k += 1
            
            return res
                    
        
        return merge_two_sorteds(sorted1, sorted2)



class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def insertion(n):
            for j in range(1, n):
                i = j-1
                key = nums[j]
                while i > 0 and nums[i] > key:
                    nums[i+1] = nums[i]
                    i -= 1
                
                nums[i+1] = key
            return nums
        
        n = len(nums)
        insertion(n)
        return nums


class Solution: # find min one by one #less swaps 
    def selection(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        for i in range(n):
            minindex = i
            for j in range(i+1, n):
                if nums[j] < nums[minindex]:
                    minindex = j
                    
            nums[minindex], nums[i] = nums[i], nums[minindex]
            
        return nums 



def bubblesort(self, nums: List[int]) -> List[int]:
    #sort using pairs @ sort using adjecent # like find peak etc
        n = len(nums)
        
        while True:
            isend = True
            for i in range(n-1):
                if nums[i] > nums[i+1]:
                    isend = False
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                
            
            if isend: break
        
        return nums



class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        k = len(nums) - k
        
        def getpivot(nums, start, end):
            random = randint(start, end)
            nums[end], nums[random] = nums[random], nums[end]
            pivot = end
            cpi = start
            for i in range(start, end):
                if nums[i] <= nums[pivot]:
                    nums[i], nums[cpi] = nums[cpi], nums[i]
                    cpi += 1
            
            nums[cpi], nums[pivot] = nums[pivot], nums[cpi]
            return cpi
        
        def quickselect(nums, start, end):
            if start == end: return nums[start]
            
            pivot_index = getpivot(nums, start, end)
            
            if pivot_index == k: 
                return nums[k]
            elif k < pivot_index:
                return quickselect(nums, start, pivot_index-1)
            else:
                return quickselect(nums,pivot_index+1, end)
            
        return quickselect(nums, 0, len(nums)-1)
                
        
        