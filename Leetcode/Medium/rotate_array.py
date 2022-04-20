nums = [1,2,3,4,5,6,7]
k = 3

def rotate(nums, k):
      """
      Do not return anything, modify nums in-place instead.
      """
      if k<len(nums):
          l = len(nums)-k
          nums_1 = nums[-k:]+(nums[0:l])
          for i in range(len(nums)):
              nums[i]=nums_1[i]
      else:
          ind = 0
          visited = []
          current_val = nums[ind]
          while len(visited)!=len(nums):
              next_ind = (ind+k)%len(nums)
              next_val = nums[next_ind]
              nums[next_ind] = current_val
              current_val = next_val
              if next_ind in visited:
                  ind = (next_ind+1)%len(nums)
                  current_val = nums[ind]
              else:
                  ind = next_ind
                  visited.append(next_ind)
                  
rotate(nums, k)
