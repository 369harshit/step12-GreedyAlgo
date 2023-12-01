def min_jumps(nums):
    n = len(nums)
    jumps = [float('inf')] * n
    jumps[0] = 0
    
    for i in range(n):
        for j in range(1, nums[i] + 1):
            if i + j < n:
                jumps[i + j] = min(jumps[i + j], jumps[i] + 1)
    
    return jumps[n - 1]

# Test the function
nums = [2, 3, 1, 1, 4]
result = min_jumps(nums)
print("Minimum number of jumps required:", result)
