from math import ceil, sqrt


class SquareRootDecomposition:

    def __init__(self,arr):
        self.arr = arr
        self.n = len(arr)
        self.block_size = int(sqrt(self.n))
        self.data = [float('inf')]*ceil(self.n // self.block_size)
        self.build()


    def build(self):

        for i in range(self.n):
           self.data[i // self.block_size] = min(self.data[i // self.block_size], self.arr[i])



    def update(self, index, new_val):
        self.arr[index] = new_val
        self.data[index // self.block_size] = min(self.data[index//self.block_size], new_val)
        return True


    def range(self, L, R):

        # 1..100,  23..73, 23..27

        res = float('inf')
        
        while L < R and  L % self.block_size != 0:
            res = min(res, self.arr[L])
            L += 1

        while L + self.block_size <= R:
            res = min(res, self.data[L // self.block_size])
            L += self.block_size

        while L <= R:
            res = min(res, self.arr[L])
            L += 1

        return res



a = [10,2,6,-3,5,8,1,15]
srd = SquareRootDecomposition(a)

print(srd.range(4, 7))







# class NumArray:

#     def __init__(nums, self): #preprocess
#         self.nums = nums
#         self.n = len(nums)
#         self.block_size = int(sqrt(n))
#         self.S = [0]*(ceil(self.n/self.block_size))

#         for i in range(self.n): 
#             self.S[i // self.block_size] += nums[i] #modify based on your requirement


#     def update(self, index, val):
#         change = val - self.nums[i]
#         self.S[i//self.block_size] += change
#         self.nums[i] = val


#     def range(left, right):
#         ans = 0
#         while left < right and left % self.block_size != 0:
#             ans += self.nums[left]
#             left += 1

#         while left + self.block_size <= R:
#             ans += self.S[left // self.block_size]
#             left += self.block_size


#         while left <= right:
#             ans += self.nums[left]
#             left += 1

#         return ans
