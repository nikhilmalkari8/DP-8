def numberOfArithmeticSlices(nums):
    n = len(nums)
    if n < 3:
        return 0  # Not enough elements to form an arithmetic slice

    dp = [0] * n
    total_slices = 0

    for i in range(2, n):
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            dp[i] = dp[i - 1] + 1
        total_slices += dp[i]

    return total_slices
