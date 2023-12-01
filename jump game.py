def canJump(nums):
    def can_reach_end(position):
        # If the current position reaches or exceeds the last index, return True
        if position >= len(nums) - 1:
            return True
        
        max_jump = min(position + nums[position], len(nums) - 1)
        # Explore all possible jumps from the current position
        for next_position in range(position + 1, max_jump + 1):
            if can_reach_end(next_position):
                return True
        
        return False

    # Start from the first position (index 0)
    return can_reach_end(0)

# Test the function
nums = [2, 3, 1, 1, 4]
print(canJump(nums))  # Output: True
